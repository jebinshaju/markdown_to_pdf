import streamlit as st
import markdown2
import pdfkit
import io

def convert_markdown_to_html(markdown_text):
    try:
        # Convert Markdown to HTML
        html_content = markdown2.markdown(markdown_text)
        return html_content
    except Exception as e:
        st.error(f"Error converting Markdown to HTML: {e}")
        return None

def main():
    st.title("Markdown to PDF App")

    uploaded_file = st.sidebar.file_uploader("Upload a Markdown file", type=["md"])

    col1, col2 = st.columns(2)

    markdown_text = ""
    with col1:
        st.header("Input Markdown")
        if uploaded_file is not None:
            markdown_text = uploaded_file.read().decode("utf-8")
        else:
            markdown_text = st.text_area("Enter Markdown text here", height=400)

    if markdown_text:
        html_content = convert_markdown_to_html(markdown_text)

        if html_content:
            with col2:
                st.header("HTML Preview")
                st.markdown(html_content, unsafe_allow_html=True)

                font_size = st.slider('Select font size', min_value=10, max_value=36, value=14)
                font_family = st.selectbox('Select font family', options=['Arial', 'Helvetica', 'Times New Roman', 'Courier New', 'Verdana'])

                html_preview = f"""
                <div style="background-color: white; font-size: {font_size}px; font-family: {font_family};">
                    {html_content}
                </div>
                """

                pdf_options = {
                    'quiet': '',
                    'no-outline': None,
                    'dpi': 300,
                    'margin-top': '0mm',
                    'margin-right': '0mm',
                    'margin-bottom': '0mm',
                    'margin-left': '0mm',
                    'encoding': "UTF-8",
                    'custom-header' : [
                        ('Accept-Encoding', 'gzip')
                    ],
                    'no-outline': None,
                    'zoom': 1,
                    'page-size': 'Letter',
                    'minimum-font-size': font_size,
                }

                pdf_bytes = pdfkit.from_string(html_preview, False, options=pdf_options)

                if pdf_bytes:
                    pdf_preview_io = io.BytesIO(pdf_bytes)
                    pdf_preview_io.seek(0)

                    st.download_button(
                        label="Download PDF",
                        data=pdf_preview_io,
                        file_name="converted.pdf",
                        mime="application/pdf",
                        key="pdf_preview_download_button"
                    )
                else:
                    st.write("Failed to generate PDF.")

if __name__ == "__main__":
    main()
