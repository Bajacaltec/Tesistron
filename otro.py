   
con = sqlite3.connect('data.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS B
            (Nombre TEXT,Número INT)""")


col1,col2=st.columns(2)
with col1:
    with st.expander('Identificación'):
        with st.form('Identificación'):
            nombre=st.text_input('Nombre')
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
    
