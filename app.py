## TODO optimize requirements.txt to include only libraries we use
## TODO resolve the library importing mess
## TODO see if you can work with "dotlottie" files instead of normal files. "dotlottie" file sizes are less. Or transition to URLs.
## TODO echarts link: https://echarts.streamlit.app https://github.com/andfanilo/streamlit-echarts
## TODO country_a South Africa, Antigua and Barbuda returns error
## TODO categorize indexes
## TODO consolidate all magic strings in the streamlit project into global variables, for better centralization maybe have another constant.py script here too.
## TODO checkout similar page-runtime settings
## TODO save strings in constant, to avoid magic strings


import streamlit as st

st.set_page_config(layout = "wide", page_title = "QG Intelligence", page_icon = "🌐")

from pages import base, patterns, events, experimental, faq, contact


pages = [
    st.Page(page = base.base,                 title = "Base",               icon = "🌐"),
    st.Page(page = patterns.patterns_portal,  title = "Patterns",           icon = "📈"),
    st.Page(page = events.event_frequency,    title = "Events",             icon = "📊"),
    st.Page(page = experimental.experimental, title = "Under Construction", icon = "🚧"),
    st.Page(page = faq.faq,                   title = "FAQ",                icon = "❓"),
    st.Page(page = contact.contact,           title = "Contact",            icon = "📬"),
]


pg = st.navigation(pages)
pg.run()

