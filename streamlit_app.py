import streamlit as sl
import pandas as pd

sl.title('Breakfast Favorites')
sl.header('Breakfast Menu')
sl.text('🥣Omega 3 & Blubery Oatmeal')
sl.text('🥗Kale, Spinach & Rocket Smoothie')
sl.text('🐔Hard-Boiled Free-Range Egg')
sl.text('🥑🍞Avokado toast')


sl.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list=pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
sl.multiselect('Chjose fruits please',list(my_fruit_list.index))
sl.dataframe(my_fruit_list)
