

# Markdown to PDF Streamlit App Documentation

## Overview

 This app allows users to convert Markdown text into HTML and preview the HTML content with customizable font size and font family. Users can also generate and download the corresponding PDF file.

## Installation

Ensure you have the required dependencies installed. You can install them via pip:

```bash
pip install streamlit markdown2 pdfkit
```

Additionally, make sure you have `wkhtmltopdf` installed. You can download it from the [official website](https://wkhtmltopdf.org/downloads.html).

## Usage

1. **Launch the App**: Run the Streamlit app by executing the following command in your terminal:

    ```bash
    streamlit run markdown_to_pdf_app.py
    ```

2. **Input Markdown Text**: You can either upload a Markdown file using the file uploader in the sidebar or directly enter Markdown text into the text area provided.

3. **Preview HTML**: The app will convert the Markdown text to HTML and display the HTML content in the right panel. You can customize the font size and font family using the sliders and select box provided.

4. **Generate PDF**: After customizing the HTML preview, click the "Download PDF" button to generate and download the corresponding PDF file. The PDF will be generated with the selected font size and font family.

## Dependencies

- **Streamlit**: Python library for building interactive web apps.
- **markdown2**: Python library for converting Markdown to HTML.
- **pdfkit**: Python library for generating PDF files from HTML.

## Additional Notes

- **Font Support**: The app supports various font families such as Arial, Helvetica, Times New Roman, Courier New, and Verdana.
- **PDF Generation**: PDF files are generated using `wkhtmltopdf`, so make sure it is properly installed on your system.
- **Error Handling**: The app provides error messages in case of any issues during HTML to PDF conversion.

## Support

If you encounter any issues or have any questions, please feel free to [open an issue](https://github.com/yourusername/markdown-to-pdf-app/issues) on GitHub.

## License

This app is licensed under the [MIT License](https://opensource.org/licenses/MIT).

