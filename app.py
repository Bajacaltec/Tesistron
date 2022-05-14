from numpy import append
import streamlit as st
import sqlite3

from sympy import expand
#APP que permite hacer el análisis para una tesis automaticamente al capturar los datos en la webapp
st.set_page_config(layout="wide")
#Usuario y contraseña
fol1,fol2,fol3,fol4=st.columns(4)
with fol3:
    usuario=st.text_input('Usuario')
with fol4:
    contraseña=st.text_input('Contraseña',type='password')
with fol1:
    st.title('Tesistron')
    
con = sqlite3.connect('data.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS B
            (Nombre TEXT,Número INT)""")


col1,col2=st.columns(2)
with col1:
    with st.expander('Identificación'):
        with st.form('Identificación'):
            nombre=st.text_input('Nombre',)
            registro=st.form_submit_button('registra',)
            if registro==True:
                cur.execute("INSERT INTO B(Nombre) VALUES(?)",(nombre))
                con.commit()
                con.close()
                
        
with col2:
    with st.expander('Resumen',expanded=True):
        st.subheader('Resumen',)
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        sumedad=cur.execute('''Select Nombre FROM B''')
        resumen=cur.fetchall()
        st.table(resumen)
    
