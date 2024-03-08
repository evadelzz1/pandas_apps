import FinanceDataReader as fdr
import pandas as pd
# 전 종목의 종목명과 전체코드 얻기
df_krx = fdr.StockListing('KRX').iloc[:, :3]

# 원하는 종목 stocks로 지정해서 가져오기
stocks = ["005930", "035720"]
df1 = pd.DataFrame()
for i in stocks:
    df = fdr.DataReader(i, '2018-06-30', "2018-07-30")
    df["Code"] = i
    df1 = pd.concat([df1, df])
df1.reset_index().merge(df_krx, how="left")

# 엑셀파일속 원하는 종목코드 리스트로 주식정보 가져오기
df2 = pd.read_excel("fdr_e01_주식보유현황.xlsx", dtype={"종목":str})
stocks = df2["종목"]
df1 = pd.DataFrame()
for i in stocks:
    df = fdr.DataReader(i, '2018-06-30', "2018-07-30")
    df["Code"] = i
    df1 = pd.concat([df1, df])
df1.reset_index().merge(df_krx, how="left")

# 엑셀파일속 원하는 종목명 리스트로 주식정보 가져오기
df3 = pd.read_excel("fdr_e01_주식보유현황.xlsx", sheet_name=1)
stocks = df3.merge(df_krx, how="left")["Symbol"]
df1 = pd.DataFrame()
for i in stocks:
    df = fdr.DataReader(i, '2018-06-30', "2018-07-30")
    df["Code"] = i
    df1 = pd.concat([df1, df])
df1.reset_index().merge(df_krx, how="left")