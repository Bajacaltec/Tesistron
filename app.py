
from re import S
from numpy import append
import streamlit as st
st.set_page_config(layout="wide")
col1,col2,col3=st.columns(3)

import sqlite3
import time
import Usuarios.alberto as alberto
import inicio
import Usuarios.Lissvia as lissvia

from sympy import expand
#APP que permite hacer el análisis para una tesis automaticamente al capturar los datos en la webapp
#Usuario y contraseña
fol1,fol2,fol3,fol4=st.columns(4)
with fol1:
    st.image('BCtec.jpg','Baja Caltec',150)
with fol2:
    st.title('Tesistron')
with fol3:
    usuario=st.text_input('Usuario')
with fol4:
    contraseña=st.text_input('Contraseña',type='password')
if usuario=='Alberto' and contraseña=='1234':
    alberto.inicio()
elif usuario=='Lissvia' and contraseña=='1234':
    lissvia.inicio()
    
    

else:
    inicio.inicio()
    
            
 