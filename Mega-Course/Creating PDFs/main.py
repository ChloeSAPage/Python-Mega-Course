from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", )
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, rows in df.iterrows():
    pdf.add_page()

    # Header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,100)
    
    pdf.cell(w=0, h=12, txt=rows["Topic"], align="L", ln=1)
    
    for i in range(20, 298, 10):
        pdf.line(10, i, 200, i)
        
    # Footer
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=11)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=11, txt=rows["Topic"], align="R")

    for item in range(rows["Pages"] -1 ):
        pdf.add_page()
        # Footer on all pages
        pdf.ln(270)
        pdf.set_font(family="Times", style="I", size=11)
        pdf.set_text_color(100,100,100)
        pdf.cell(w=0, h=11, txt=rows["Topic"], align="R")
        for i in range(20, 298, 10):
            pdf.line(10, i, 200, i)

pdf.output("name.pdf")
 