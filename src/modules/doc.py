from docx import Document
import os


def open_docx(dirname, filename):
    docx_path = os.path.join(dirname, filename)
    document = Document(docx_path)
    return document


def handle_table(docx):
    table = docx.tables[0]
    replace_text(table, 0, 2, '2022年3月13日15时59分')
    docx.save('../static/tmp/demo.docx')


def replace_text(table, row, col, text):
    run = table.cell(row, col).paragraphs[0].runs[0]
    run.text = run.text.replace(run.text, text)


if __name__ == '__main__':
    docx_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + '\\static\\docx'
    doc = open_docx(docx_dir, 'doc1.docx')
    handle_table(doc)
