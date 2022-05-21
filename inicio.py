import streamlit as st

def inicio():
    st.title('Bienvenido a el tesistron')
    st.success('El mejor apoyo para iniciar, desarrollar, terminar una tésis y finalmente publicar tu trabajo')
    col1,col2=st.columns(2)
    with col2:
        st.video('https://www.youtube.com/watch?v=dsBTlaHxG2Q')
    