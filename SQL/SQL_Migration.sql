-- PostgreSQL Schema Migration for Telemetry Data (Phase 1 Inception)
CREATE TABLE IF NOT EXISTS device_telemetry (
    id BIGSERIAL PRIMARY KEY,
    device_ip INET NOT NULL,
    status VARCHAR(20) NOT NULL,
    cpu_utilization NUMERIC(5, 2),
    latency_ms NUMERIC(7, 2),
    recorded_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- Index for high-frequency temporal querying
CREATE INDEX IF NOT EXISTS idx_telemetry_ip_time 
ON device_telemetry (device_ip, recorded_at DESC);
