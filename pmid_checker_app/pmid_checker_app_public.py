
import streamlit as st
import csv
import pandas as pd
import os

# Function to load PMIDs from a CSV file
def load_pmids(filepath):
    try:
        with open(filepath, 'r', newline='') as f:
            reader = csv.reader(f)
            next(reader, None)  # Skip header
            return {row[0].strip() for row in reader if row and row[0].strip().isdigit()}
    except FileNotFoundError:
        st.error(f"Error: {filepath} not found.")
        return set()

# Load PMIDs from both files
base_path = os.path.dirname(__file__)
pmids1 = load_pmids(os.path.join(base_path, 'phibase_4.csv'))
pmids2 = load_pmids(os.path.join(base_path, 'phibase_5.csv'))

st.title("PMID Checker for PHI-base")
st.caption("PHI-base: 7 January 2026 • PHI-Canto: 13 January 2026")

# Single or batch input in one box
pmid_input = st.text_area("Enter one or more PMIDs (comma, space, or newline separated, max:50):")

results = []

if pmid_input:
    # Split input into individual PMIDs
    pmid_list = [p.strip() for p in pmid_input.replace(',', ' ').split() if p.strip().isdigit()]

    if not pmid_list:
        st.warning("Error: Please enter numeric PMIDs only.")
    else:
        st.write(f"Checking {len(pmid_list)} PMIDs...")
        for pmid in pmid_list:
            if pmid in pmids1 and pmid in pmids2:
                status = "Curated in BOTH PHI-base4 and PHI-Canto"
            elif pmid in pmids1:
                status = "Curated in PHI-base4"
            elif pmid in pmids2:
                status = "Curated in PHI-Canto"
            else:
                status = "Not curated"

            results.append({"PMID": pmid, "Status": status})
            # Display on screen
            if "Not curated" in status:
                st.info(f"{pmid}: ❌ {status}")
            else:
                st.success(f"{pmid}: ✅ {status}")

        # Convert results to DataFrame
        df_results = pd.DataFrame(results)

        # Download button
        st.download_button(
            label="Download Results as CSV",
            data=df_results.to_csv(index=False),
            file_name="pmid_check_results.csv",
            mime="text/csv"
        )
