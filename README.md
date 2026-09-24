Asynchronous Network Telemetry Poller

Network Automation & Monitoring Platform
A comprehensive multi-year software initiative focused on building scalable telemetry collection, automated network diagnostics, PostgreSQL data pipelines, and real-time Splunk alert integrations.

20+ Mos.
Continuous Delivery
100%
Custom Built Stack
15k+
Telemetry Events/Sec
4 Peers
Core Engineering Team

An interactive engineering showcase and project artifact documenting 8+ months of continuous, collaborative network automation development. This self-contained web application serves as both a live demonstrator and a technical archive for asynchronous network telemetry ingestion, storage, monitoring, and visualization.

📌 Overview
The Asynchronous Network Telemetry Poller highlights an end-to-end data pipeline designed to collect, process, & display multi-vendor network device metrics in real time. The project packages system architecture diagrams, live code snippets, and multi-year milestone tracking into a unified interface.

🚀 Key Features
Multi-Year Interactive Timeline (2024–2026)
  * Categorizes project milestones from Phase 1 (Inception, Oct 2024) to Phase 4
    (Production, 2026).
  * Features active year filtering buttons and expandable deep-dive details.
Interactive SVG System Architecture Diagram
  * Visualizes end-to-end data flow: Network End-Devices --> Python Polling Daemons --> PostgreSQL Storage --> Splunk HEC --> REST API / UI Dashboards.
  * Includes click-to-inspect nodes for real-time data inspection.
Interactive Code Snippet Viewer
  * Tabbed, syntax-highlighted code blocks featuring Python poller daemons, SQL table          migrations, and GitHub Actions CI/CD workflows with built-in copy capabilities.
Built-in Source Exporter
  * Integrated export modal and clipboard utility that outputs a clean source template on
    demand.
Dynamic Dark/Light Mode
  * Full theme-switching support powered by Tailwind CSS w/ auto system preference detection.
Tech Stack & Skills Matrix
  * Comprehensive breakdown of core languages, database architecture, monitoring tooling, &
    network automation capabilities.


🚀 Features active year filtering buttons and expandable deep-dive details.Interactive SVG System Architecture DiagramVisualizes end-to-end data flow: Network End-Devices --> Python Polling Daemons -->PostgreSQL Storage --> Splunk HEC $\rightarrow$ REST API / UI Dashboards.

Includes click-to-inspect nodes for real-time data inspection.
Interactive Code Snippet Viewer
Tabbed, syntax-highlighted code blocks featuring Python poller daemons, SQL table migrations, and GitHub Actions CI/CD workflows with built-in copy capabilities.
Built-in Source ExporterIntegrated export modal and clipboard utility that outputs a clean source template on demand.
Dynamic Dark/Light ModeFull theme-switching support powered by Tailwind CSS with automatic system preference detection.
Tech Stack & Skills MatrixComprehensive breakdown of core languages, database architecture, monitoring tooling, and network automation capabilities.

🛠️ Core Tech Stack & Implementation
Icon  Technology  Category  Implementation Details  
PyPythonCore Development
Built asynchronous data collectors, daemon scripts, and custom log parsing routines using asyncio and standard library tooling.
PGPostgreSQL Data Layer
Designed normalized relational schemas, index strategies for time-series telemetry data, and optimized SQL query workflows.
SpSplunk Monitoring
Engineered HTTP Event Collector (HEC) JSON streams, constructed dashboard visualizations, and defined trigger thresholds.
GitGit & CI/CD DevOps
Managed parallel version control across a 4-person team using branch protection rules, GitHub Actions, and PR code reviews.
APIRESTful APIs
BackendStructured FastAPI JSON endpoints providing secure access to live router metrics, database records, and health checks.
NetNetwork AutoDomain Knowledge
Multi-vendor equipment configuration, interface state verification, telemetry aggregation, and automated error logging.

🗓️ Development Phases (2024 – 2026)
Phase 1: Inception & Architecture (Oct 2024)
Requirements gathering, database schema drafting, and initial asynchronous asyncio network polling proof-of-concept.

Phase 2: Database & Pipeline Integration (2025)
Relational schema normalization in PostgreSQL, Splunk HEC pipeline configuration, and setting up automated GitHub Actions for the team.

Phase 3: REST API & Dashboard Layer (Late 2025)
Exposing live router metrics via FastAPI JSON endpoints and building the interactive UI dashboard components.

Phase 4: Production & Documentation (2026)
Finalizing project showcase artifacts, query optimization, and packaging documentation into a single interactive browser utility.

📦 Getting Started
To view or deploy the project showcase locally:
Bash# Clone the repo
git clone https://github.com/your-username/Asynchronous-Network-Telemetry-Poller.git

# Navigate into the project folder
cd Asynchronous-Network-Telemetry-Poller

# Open index.html in any browser (no web server needed)
open index.html
