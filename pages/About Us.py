import streamlit as st
col1,col2,col3 = st.columns([2,1,2])
with col2:
	st.markdown("# About Us")
st.divider()
col1,col2,col3 = st.columns([1,9,1])
with col2:
	st.markdown("#### We are a team driven by the problems that surround us and strive to provide a solution accessible to all.")
st.divider()
st.subheader("Introducing the team behind the project")
col1,col2,col3 = st.columns([2,1,2])
with col2:
	st.image("Jagan.jpg")
col1,col2,col3 = st.columns([5,1,5])
with col2:
	st.markdown("###### Jagan Mohan K")
col1,col2,col3 = st.columns([2,1,2])
with col2:
	st.image("Nithin.jpg")
col1,col2,col3 = st.columns([3,1,3])
with col2:
	st.markdown("###### Nithin kumar reddy V")
col1,col2,col3 = st.columns([2,1,2])
with col2:
	st.image("Abhinaya.jpg")
col1,col2,col3 = st.columns([4,1,4])
with col2:
	st.markdown("###### Abhinaya Rapolu")