# QGI (Streamlit Prototype, 2024)

> [!IMPORTANT]
> **Historical Prototype (2024)**: This repository contains the original Streamlit prototype of QGI developed in January 2024. For the modern enterprise Cloud Data & Applied ML platform, visit [AminAlAit/qgi](https://github.com/AminAlAit/qgi).

[![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Streamlit-1.36.0-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Status](https://img.shields.io/badge/Status-Historical_Prototype-blue?style=flat-square)](#)
[![License](https://img.shields.io/badge/License-Apache_2.0-green?style=flat-square)](LICENSE)

---

## The Origin Story

In January 2024, I wanted to answer a fundamental quantitative question: **Do historical macroeconomic and geopolitical trajectories across nations repeat with measurable cross-correlation?** 

When an emerging economy experiences a specific combination of debt-to-GDP spikes, currency devaluations, and demographic shifts, can we algorithmically match that multi-variable curve against historical precedents (e.g., Latin America in the 1980s, Southeast Asia in 1997, or Southern Europe in 2011) to understand what followed?

This repository was my first attempt at building that engine. Over a four-week sprint, I pulled together historical datasets from the World Bank and UN statistical divisions, built rolling cross-correlation routines in NumPy and SciPy, and wrapped the entire workflow in a Streamlit interface so I could explore hypotheses in real time.

---

## What This Prototype Does

1. **Cross-National Indicator Matching:** Select a target country and a historical time window, then query multi-indicator time series across 100+ nations.
2. **Lagged Correlation Engine:** Compute lead-lag correlation coefficients across temporal series to identify preceding and trailing indicators.
3. **Interactive Visual Exploration:** Render dynamic ECharts and Plotly charts directly inside Streamlit with configurable normalization and windowing filters.

---

## What I Learned (and Why We Outgrew It)

This prototype accomplished exactly what a prototype should: it validated the analytical concept and surfaced the engineering bottlenecks of scaling time-series analysis in a single Python process.

* **In-Memory Compute Ceilings:** Running all-to-all cross-correlations across hundreds of time series with varying sample frequencies on a single thread caused severe CPU and memory bottlenecks as dataset sizes grew.
* **The Monolith Problem:** Tightly coupling data ingestion, statistical computation, and front-end rendering inside a single Streamlit script meant that UI re-renders frequently triggered redundant compute cycles.
* **Data Freshness & Pipeline Fragility:** Relying on local CSVs and ad-hoc fetch scripts lacked schema validation, data versioning, and automated reconciliation.

These hard lessons directly informed the architecture of the new platform. In the modern [AminAlAit/qgi](https://github.com/AminAlAit/qgi) monorepo, we completely decoupled compute, storage, and visualization: adopting an enterprise cloud data warehouse, event-driven ingestion pipelines, reproducible ML feature stores, and dedicated client interfaces.

---

## Running the Prototype Locally

The codebase has been cleaned and pinned to Python 3.10 to ensure it boots cleanly on modern systems without dependency breakage.

### Prerequisites
* Python 3.10.x
* Git

### Quickstart

```bash
# 1. Clone the repository
git clone https://github.com/AminAlAit/qgi-streamlit.git
cd qgi-streamlit

# 2. Create and activate an isolated virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install pinned dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Launch the Streamlit application
streamlit run app.py
```

Open your browser at `http://localhost:8501` to explore the original interface.

---

## Repository Structure

```
qgi-streamlit/
├── data/               # Curated historical sample indicators & country pattern CSVs
├── constant/           # Portable path constants, sector mappings, and index metadata
├── database/           # Pattern ranking and country lookup helpers
├── pages/              # Streamlit multi-page views (Base, Patterns, Events, FAQ, Contact)
├── plotting/           # Interactive ECharts and timeline chart wrappers
├── utils/              # Cross-correlation, filtering, and time-series transformation logic
├── app.py              # Main Streamlit application entry point
├── requirements.txt    # Pinned, reproducible runtime dependencies
├── .gitignore          # Clean environment and OS exclusions
└── README.md           # Historical context and run instructions
```

---

## License

This historical codebase is released under the [Apache 2.0 License](LICENSE).
