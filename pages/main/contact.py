import streamlit as st

st.title('Kontaktní informace')
col1, col2 = st.columns(2)

with col1:
    st.info('Luděk Reif', icon=":material/signature:")
    st.info('+420 720 116 008', icon=":material/call:")
    st.info('luipenox@gmail.com', icon=":material/mail:")
    st.info('https://www.linkedin.com/in/luipenox/', icon=":material/link:")

    with col2:
        st.image('assets/images/luipenox.jpg', width=272)