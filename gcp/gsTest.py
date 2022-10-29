import gspread
from google.oauth2.service_account import Credentials

# お決まりの文句
# 2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']

# ダウンロードしたjsonファイル名をクレデンシャル変数に設定。
credentials = Credentials.from_service_account_file("https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9c54a831-ed2d-4a91-a3a2-924f4d3db0ff/db-training-2022-9e93ad4d-77f3dc777dc4.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221026%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221026T115533Z&X-Amz-Expires=86400&X-Amz-Signature=21e20e16477e8b4e6b360349c567a1bc58f0ad686d0acf68bb23193cd033cf41&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22db-training-2022-9e93ad4d-77f3dc777dc4.json%22&x-id=GetObject", scopes=scope)

# OAuth2の資格情報を使用してGoogle APIにログイン。
gc = gspread.authorize(credentials)

# スプレッドシートIDを変数に格納する。
SPREADSHEET_KEY = '1qekHQj9aS4MtrDP_wERA3Egzro0rUY9xiXhpwfDwXMc'
# スプレッドシート（ブック）を開く
workbook = gc.open_by_key(SPREADSHEET_KEY)

