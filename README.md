# 🚰 Progressive Water Price Analytical System - Lab 2

An automated data engineering and visualization pipeline designed to scrape, structure, and analyze the progressive water pricing systems across 5 major provinces/cities in Vietnam (Hanoi, Hai Phong, Da Nang, Can Tho, and Ba Ria - Vung Tau). The project features a Command Line Interface (CLI) application enabling real-time data crawling from dynamic HTML sources and statistical chart rendering.

## 📌 Architectural & Technical Highlights
The codebase is structured to cleanly separate configuration, extraction logic, and visualization layers:
1. **Dynamic HTML Scraper:** Built with `pandas.read_html` utilizing a `BeautifulSoup4` (`bs4`) engine to parse and extract tabular data directly from raw localized legislative HTML files.
2. **Robust Content Mapping:** Features an explicit routing configuration mapping dictionary to dynamically navigate hidden structural variations and anomalies across different municipal table hierarchies.
3. **Keyword-based NLP Taxonomy:** Implements a keyword dictionary matrix to parse, sanitize, and segregate non-residential commercial sectors dynamically during runtime extraction.

---

## 📂 Project Directory Structure
```text
ADY201m PROJECT LAB2 - WATER PRICE/
├── .gitignore              # Prevents Python caching (__pycache__) and environment folders from staging
├── README.md               # Production-grade system documentation
├── config.py               # Central directory paths, commercial keywords matrix, and HTML parsing configurations
├── link.txt                # References to legal frameworks from the national database (Thu Vien Phap Luat)
├── main.py                 # Core CLI runtime driver managing application event loops
├── scraper.py              # Extraction layer splitting pipelines into Residential (DS1) & Economic (DS2) pipelines
├── visualizer.py           # Advanced chart rendering pipeline utilizing specialized Seaborn and Matplotlib engines
├── Scrawl_html/            # Local storage folder containing source municipal legislative HTML files
├── Dataset 1/              # Output directory for populated residential data structures
│   ├── baseline_hocu_dothi.csv # Progressive tier scaling metrics for urban citizens
│   └── welfare_ansinh_xh.csv   # Target social security welfare subsidies data
└── Dataset 2/              # Output directory for commercial data structures
    └── khoi_kinh_te.csv    # Consolidated pricing matrices for Administrative, Manufacturing, and Commercial sectors
