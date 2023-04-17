# import the streamlit library
import streamlit as st

# give a title to our app
st.title('App to find greatest of 3 Numbers')

# first number
first = st.number_input("Enter First Number:")

# second number
second = st.number_input("Enter Second Number:")

# third number
third = st.number_input("Enter Third Number:")

# compare status value
if(second > first):
	if(third > second):
		Max=third
	else:
		Max=second
elif (third > first):
	Max=third
else:
	Max=first	
	
st.success("The greatest of the numbers is {}.".format(Max))
