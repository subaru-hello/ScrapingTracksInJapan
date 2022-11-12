import csv
import pandas as pd
import tabula
import os


file_name_list = os.listdir("./track_pdfs")

for pdf_name in file_name_list:
  pdf = './track_pdfs/' + pdf_name
  df = tabula.read_pdf(pdf, lattice=True, pages ='all')
  csv_path = "./csvs/{0}.csv".format(pdf_name)
  
  if type(df) is list:
    for deep_df in df:
      deep_df.to_csv(csv_path, index=False, encoding="utf-8")
  else:
    df.to_csv(csv_path, index=False, encoding="utf-8")
