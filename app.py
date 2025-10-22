
import streamlit as st
import pandas as pd
from io import BytesIO
from analyzer import ct_analysis, tus_analysis

st.set_page_config(page_title="Excel Analyzer", page_icon="📊")
st.title("Excel Analyzer App 📊")
st.write("Upload your Excel file to generate CT and TUS Analysis reports.")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "xls"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.success("✅ File uploaded successfully!")

    if st.button("Run Analysis"):
        with st.spinner("Analyzing your data..."):
            ct_result = ct_analysis(df)
            tus_result = tus_analysis(df)

            def to_excel(df):
                output = BytesIO()
                with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
                    df.to_excel(writer, index=False)
                return output.getvalue()

            st.download_button("📥 Download CT Analysis", to_excel(ct_result), "CT_Analysis.xlsx")
            st.download_button("📥 Download TUS Analysis", to_excel(tus_result), "TUS_Analysis.xlsx")

        st.success("Analysis completed!")
