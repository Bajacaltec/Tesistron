import time
from sqlalchemy import false, true
import streamlit as st

def inicio():
    time.sleep((0.5))
    fol1,fol2,fol3=st.columns(3)
    with fol1:
        st.success('Bienvenida Lissvia')
    with fol2:
        st.image('b.jpg')
    with fol3:
        st.image('b.jpg')
        
        
    # ---------------------------------------------------------------------------- #
    #                                    botones                                   #
    # ---------------------------------------------------------------------------- #
    col1,col2,col3,col4,col5,col6,col7,col8=st.columns(8)
    with col1:
        general=st.button('General')
    with col2:
        portada_boton=st.button('Portada')
    with col3:
        resumen_boton=st.button('Resumen')
    with col4:
        st.button('Marco teórico')
    with col5:
        st.button('Metodología')
    with col6:
        st.button('Resultados',disabled=True)
    with col7:
        st.button('Conclusiones',disabled=True)
    with col8:
        st.button('Discusión',disabled=True)
        
    # ---------------------------------------------------------------------------- #
    #                                    portada                                   #
    # ---------------------------------------------------------------------------- #
    if portada_boton==True:    
        with st.expander('Inicio', expanded=True):
            col1,col2=st.columns(2)
            with col1:
                global titulo
                titulo=st.text_area('Título de tesis','Título de tesis')
                global autor_principal
                autor_principal=st.text_input('Autor principal','Autor')
                autor_secundario=st.text_input('Autor secundario')
            with col2:
                st.info('Vista previa')
                
    elif general==True:
        col1,col2=st.columns(2)
        with col1:
            st.subheader('Información')
        with col2:
                st.info('Vista previa')
        with col1:
                st.subheader('Título')
                st.markdown(titulo)
                st.subheader('Autor principal')
                st.markdown(autor_principal)
        