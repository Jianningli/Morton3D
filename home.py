import streamlit as st
import pandas as pd

import Morton3D

st.title("3D Morton Encoding and Decoding.")

st.write('Morton Encoding...')
user_input_1 = st.text_input("specify the bit length:",9)
m=Morton3D.zorder(int(user_input_1))

st.write("enter the 3D integer coordinate:")

x = st.text_input("x",51)
y = st.text_input("y",20)
z = st.text_input("z",50)


mortonValue,mortonBinary=m.Morton(int(x),int(y),int(z))

st.write('the Morton value is...')
st.write(mortonValue)
st.write('the binary encoding is...')
st.write(mortonBinary)

st.write('Morton Decoding...')

user_input_2 = st.text_input("specify the binary encoding:",'000000000101111000010101001')
coordinate=m.deMorton(user_input_2,1)
st.write('the 3D integer coordinate is...')
st.write(coordinate)
