import streamlit

#streamlit.title('My Parent\'s new Healthy Diner')
streamlit.title('My Mom\'s new Healthy Diner')

streamlit.header('Breakfast Favourites')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries,'])
# fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
# fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries', 'Banana'])
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), [])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
# streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)


#LESSON 9:
#new section to display fruityvice api  response

streamlit.header("Fruityvice Fruit Advice!")

#--ADDED AT THE END --
#Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response)
#streamlit.text(fruityvice_response.json())#jut writes te dat to the screen

# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it to the screenas a table
streamlit.dataframe(fruityvice_normalized)


import snowflake.connector
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchone()
streamlist.text("The fruit load list contains:")
streamlist.text(my_data_row)



