-- Time-Series Telemetry Table
CREATE TABLE IF NOT EXISTS device_telemetry (
    time TIMESTAMPTZ NOT NULL,
    device_id UUID NOT NULL REFERENCES network_devices(device_id),
    cpu_utilization REAL,
    memory_used_mb REAL,
    interfaces_status JSONB,
    latency_ms REAL
);

-- Convert to TimescaleDB Hypertable
SELECT create_hypertable('device_telemetry', 'time', if_not_exists => TRUE);

-- Indexes for Fast Query Retrieval
CREATE INDEX ON device_telemetry (device_id, time DESC);
CREATE INDEX ON device_telemetry USING BRIN (time);

-- Continuous Aggregate for Hourly Averages
CREATE MATERIALIZED VIEW telemetry_hourly_avg
WITH (timescaledb.continuous) AS
SELECT
    time_bucket('1 hour', time) AS bucket,
    device_id,
    AVG(cpu_utilization) AS avg_cpu,
    MAX(cpu_utilization) AS max_cpu
FROM device_telemetry
GROUP BY bucket, device_id;
