PMID Checker for PHI-base

A lightweight Streamlit application for checking whether one or more PubMed IDs (PMIDs) have already been curated in PHI-base or PHI-Canto.

This tool helps prevent duplicate curation and supports efficient literature triage.

Overview

The app compares user-entered PMIDs against two internal datasets:

phibase_4.csv

phibase_5.csv

It reports whether each PMID is:

Curated in PHI-base4

Curated in PHI-Canto

Curated in BOTH

Not curated

The results can be viewed interactively and downloaded as a CSV file.

Features

Accepts up to 1000 PMIDs at once

Supports comma, space, or newline separation

Automatically ignores non-numeric input

Removes duplicate PMIDs

Interactive summary counts

Optional full results table

Downloadable CSV output

Fast membership checking using Python sets

Requirements

Python 3.9+

Streamlit

pandas

Install dependencies:

pip install streamlit pandas

File Structure
project_folder/
│
├── app.py
├── phibase_4.csv
├── phibase_5.csv
└── README.md


phibase_4.csv and phibase_5.csv must:

Be located in the same directory as the app

Contain PMIDs in the first column

Have one PMID per row

Running the App

From the project directory:

streamlit run app.py


The application will open automatically in your browser.

How It Works

CSV files are loaded into Python sets for fast lookup.

User input is cleaned and validated.

PMIDs are checked for membership in each dataset.

Status is assigned based on presence in one or both datasets.

Results are displayed and can be exported.

Input Rules

Maximum: 1000 PMIDs per submission

Only numeric PMIDs are accepted

Duplicate entries are automatically removed

Non-numeric values are ignored

Example Input
12345678
23456789, 34567890
45678901 56789012

Output Example
PMID	Status
12345678	Curated in PHI-base4
23456789	Curated in BOTH PHI-base4 and PHI-Canto
34567890	Not curated
Use Case

This tool is designed to support:

Literature triage

Pre-curation checks

Internal database maintenance

Avoiding duplicate curation

Rapid reporting during meetings or conferences

Future Improvements (Optional)

Potential enhancements:

Direct PubMed API lookup

DOI support

Integration with PHI-base export pipeline

Multi-version comparison

Dashboard summary statistics

Maintainer

Developed for PHI-base curation workflow.

If you'd like, I can also provide:

A more formal institutional version

A public-facing GitHub version

Or a version styled for documentation portals
