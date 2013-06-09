class CSVExportable:
    def get_csv_pairs(self):
        return []
    def get_header(self):
        return map(lambda x: x[0], self.get_csv_pairs())
    def get_row(self):
        return map(lambda x: x[1], self.get_csv_pairs())

class PDFExportable:
    def get_pdf_pairs(self):
        return []
    def get_pdfheader(self):
        return map(lambda x: x[0], self.get_pdf_pairs())
    def get_pdfrow(self):
        return map(lambda x: x[1], self.get_pdf_pairs())

