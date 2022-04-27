import streamlit

streamlit.title('🇮🇳 My Mom\'s New Healthy Diner 🇺🇸')


streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚 🐥 Hard-Bioled Free-Range Egg')
streamlit.text('🥑 🥪 Avocado Toast')

streamlit.header('🍌 🍓 Build Your Own Fruit Smoothie 🥝 🍇 🍹')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#streamlit.dataframe(my_fruit_list)

#Let's put a pick list here so customer can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#Display the table on the page
streamlit.dataframe(my_fruit_list)
