import streamlit
streamlit.title("My Parents New Healthy Diner")
streamlit.header("🥣🥗 BREAKFAST MENU 🥑🍞")
streamlit.text("Oats and Milk")
streamlit.text("Bread and Peanut butter")
streamlit.text("Eggs and omlette")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
