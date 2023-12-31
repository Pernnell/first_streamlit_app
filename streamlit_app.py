# all libraries at the top

import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

#streamlit.title('My Parent\'s new Healthy Diner')
streamlit.title('My Mom\'s new Healthy Diner')

streamlit.header('Breakfast Favourites')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# import pandas
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

#streamlit.header("Fruityvice Fruit Advice!")

#--ADDED AT THE END --
#Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call

# fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
# streamlit.write('The user entered ', fruit_choice)

# import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response)
#streamlit.text(fruityvice_response.json())#jut writes te dat to the screen

# take the json version of the response and normalize it
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it to the screenas a table
#streamlit.dataframe(fruityvice_normalized)

# REPLACEMENT FOR LESSON 9 PART

#LESSON 12 PART 1:
#new section to display fruityvice api  response
# streamlit.header("Fruityvice Fruit Advice!")
# try:
#   fruit_choice = streamlit.text_input('What fruit would you like information about?')
#   if not fruit_choice:
#     streamlit.error("Please select a fruit to get information. ")
#     #streamlit.write('The user entered ', fruit_choice)
#   else:
#     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#     streamlit.dataframe(fruityvice_normalized)
# 
# except URLError as e:
#   streamlit.error()

# REPLACEMENT FOR LESSON 12 PART-1

#LESSON 12 PART 2:

#create the repeatable code block (called a functiom)
def get_fruityvice_data(this_fruit_choice):
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      return fruityvice_normalized

#new section to display fruityvice api  response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information. ")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()



# import snowflake.connector
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)

# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()

# Let's Query Some Data, Instead
# my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
#my_data_row = my_cur.fetchone()

# streamlit.text("The fruit load list contains:")
# streamlit.text(my_data_row)

#  Let's Change the Streamlit Components to Make Things Look a Little Nicer
# streamlit.header("The fruit load list contains:")
# streamlit.dataframe(my_data_row)


#Oops! Let's Get All the Rows, Not Just One
# my_data_rows = my_cur.fetchall()
# streamlit.header("The fruit load list contains:")
# streamlit.dataframe(my_data_rows)

#--ADDED AT THE END --
# Can You Add A Second Text Entry Box? 

# add_my_fruit = streamlit.text_input('What fruit would you like to add?')
# streamlit.write('Thanks for adding ', add_my_fruit)
#streamlit.dataframe(add_my_fruit)

#This will not work correctly, but just go with it for now
# my_cur.execute("INSERT INTO fruit_load_list VALUES('from streamlit')")

import snowflake.connector
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
# my_data_rows = my_cur.fetchall()
# streamlit.text("The fruit list contains:")
# streamlit.text(my_data_rows)

# LESSON 12 PART 3: FUNCTIONS AS A BUTTON

# streamlit.header("The fruit load list contains:")
streamlit.header("View our Fruit List - Add your Favourites!:")
# Snowflake-related functions
def get_fruit_load_list():
      with my_cnx.cursor() as my_cur:
            my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
            return my_cur.fetchall()

# Add a button to load the fruit
if streamlit.button('Get Fruit List'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      my_data_rows = get_fruit_load_list()
      my_cnx.close()
      streamlit.dataframe(my_data_rows)


# LESSON 12 PART 4 - FUNCTIONALITY OF A BUTTON:

#Allow the end user to add a fruit to the list
# add_my_fruit = streamlit.text_input('What fruit would you like to add?')
# streamlit.write('Thanks for adding ', add_my_fruit)

#This will not work correctly, but just go with it for now
# my_cur.execute("INSERT INTO fruit_load_list VALUES('from streamlit')")


#Allow the end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
      with my_cnx.cursor() as my_cur:
           #  my_cur.execute("INSERT INTO fruit_load_list VALUES('from streamlit')")
            my_cur.execute("INSERT INTO fruit_load_list VALUES('" + new_fruit + "')")
            return "Thanks for adding " + new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the List'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])      
      back_from_function = insert_row_snowflake(add_my_fruit)
      my_cnx.close()
      streamlit.text(back_from_function)
      


#don't run anything past here while we troubleshoot
streamlit.stop()










