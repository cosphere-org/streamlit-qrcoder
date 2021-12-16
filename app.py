from io import BytesIO
import re

import streamlit as st
import qrcode


st.set_page_config(page_title="Generator kodów QR", layout='wide')
st.title('Generator kodów QR')
params = st.experimental_get_query_params()

default_url = None
if 'url' in params:
    default_url = params["url"][0]


if default_url:
    url = st.text_input("Adres do kodu QR", value=default_url)

else:
    url = st.text_input("Adres do kodu QR")

render = st.button("Generuj")

if (render and url) or default_url:
    st.write(f'Kod QR dla adresu: {url}')
    img = qrcode.make(url)

    stream = BytesIO()
    img.save(stream, format="png")
    st.image(stream)

    # filename
    url = url.strip()
    url = re.sub(r'/$', '', url)
    filename = url.split('/')[-1].replace('-', '_')
    filename = f'kod_qr__{filename}.png'
    stream.seek(0)
    # download button
    st.download_button(
        "Pobierz kod QR",
        stream,
        file_name=filename,
        mime="image/png")
