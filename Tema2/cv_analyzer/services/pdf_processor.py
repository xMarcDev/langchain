"""pdf_processor.py — Extracción de texto de archivos PDF subidos por el usuario."""

from io import BytesIO

import PyPDF2

NO_TEXT_ERROR = (
    "Error: El PDF no contiene texto extraíble. Por favor, asegúrese de que el archivo PDF "
    "no esté protegido o que contenga texto seleccionable."
)


def extraer_texto_pdf(pdf_file) -> str:
    """Extrae el texto de un PDF, separando cada página con un encabezado.

    Args:
        pdf_file: Objeto tipo archivo con el PDF (por ejemplo, el UploadedFile de Streamlit).

    Returns:
        El texto extraído, o un mensaje que empieza por "Error" si no se pudo leer.
    """
    try:
        pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_file.read()))
        full_text = ""

        for page_number, page in enumerate(pdf_reader.pages, start=1):
            page_text = page.extract_text() or ""
            if page_text.strip():
                full_text += f"\n--- PÁGINA {page_number} ---\n"
                full_text += page_text + "\n"

        full_text = full_text.strip()
        if not full_text:
            return NO_TEXT_ERROR
        return full_text

    except Exception as error:
        return f"Error al procesar el PDF: {error}"
