import streamlit as st

def login_page():
    # Aquí incluirías tu lógica de autenticación



# Use la función `st.markdown()` para cargar el archivo CSS en su aplicación de Streamlit


    username = st.text_input('Usuario')
    password = st.text_input('Contraseña', type='password')

    if st.button('Iniciar sesión'):
        # Aquí deberías validar las credenciales y decidir si el login es exitoso o no
        if username == 'jhon' and password == '123':
            # Si el login es exitoso, redirige a la página principal
            st.experimental_set_query_params(page='dashboard')


page = st.experimental_get_query_params().get('page', [''])[0]

if page == 'dashboard':
   from das import dashboard_page
   dashboard_page()
else:
    login_page()