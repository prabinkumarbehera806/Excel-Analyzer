import streamlit as st
import pandas as pd
from io import BytesIO
from analyzer import ct_analysis, tus_analysis

st.set_page_config(page_title="Excel Analyzer", page_icon="📊")
st.title("Excel Analyzer App 📊")
st.write("Upload your Excel file to generate CT and TUS Pivot reports.")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "xls"])

if uploaded_file:
    try:
        # use openpyxl for .xlsx
        df = pd.read_excel(uploaded_file, engine="openpyxl")
        st.success("✅ File uploaded successfully!")

        if st.button("Run Analysis"):
            with st.spinner("Analyzing your data..."):
                ct_result = ct_analysis(df)
                tus_result = tus_analysis(df)

                def to_excel(dataframe):
                    output = BytesIO()
                    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
                        dataframe.to_excel(writer, index=False)
                    return output.getvalue()

                st.download_button(
                    label="📥 Download CT Analysis",
                    data=to_excel(ct_result),
                    file_name="CT_Pivot.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

                st.download_button(
                    label="📥 Download TUS Analysis",
                    data=to_excel(tus_result),
                    file_name="TUS_Pivot.xlsx",
                    mime="application/vnd.openxmlformats-officedocument-spreadsheetml.sheet"
                )

            st.success("✅ Analysis complete! Download your results above.")

    except Exception as e:
        st.error(f"⚠️ Something went wrong: {e}")
