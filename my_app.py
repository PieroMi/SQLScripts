import streamlit as st

# Add a title to the app
st.title('My Streamlit App')

# Add some text to the app
st.write('Welcome to my app!')

# Add a slider to the app
x = st.slider('Select a value')

# Add a button to the app
if st.button('Submit'):
    st.write(f'Value selected: {x}')
    
!streamlit run my_app.py
