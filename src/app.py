import streamlit as st
import pandas as pd
from format import process_contracts

st.title("Excel Formatter")
st.write(
    "Upload your contracts XLSX file to format the license plates and export to CSV."
)

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file is not None:
    raw_df = pd.read_excel(uploaded_file)

    csv_data = process_contracts(raw_df)

    output_filename = st.text_input("Name your output file:", value="formatted_contracts.csv")

    if not output_filename.endswith(".csv"):
        output_filename += ".csv"

    st.download_button(
        label="Download Formatted CSV",
        data=csv_data,
        file_name=output_filename,
        mime="text/csv",
    )
