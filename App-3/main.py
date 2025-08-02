from fpdf import FPDF
import pandas as pd


pdf = FPDF()
df = pd.read_csv("topics.csv")
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=24)
    pdf.set_text_color(254, 0, 0)
    pdf.cell(200, 10, txt=row["Topic"], ln=True, align="L")
    pdf.line(10, 20, 200, 22)


pdf.output("output.pdf")
