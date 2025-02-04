# erfordert pip install pyreadstat
# erfordert pip install openpyxl for df.to_excel
import pandas as pd
df = pd.read_spss("ZA5554_v1-0-0.sav")

df.to_excel("ZA5554_v1-0-0_v2.xlsx", index=False)

print(df.head(5))

