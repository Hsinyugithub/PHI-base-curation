import streamlit as st
import csv
import pandas as pd
import os

# ----------------------------
# Configuration
# ----------------------------
MAX_PMIDS = 1000

# ----------------------------
# Functions
# ----------------------------
def load_pmids(filepath):
    try:
        df = pd.read_csv(filepath, dtype=str)
        return set(df.iloc[:, 0].dropna().str.strip())
    except FileNotFoundError:
        st.error(f"Error: {filepath} not found.")
        return set()

# ----------------------------
# Load data
# ----------------------------
base_path = os.path.dirname(__file__)
pmids1 = load_pmids(os.path.join(base_path, "phibase_4.csv"))
pmids2 = load_pmids(os.path.join(base_path, "phibase_5.csv"))

# ----------------------------
# UI
# ----------------------------
st.title("PMID Checker for PHI-base")
st.caption("PHI-base: 7 January 2026 • PHI-Canto: 13 January 2026")

pmid_input = st.text_area(
    "Enter one or more PMIDs (comma, space, or newline separated, max: 1000):"
)

results = []

# ----------------------------
# Processing
# ----------------------------
if pmid_input:
    raw_tokens = pmid_input.replace(",", " ").split()

    pmid_list = list(dict.fromkeys(
        p.strip() for p in raw_tokens if p.strip().isdigit()
    ))

    invalid = [t for t in raw_tokens if not t.strip().isdigit()]

    if not pmid_list:
        st.warning("Please enter numeric PMIDs only.")
    else:
        if invalid:
            st.info(f"Ignored {len(invalid)} non-numeric entries.")

        if len(pmid_list) > MAX_PMIDS:
            st.warning(f"Only the first {MAX_PMIDS} PMIDs will be checked.")
            pmid_list = pmid_list[:MAX_PMIDS]

        st.write(f"Checking {len(pmid_list)} PMIDs...")

        for pmid in pmid_list:
            in_4 = pmid in pmids1
            in_5 = pmid in pmids2

            if in_4 and in_5:
                status = "Curated in BOTH PHI-base4 and PHI-Canto"
            elif in_4:
                status = "Curated in PHI-base4"
            elif in_5:
                status = "Curated in PHI-Canto"
            else:
                status = "Not curated"

            results.append({"PMID": pmid, "Status": status})

# ----------------------------
# Results
# ----------------------------
df_results = pd.DataFrame(results, columns=["PMID", "Status"])

if not df_results.empty:

    categories = [
        "Curated in PHI-base4",
        "Curated in PHI-Canto",
        "Curated in BOTH PHI-base4 and PHI-Canto",
        "Not curated"
    ]

    st.subheader("Summary of PMID Curation Status")

    # Clickable counts
    for cat in categories:
        count = df_results[df_results["Status"] == cat].shape[0]

        col1, col2 = st.columns([4, 1])
        col1.write(cat)

        if col2.button(str(count), key=f"btn_{cat}"):
            st.markdown(f"**PMIDs for: {cat}**")
            st.dataframe(df_results[df_results["Status"] == cat])

    # Optional full table
    show_full = st.toggle("Show full results table")

    if show_full:
        st.dataframe(df_results)

    # Download button
    st.download_button(
        label="Download Results as CSV",
        data=df_results.to_csv(index=False),
        file_name="pmid_check_results.csv",
        mime="text/csv"
    )
