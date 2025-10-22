import streamlit as st
from analyzer import analyze_excel

st.set_page_config(page_title="Excel Analyzer", page_icon="📊", layout="centered")

st.title("📈 Excel Analyzer App")
st.markdown("Upload your raw Excel file to generate CT and TUS Analysis reports.")

# Upload file
uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded_file:
    st.success("File uploaded successfully!")

    # Process the file
    with st.spinner("Analyzing data..."):
        ct_output, tus_output = analyze_excel(uploaded_file)
        st.success("Analysis completed!")

    # Download buttons
    with open(ct_output, "rb") as f:
        st.download_button("📥 Download CT Analysis", f, file_name=ct_output)

    with open(tus_output, "rb") as f:
        st.download_button("📥 Download TUS Analysis", f, file_name=tus_output)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit and pandas.")
