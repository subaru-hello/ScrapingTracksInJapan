from turtle import title
import gspread
import os
import csv
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

load_dotenv()

# 2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

# ダウンロードしたjsonファイル名をクレデンシャル変数に設定。
credentials = Credentials.from_service_account_file("gcp.json", scopes=scope)

# OAuth2の資格情報を使用してGoogle APIにログイン。
gsc = gspread.authorize(credentials)

# スプレッドシートIDを変数に格納する。
SPREADSHEET_KEY = os.environ["SPR_KEY"]
# スプレッドシート（ブック）を開く
workbook = gsc.open_by_key(SPREADSHEET_KEY)

# pathに入る名前とワークシートに入る名前を作成
prefecture_nanes = ["kanagawa", "tokyo", "chiba", "saitama", "gunma"]
for prefecture_name in prefecture_nanes:
# csv_pathの検索
  csv_path = "./csvs/{0}_tracks.csv".format(prefecture_name)

# シートの作成＆検索
  workbook.add_worksheet(title=prefecture_name, rows=30, cols=30)

  new_worksheet = workbook.worksheet(prefecture_name)
  track_data= []

# csv読み込んでtrack_dataに入れる
  with open(csv_path, 'r') as f:
      reader = csv.reader(f)
      for row in reader:
        for name_address_pref in range(0,len(row)):
          track_data.append(row[name_address_pref])

# セルの値をまとめて更新する
  cell_list = new_worksheet.range('A1:C20')
  for i  in range(0,len(track_data)):
    cell_list[i].value = track_data[i]

  new_worksheet.update_cells(cell_list)