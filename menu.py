import streamlit as st

def get_menu():
    page_home = st.Page(
        "pages/main/home.py",
        title="Úvodní stránka",
        icon=":material/home:")

    page_contact = st.Page(
        "pages/main/contact.py",
        title="Kontakt",
        icon=":material/mail:")

    main_pages = [
        page_home,
        page_contact
    ]

    page_01 = st.Page(
        "pages/analysis/01_acute_care_in_psychiatry.py",
        title="Akutní psychiatrická péče",
        icon=":material/mail:")

    analysis_pages = [
        page_01
    ]



    menu = st.navigation({"Informace": main_pages, 'Analýzy': analysis_pages})

    return menu