
import streamlit as st
import csv

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
pmids1 = load_pmids('phibase_4.csv')
pmids2 = load_pmids('phibase_5.csv')

# App title
st.title("PMID Checker for PHI-base")

# Input field
pmid = st.text_input("Enter PMID (digits only):")

if pmid:
    if not pmid.isdigit():
        st.warning("Error: PMID must be numeric.")
    else:
        if pmid in pmids1 and pmid in pmids2:
            st.success("✅ This publication is curated in BOTH PHI-base4 and PHI-Canto")
        elif pmid in pmids1:
            st.success("✅ This publication is curated in PHI-base4")
        elif pmid in pmids2:
            st.success("✅ This publication is curated in PHI-Canto")
        else:
            st.info("✅ Go ahead, you can curate this publication!")
