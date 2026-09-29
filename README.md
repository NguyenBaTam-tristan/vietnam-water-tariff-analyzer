# 🚰 Vietnam Water Tariff Analyzer

An automated data pipeline and command-line tool that scrapes, structures, and visualizes **progressive water pricing** across five major Vietnamese provinces and cities: **Hanoi, Hai Phong, Da Nang, Can Tho, and Ba Ria - Vung Tau**.

The tool parses legal documents saved as HTML pages, extracts the pricing tables, splits them into residential and commercial datasets, and renders comparison charts from the results.

> Originally developed as **Lab 2** of the ADY201m course project.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Datasets](#datasets)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Tech Stack](#tech-stack)
- [Limitations](#limitations)
- [Contributing](#contributing)

## Features

- **HTML table scraping.** Reads tariff tables directly from locally saved legal HTML files using `pandas.read_html` with a `BeautifulSoup4` parser.
- **Per-city routing configuration.** A mapping dictionary handles the structural differences and quirks between each city's table layout.
- **Keyword-based sector classification.** A keyword matrix separates non-residential sectors (administrative, manufacturing, commercial) from household pricing during extraction.
- **Two clean output datasets.** Residential and commercial data are exported as separate CSV files.
- **Chart rendering.** Uses Seaborn and Matplotlib to visualize price tiers and compare cities.
- **Interactive CLI.** A menu-driven `main.py` runs the whole workflow.

## How It Works

```
Legal HTML files          Scraper                 Datasets               Visualizer
(Scrawl_html/)   ───▶   (scraper.py)   ───▶   (CSV files)   ───▶   (visualizer.py)
                        uses config.py          Dataset 1 & 2           charts & stats
```

1. **Configure.** `config.py` holds directory paths, the commercial keyword matrix, and the HTML parsing rules for each city.
2. **Extract.** `scraper.py` runs two pipelines: residential (Dataset 1) and economic sectors (Dataset 2).
3. **Visualize.** `visualizer.py` reads the CSVs and draws the charts.
4. **Run.** `main.py` ties everything together in an interactive CLI.

## Project Structure

```
Water_Price_Analysis/
├── .gitignore               # Ignores Python cache and environment folders
├── README.md                # Project documentation
├── config.py                # Paths, keyword matrix, and HTML parsing settings
├── link.txt                 # Links to the legal sources (Thu Vien Phap Luat)
├── main.py                  # CLI entry point
├── scraper.py               # Extraction pipelines for residential and economic data
├── visualizer.py            # Chart rendering with Seaborn and Matplotlib
├── Scrawl_html/             # Saved source HTML files from municipal regulations
├── Dataset 1/               # Residential output
│   ├── baseline_hocu_dothi.csv   # Progressive tier pricing for urban households
│   └── welfare_ansinh_xh.csv     # Social welfare subsidy data
├── Dataset 2/               # Commercial output
│   └── khoi_kinh_te.csv          # Pricing for administrative, manufacturing, and commercial sectors
└── Draft&Test Notebook/     # Exploratory drafts and test notebooks
```

## Datasets

| Dataset | File | Description |
|---------|------|-------------|
| Dataset 1 | `baseline_hocu_dothi.csv` | Progressive tier pricing for urban residential users |
| Dataset 1 | `welfare_ansinh_xh.csv` | Pricing and subsidies related to social security welfare |
| Dataset 2 | `khoi_kinh_te.csv` | Consolidated pricing for administrative, manufacturing, and commercial sectors |

## Getting Started

### Prerequisites

- Python 3.8 or newer
- The libraries listed below

### Installation

```bash
git clone https://github.com/NguyenBaTam-tristan/Water_Price_Analysis.git
cd Water_Price_Analysis
pip install pandas beautifulsoup4 lxml matplotlib seaborn
```

> The repository does not include a `requirements.txt` yet. If you hit an import error, install the missing package with `pip`.

## Usage

Run the CLI from the project root:

```bash
python main.py
```

Follow the on-screen menu to scrape the data and generate charts. Output CSVs are written to `Dataset 1/` and `Dataset 2/`.

## Data Sources

The pricing data comes from official municipal regulations on water tariffs. The references are listed in [`link.txt`](link.txt) and come from the Vietnamese national legal database (Thu Vien Phap Luat). The HTML files in `Scrawl_html/` are local copies of those documents.

## Tech Stack

| Purpose | Tool |
|---------|------|
| Language | Python |
| Data handling | pandas |
| HTML parsing | BeautifulSoup4 (`bs4`) |
| Visualization | Matplotlib, Seaborn |

## Limitations

- The scraper depends on the current layout of the saved HTML files. New cities or regulation formats need a new entry in the routing configuration in `config.py`.
- Keyword-based sector classification may misclassify entries that use unusual wording.
- Tariffs change over time, so check the source documents for the latest official prices.

## Contributing

Suggestions and improvements are welcome:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-city`
3. Commit your changes
4. Push the branch and open a Pull Request
