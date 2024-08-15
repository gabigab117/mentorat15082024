import re
from pypdf import PdfReader


reader = PdfReader("monpdf.pdf")
page = reader.pages[0]
text = page.extract_text()

print("______")

a = re.findall(r'[\w.]+@\w+\.[a-z]{2,4}', text)
print(a)


## Une classe à la va vite, mais exemple rapide en POO

# class PdfEmailExtractor:
#     def __init__(self, pdf_path: str):
#         self.pdf = PdfReader(pdf_path)
#         self.text = ""
#         self.emails = []
#
#     def extract_text_from_page(self, page_number: int):
#         page = self.pdf.pages[page_number]
#         self.text = page.extract_text()
#
#     def extract_text_from_all_pages(self):
#         for page in self.pdf.pages:
#             self.text += page.extract_text()
#
#     def get_emails(self):
#         emails = re.findall(r'[\w.]+@\w+\.[a-z]{2,4}', self.text)
#         self.emails = emails
#         return self.emails
#
#
# r = PdfEmailExtractor("monpdf.pdf")
# r.extract_text_from_all_pages()
# r.get_emails()
# print(r.emails)
