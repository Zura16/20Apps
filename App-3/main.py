from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    topic = row["Topic"]
    num_pages = row["Pages"]

    # --- First Page ---
    pdf.add_page()

    # Draw lines (horizontal lines every 10mm)
    for y in range(20, 290, 10):
        pdf.line(10, y, 200, y)

    # Add header
    pdf.set_font("Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.set_y(10)
    pdf.cell(0, 10, txt=topic, ln=True, align="L")
    pdf.ln(10)  # Move cursor to avoid overlapping lines

    # Add footer
    pdf.set_y(-15)
    pdf.set_font("Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(0, 10, txt=topic, align="R")

    # --- Additional Pages ---
    for _ in range(num_pages - 1):
        pdf.add_page()

        # Draw lines
        for y in range(20, 290, 10):
            pdf.line(10, y, 200, y)

        # Footer
        pdf.set_y(-15)
        pdf.set_font("Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(0, 10, txt=topic, align="R")

# Export PDF
pdf.output("output.pdf")
