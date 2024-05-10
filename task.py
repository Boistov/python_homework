from datetime import datetime

date_str = input()
date_format = "%m/%d/%Y"
input_date = datetime.strptime(date_str, date_format)

converted_date = input_date.strftime("%Y%d%m")

print(converted_date)