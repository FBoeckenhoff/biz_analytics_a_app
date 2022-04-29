import streamlit as st
from scipy.stats import linregress

st.title("Number of Humans on Earth")
st.text(" ")
st.text("Move the slider to discover the number of humans in a given year.")


years = [2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003,
         2002, 2001, 2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990, 1989, 1988, 1987, 1986, 1985,
         1984, 1983, 1982, 1981, 1980, 1979, 1978, 1977, 1976, 1975, 1974, 1973, 1972, 1971, 1970, 1969, 1968, 1967,
         1966, 1965, 1964, 1963, 1962, 1961, 1960, 1959, 1958, 1957, 1956, 1955, 1954, 1953, 1952, 1951
         ]
population = [7794798739, 7713468100, 7631091040, 7547858925, 7464022049, 7379797139, 7295290765, 7210581976,
              7125828059, 7041194301, 6956823603, 6872767093, 6789088686, 6705946610, 6623517833, 6541907027,
              6461159389, 6381185114, 6301773188, 6222626606, 6143493823, 6064239055, 5984793942, 5905045788,
              5824891951, 5744212979, 5663150427, 5581597546, 5498919809, 5414289444, 5327231061, 5237441558,
              5145426008, 5052522147, 4960567912, 4870921740, 4784011621, 4699569304, 4617386542, 4536996762,
              4458003514, 4380506100, 4304533501, 4229506060, 4154666864, 4079480606, 4003794172, 3927780238,
              3851650245, 3775759617, 3700437046, 3625680627, 3551599127, 3478769962, 3407922630, 3339583597,
              3273978338, 3211001009, 3150420795, 3091843507, 3034949748, 2979576185, 2925686705, 2873306090,
              2822443282, 2773019936, 2724846741, 2677608960, 2630861562, 2584034261
              ]

regression_result = linregress(years, population)
scipy_slope = regression_result.slope
scipy_intercept = regression_result.intercept
desired_year = st.slider(label="Select a year", min_value=1951, max_value=2150, value=2022, step=1, format=None,
                         disabled=False)


def scipy_model(desired_year):
    model_result = scipy_slope * desired_year + scipy_intercept
    return model_result


model_result = scipy_model(desired_year)
selected_population = model_result if desired_year > 2020 else population[years.index(desired_year)]


def thousand_sep(num):
    return "{:,}".format(num)


st.text(" ")
if desired_year > 2020:
    st.write("The _**projected**_ global population in the year", str(desired_year), "will be",
             thousand_sep(round(selected_population)), ".")
else:
    st.write("The _**actual**_ global population in the year", str(desired_year), "was",
             thousand_sep(selected_population), ".")
st.text(" ")
st.text(" ")

st.text("Select your year of birth to find out how global population has increased.")
birth_year = st.number_input("Year of birth", min_value=1951, max_value=2020, value=1980, step=1)
st.text(" ")
st.write("When you were born, global population was at", thousand_sep(population[years.index(birth_year)]), ".")
st.write("Since then, it has increased by", thousand_sep(round(scipy_model(2022) - population[years.index(birth_year)])), ".")

st.text(" ")
if st.button("Information on the model and its data", help="Click here for further information"):
    "The population numbers between 1951 and 2020 are historical values from the following source: "
    "United Nations. (2020). World Population Prospects 2019. https://population.un.org/wpp/"
    "Starting from 2021, the estimations are calculated based on a linear regression model based on the previous years."
    "Author Finn Böckenhoff"

#%%

#%%
