import streamlit as st

st.title("Power calculator")
st.write("This app calculates the power of a number.")\

n=st.number_input("Enter the base number (n):", value=1, step=1)

square = n ** 2
cube = n ** 3
fifth_power = n ** 5

st.write(f"The square of {n} is: {square}")
st.write(f"The cube of {n} is: {cube}")
st.write(f"The fifth power of {n} is: {fifth_power}")
