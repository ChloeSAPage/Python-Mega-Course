from pathlib import Path
import glob
from fpdf import FPDF

my_files = glob.glob("Text+Files/*.txt")

# Create the PDF
pdf = FPDF(orientation="P", unit="mm", format = "A4")

# Go through each text file
for file in my_files:
    
    # Each Page starts with the name of the Text file
    filename = Path(file).stem
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=25)
    pdf.cell(w=0, h=12, txt=f"{filename.capitalize()}", align="L", ln=1)
    
    # Add the Content
    with open(file, "r") as textfile:
        contents = textfile.read()

    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=contents)


pdf.output("animals.pdf")