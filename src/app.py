import streamlit as st
import pandas as pd
from format import process_contracts

st.title("Excel Formatter")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file is not None:
    raw_df = pd.read_excel(uploaded_file)

    start_id = st.number_input("Enter last number from previous csv file(If you are at the start of the month use 0)", value = 0, step = 1)
    csv_data = process_contracts(raw_df, start_id)

    output_filename = st.text_input("Name your file:", value="formatted_contracts.csv")

    if not output_filename.endswith(".csv"):
        output_filename += ".csv"

    st.download_button(
        label="Download Formatted CSV",
        data=csv_data,
        file_name=output_filename,
        mime="text/csv",
    )
