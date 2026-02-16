# PMID Checker for PHI-base

A lightweight Streamlit web application to check whether PubMed IDs
(PMIDs) have been curated in **PHI-base 4** and/or **PHI-Canto**.

This tool is designed to support biocuration workflows by quickly
identifying the curation status of single or multiple publications.

------------------------------------------------------------------------

## Features

-   ✅ Check one or multiple PMIDs at once (batch input)
-   📂 Compares against two local CSV files:
    -   `phibase_4.csv`
    -   `phibase_5.csv` (PHI-Canto)
-   📊 Clear on-screen status indicators
-   ⬇️ Download results as a CSV file
-   ⚡ Fast and simple interface using Streamlit

------------------------------------------------------------------------

## Interface

Users can paste PMIDs separated by: - commas\
- spaces\
- new lines

Maximum recommended input: **50 PMIDs per check**

------------------------------------------------------------------------

## Status Definitions

  -----------------------------------------------------------------------
  Status                         Meaning
  ------------------------------ ----------------------------------------
  Curated in BOTH PHI-base4 and  PMID appears in both datasets
  PHI-Canto                      

  Curated in PHI-base4           PMID curated only in PHI-base 4

  Curated in PHI-Canto           PMID curated only in PHI-Canto

  Not curated                    PMID not found in either dataset
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## File Structure

. ├── app.py ├── phibase_4.csv ├── phibase_5.csv └── README.md

-   CSV files must contain PMIDs in the **first column**
-   A header row is expected and will be skipped

------------------------------------------------------------------------

## Installation

### 1. Clone the repository

``` bash
git clone <repository-url>
cd <repository-name>
```

### 2. Install dependencies

``` bash
pip install streamlit pandas
```

------------------------------------------------------------------------

## Running the App

``` bash
streamlit run app.py
```

The app will open automatically in your default web browser.

------------------------------------------------------------------------

## Notes

-   PMIDs must be numeric
-   Duplicate PMIDs are allowed but may be filtered in future versions
-   CSV files are loaded locally; no external APIs are used

------------------------------------------------------------------------

## Version Information

-   **PHI-base reference date:** 7 January 2026\
-   **PHI-Canto reference date:** 13 January 2026

(Displayed in the app interface)

------------------------------------------------------------------------

## License

Internal tool for PHI-base curation support.
