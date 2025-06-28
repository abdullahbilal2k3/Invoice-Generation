import pandas as pd
import glob
from fpdf import FPDF
filepaths = glob.glob("Invoices/*.xlsx" )

for filepath in filepaths:
    df = pd.read_excel(filepath , sheet_name= "Sheet 1")
    print(df)