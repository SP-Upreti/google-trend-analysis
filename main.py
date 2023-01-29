import pandas as pd
from matplotlib import pyplot as pp
from pytrends.request import TrendReq
 
pytrend = TrendReq()

#requesting data from google API
pytrend.build_payload(kw_list=["chatgpt"])
df = pytrend.interest_by_region()
google_data = df.head(200)

#making pandas dataframe of obtained  data
data = pd.DataFrame(google_data)


#sorting the values on the basis of data in descending order
data2 = data.sort_values(by="chatgpt", ascending=False)


#getting top 10 countries with highest score
top = data2.iloc[0:10]
top_ten = pd.DataFrame(top)
print("data frame")
print(top_ten)

#saving obtained data in CSV format
top_ten.to_csv("data.csv")
#reading the saved data
topdata = pd.read_csv("data.csv")

#getting data for bar graph
country = topdata["geoName"].to_list()
score = topdata["chatgpt"]

#showing data in bargraph
pp.bar(country, score, label = "Country")
pp.title("Top 10 countries where chatgpt is most popular.")
pp.xlabel("countries")
pp.ylabel("score")
pp.show()