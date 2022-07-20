import streamlit
streamlit.title("My Parents New Healthy Diner")
streamlit.header("🥣🥗 BREAKFAST MENU 🥑🍞")
streamlit.text("Oats and Milk")
streamlit.text("Bread and Peanut butter")
streamlit.text("Eggs and omlette")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# pick list to pick the fruit they want to include
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Honeydew','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# display api response 
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")


# normalise the data
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output to display
streamlit.dataframe(fruityvice_normalized)
