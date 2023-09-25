import streamlit as st
from das import dashboard_page

def login_page():
    # Aquí incluirías tu lógica de autenticación

    with open("styles.css", "r") as f:
     styles = f.read()

# Use la función `st.markdown()` para cargar el archivo CSS en su aplicación de Streamlit

    st.markdown(styles, unsafe_allow_html=True)

    username = st.text_input('Usuario')
    password = st.text_input('Contraseña', type='password')

    if st.button('Iniciar sesión',styles={
    "color": "red",
    "font-size": "20px",
    "font-family": "Verdana"
}):
        # Aquí deberías validar las credenciales y decidir si el login es exitoso o no
        if username == 'jhon' and password == '123':
            # Si el login es exitoso, redirige a la página principal
            st.experimental_set_query_params(page='dashboard')


page = st.experimental_get_query_params().get('page', [''])[0]

if page == 'dashboard':
    dashboard_page()
else:
    login_page()