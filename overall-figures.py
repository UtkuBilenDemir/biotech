#%% Dependencies
import pandas as pd
import altair as alt

#%% Focus countries: Austria, Sweden, Ireland, Slovenia
biotech_firms = pd.read_csv("./01_data/biotech_firms.csv")

#%% Choose countries
focus_countries = ["Austria", "Sweden", "Ireland", "Slovenia"]
country_indexes = [i for i,x in enumerate(biotech_firms.iloc[:, 0]) if "".join(x_0 for x_0 in x if x_0.isalnum()) in focus_countries]
biotech_firms = biotech_firms.iloc[country_indexes,]

#%% DataFrame to Time Series
biotech_firms = biotech_firms.transpose()
biotech_firms_TimeSeries = biotech_firms.unstack()
country_name_series = []
for i, cou in enumerate(focus_countries):
    country_name_series.extend(len(biotech_firms_TimeSeries)//len(focus_countries) * [cou])
biotech_firms_TimeSeries = pd.DataFrame(biotech_firms_TimeSeries)
biotech_firms_TimeSeries["Country"] = country_name_series
biotech_firms_TimeSeries = biotech_firms_TimeSeries.reset_index(drop=True)
index_to_go = list(range(0,64, 16)) + list(range(15,64, 16))
biotech_firms_TimeSeries = biotech_firms_TimeSeries.drop(index_to_go)
biotech_firms_TimeSeries["Year"] = [int(x) for x in list(biotech_firms.index.values)[1:15]] * 4
biotech_firms_TimeSeries.columns.values[0] = "number"
biotech_firms_TimeSeries["number_of_firms"] = biotech_firms_TimeSeries.iloc[:,0]
#%% Are plot through Altair
raw =  chart = alt.Chart(biotech_firms_TimeSeries.dropna()).mark_line().encode(
    x="Year",
    y="number_of_firms",
    color="Country"
)

background = raw.encode(opacity=alt.value(0.2))

chart = alt.Chart(biotech_firms_TimeSeries).mark_line().encode(
    x="Year",
    y=alt.Y("number_of_firms" , impute=alt.ImputeParams(method="mean")),
    color="Country"
)
background + chart


#%%
biotech_firms_TimeSeries.dropna()






#%% TEST
biotech_firms_TimeSeries.head(20)

#%% 
from vega_datasets import data

source = data.iowa_electricity()



# %%
bla = alt.Chart(source).mark_area().encode(
    x="year:T",
    y="net_generation:Q",
    color="source:N"
)
# %%
len(test)
# %%
source

#%% 
dims(test)
# %%