import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("Invoices/*.xlsx")

for filepath in filepaths:
    # Creating a seperate PDF for each excel file
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Adding the Invoice number to the top of the page
    filename = Path(filepath).stem
    invoice_num, date = filename.split("-")
    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(w=50, h=8, txt=f"Invoice Number. {invoice_num}", ln=1)

    # Adding the date
    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

    # Adding the data
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # Add the column name
    column = df.columns
    column = [item.replace("_", " ").title() for item in column]
    pdf.cell(w=30, h=8, txt=str(column[0]), border=1)
    pdf.cell(w=60, h=8, txt=str(column[1]), border=1)
    pdf.cell(w=40, h=8, txt=str(column[2]), border=1)
    pdf.cell(w=30, h=8, txt=str(column[3]), border=1)
    pdf.cell(w=30, h=8, txt=str(column[4]), border=1, ln=1)

    # Add the data for each column
    for index, row in df.iterrows():
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=60, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=40, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    # Add total price
    total_price = df["total_price"].sum()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=60, h=8, txt="", border=1)
    pdf.cell(w=40, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_price), border=1, ln=1)
    pdf.cell(w=30, h=8, txt=f"The total price is {total_price}", ln=1)

    # Company name and logo
    pdf.set_font(family="Times", style="B", size=17)
    pdf.cell(w=30, h=8, txt=f"PythonHow")
    pdf.image("pythonhow.png", w=10)

    pdf.output(f"PDFs/{filename}.pdf")
