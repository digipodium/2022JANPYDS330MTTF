## to run, use cmd:
## streamlit run app.py
##
import streamlit as st

# text display
st.title('Hello World')
st.header('Streamlit is awesome!')
st.subheader('Here is a subtitle')
st.text('Here is some text')
st.write('Here is some text, too {this is a magic function}')
x = [1, 2, 3]
st.write(x)
student = {
    'name': 'John',
    'age': 25,
    'courses': ['Math', 'CompSci']
}
st.write(student)
st.success('Yay!')
st.error('Boo!')
st.info('This is some info')
st.warning('This is a warning')
st.markdown('This is a **markdown** text')
st.image('meh.gif')

# form input
st.subheader('User Input')
name = st.text_input('What is your name?')
st.write(f"Hello, {name}")

a = st.number_input('A number')
b = st.number_input('Another number')
st.write(f'{a} + {b} = {a + b}')

with st.form('form1',clear_on_submit=True):
    name = st.text_input('Name')
    age = st.number_input('Age',min_value=0,max_value=100)
    gender = st.radio("Select a gender",options=['male','female','other'])
    education = st.selectbox("select education",options=['graduate','post-graduate','school','no education'])
    btn = st.form_submit_button("submit")

    if btn:
        st.write(f'form submitted')
    
    