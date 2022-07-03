from click import option
import streamlit as st
import pandas as pd

st.title("Marketing Data")
df = pd.read_excel("tes_data.xlsx")
df['No'][-1]= df['No'].max()+1

st.header("Data Closing")
st.write(df)
save_data = st.button("Simpan")

nama_klien = 'Nama Klien'

st.sidebar.header("Pilihan")
option_form = st.sidebar.form(key = 'form1', clear_on_submit = True)
add_no = df['No'][-1]= df['No'].max()+1
add_date = option_form.date_input("Tanggal")
kategori = option_form.selectbox("Kategori" , ["Canvashing", "SPH", "Closing"], index=2)
user_name = option_form.selectbox("Nama Marketing", ["Ahmad Saripudin", "Anastasia Anindya Putri", "Budi Triwibowo", "Chelsi Luisyena Nepa","Derby Moammer Khadafy", 
"Dina Margaretha Simatupang", "Dwi Ferry Septianus", "Edo Permana", "Ferry Agusdiansyah", "Hadi Setiawan", "Indira Oktavia", "Meli Kartika Sari", 
"Novis Terisman Zebua", "Teguh Suyono", "Rizka Riani Amelita", "Yuli Sektiyani"], index=2)
user_client = option_form.text_input(label=f"{nama_klien}" , value = 'Jangan Singkatan')
user_branch = option_form.selectbox("Cabang Pelaksana", ["Aceh", "Bali", "Balikpapan", "Bandung","Banjarmasin", "Batam", "Cilacap",
"DKI", "Jatibening", "Kendari", "Kupang", "Lombok", "Makassar", "Medan", "Padang", "Palembang", "Pangkal Pinang", "Pekanbaru", 
"Samarinda", "Semarang","Serpong", "Surabaya", "Tanjung Selor", "Tegal", "Yogyakarta"], index=2)
add_data = option_form.form_submit_button()
if add_data:
    new_data = {"No" : add_no, "Tanggal" : add_date, "Kategori" : kategori, "Nama Marketing" : user_name, "Nama Klien" : user_client, "Cabang Pelaksana" : user_branch}
    df = df.append(new_data, ignore_index = True)
    df.to_excel("tes_data.xlsx", index = False)
