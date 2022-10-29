import gspread
import os
from google.oauth2.service_account import Credentials

os.environ.SPR

# 2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

# ダウンロードしたjsonファイル名をクレデンシャル変数に設定。
credentials = Credentials.from_service_account_file("./gcp/gcp.json", scopes=scope)

# OAuth2の資格情報を使用してGoogle APIにログイン。
gc = gspread.authorize(credentials)

# スプレッドシートIDを変数に格納する。
SPREADSHEET_KEY = os.environ.SPR
# スプレッドシート（ブック）を開く
workbook = gc.open_by_key(SPREADSHEET_KEY)

# シートの一覧を取得する。（リスト形式）
worksheets = workbook.worksheets()
print(worksheets)
# シートを開く
worksheet = workbook.worksheet("シート2")
# セルA1に”test value”という文字列を代入する。
worksheet.update_cell(1, 1, "test value")
