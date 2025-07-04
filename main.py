import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
from datetime import date
from itertools import islice

filepaths = glob.glob("Invoices/*.xlsx" )

for filepath in filepaths:

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    invoicenr = filename.split("-")[0]
    tdate = date.today()

    pdf.set_font(family="Times", size= 16, style="B")
    pdf.cell( w = 50 , h= 8, txt=f"Invoice nr. {invoicenr} ",ln =1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date {tdate}",ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    columns = df.columns
    columns = [item.replace("_"," ").title() for item in columns]
    pdf.set_font(family="Times", size=12,style= "B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=50, h=8, txt=columns[1], border=1)
    pdf.cell(w=50, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=50, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=50, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    price = df["total_price"].sum()
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=50, h=8, txt="", border=1)
    pdf.cell(w=50, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(price) , border=1, ln=1)




    pdf.set_font(family="Times", size= 8, style="B")
    pdf.cell( w = 50 , h= 8, txt=f"Total price= {price} ",ln =1)

    pdf.output(f"PDFs/{filename}.pdf")