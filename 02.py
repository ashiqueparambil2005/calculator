import streamlit as st
from calculator_logic import add, subtract, multiply, divide

st.title('XAIDOR Calculator')    

col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input('Enter first number', value=0)

with col2:
    num2 = st.number_input('Enter second number', value=0)

operation = st.selectbox('Select operation', ['Add', 'Subtract', 'Multiply', 'Divide'])

if st.button('Calculate'):
    if operation == 'Add':
        result = add(num1, num2)
    elif operation == 'Subtract':
        result = subtract(num1, num2)
    elif operation == 'Multiply':
        result = multiply(num1, num2)
    elif operation == 'Divide':
        result = divide(num1, num2)
    st.balloons()
    st.write('Result:', result)



