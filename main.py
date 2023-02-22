
import pandas

data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors={"Black":0,"Cinnamon":0,"Gray":0}
colors["Gray"]=len(data[data["Primary Fur Color"]=="Gray"])
for color in colors:
    colors[color]=len(data[data["Primary Fur Color"]==color])
data_dict={
    "Fur Color":["Gray", "Cinnamon", "Black"],"Count":[colors["Gray"],colors["Cinnamon"],colors["Black"]]
}

df= pandas.DataFrame(data_dict)
print(df)