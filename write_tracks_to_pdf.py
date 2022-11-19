import csv
import pandas as pd
import tabula
import os


file_name_list = os.listdir("./track_pdfs")

def rename_index(df):
    return df.rename(columns={"個人利用": "個人利用a.m", "Unnamed: 0": "個人利用p.m"})

def main():
  for pdf_name in file_name_list:
    pdf = './track_pdfs/' + pdf_name
    df = tabula.read_pdf(pdf, lattice=True, pages ='all')
    csv_path = "./csvs/{0}.csv".format(pdf_name)

    if type(df) is list:
      for deep_df in df:
        renamed_df = rename_index(deep_df)
        renamed_df.to_csv(csv_path, index=False, encoding="utf-8")
        print(renamed_df)
    else:
      renamed_df = rename_index(df)
      renamed_df.to_csv(csv_path, index=False, encoding="utf-8")
      print(renamed_df)

main()
