import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
from datetime import date

def show_home():
    # Sidebar
    with st.sidebar:
        selected = option_menu("Farm Flow",
                               ["Beranda", "Profil", "Jenis Kelinci", "Siklus Akuntansi", "Laporan Keuangan", "Tambah Transaksi"],
                                default_index=0
        )

    if selected == "Beranda":
        st.title("Beranda")
        st.subheader("Selamat Datang di Aplikasi Farm Flow")
        st.image("https://asset.kompas.com/crops/NLWjVDejksnADFEqKYshuqOyi7I=/0x0:1000x667/750x500/data/photo/2023/01/21/63cb51180cb07.jpg")

    with st.sidebar:
        if selected == "Profil":
            with st.expander("Tentang"):
                sub_menu_profil = st.radio("Pilih opsi:", ["Alamat", "Kontak", "Sejarah"])


    # Konten utama
    
    # --- Di bawah ini letakkan konten berdasarkan `selected` dan `sub_menu` seperti sebelumnya ---
    if selected == "Profil":
        if sub_menu_profil == "Alamat":
            st.subheader("ALAMAT")
            st.write("Karanglo, Barukan, Kecamatan Tengaran, Kabupaten Semarang, Jawa Tengah 50775")
            
            st.title("Lokasi Peternakan AAN Rabbits")

# Contoh data lokasi (latitude & longitude)
            data = pd.DataFrame({
                'latitude': [-7.355749722417219],
                'longitude': [110.54534101012754]
            })

            st.map(data)


        elif sub_menu_profil == "Kontak":
            st.subheader("KONTAK")
            st.write("085700182476 (Pak Aan)")
        elif sub_menu_profil == "Sejarah":
            st.subheader("Sejarah Peternakan AAN Rabbits")
            st.write("Peternakan Aan Rabbit didirikan oleh Bapak Aan sepuluh tahun yang lalu di Semarang. Berawal dari hobi memelihara kelinci, usaha ini tumbuh menjadi sebuah peternakan yang semakin dikenal masyarakat. Dengan komitmen dan kerja keras, peternakan ini berkembang pesat dari skala rumahan menjadi usaha yang lebih besar. Kini, Aan Rabbit dikenal sebagai salah satu peternakan kelinci terbesar di Semarang. Dengan jumlah kelinci yang terus bertambah dan pelayanan yang terus ditingkatkan, peternakan ini menjadi pilihan utama bagi para pecinta kelinci maupun konsumen dari berbagai kalangan. Reputasi yang dibangun selama satu dekade menjadi bukti keseriusan Bapak Aan dalam mengembangkan usahanya")
   # Sidebar submenu Kelinci
    with st.sidebar:
        if selected == "Jenis Kelinci":
            with st.expander("Kelinci"):
                sub_menu_jenis_kelinci = st.radio("Pilih opsi:", ["Jenis Kelinci", "Kalkulator Harga Kelinci"])


# input data berdasarkan submenu Kelinci
    if selected == "Jenis Kelinci":
        if sub_menu_jenis_kelinci == "Jenis Kelinci":
            st.title("Daftar Jenis Kelinci dan Harganya")

# Data kelinci: nama, harga, dan link gambar (gunakan URL gambar)
            data_kelinci = [
                {
                    "nama": "Kelinci Hyla",
                    "harga": 500000.00,
                    "gambar": "https://kuttabdigital.com/wp-content/uploads/2025/02/f15b22b2a5cc50ea035407852a1a730c-700x400.jpg"
                },
                {
                    "nama": "Kelinci Hycole",
                    "harga": 400000.00,
                    "gambar": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5JemTqL5VBmr_cUzMyXpG64mej5gjFrZE2MxCb12_p1AUd0bA6_mHwwQ39XUKUPvOFX4RPsohyphenhyphenJNalB_M0nfNg9PMf9DFeNy-r25YOY17OlTA-u6F4w7gRVVi_1komYZ9CDDKOPhZ7knj/s1600/kelinci-hycole.jpg"
                },
                {
                    "nama": "Kelinci New Zealand",
                    "harga": 350000.00,
                    "gambar": "https://t-2.tstatic.net/jakarta/foto/bank/images/kelinci-new-zealand-1.jpg"
                },
                {
                    "nama": "Kelinci New Zealand Broken Blue",
                    "harga": 1500000.00,
                    "gambar": "https://trubus.id/wp-content/uploads/2021/02/Trubus-Edisi-615-Februari-2021-Highrest-108-2-300x222.jpg"
                },
                {
                    "nama" : "Kelinci New Zealand Blue",
                    "harga" : 1500000.00,
                    "gambar" : "https://images.tokopedia.net/img/cache/500-square/VqbcmM/2022/12/8/276b70fd-ea05-40df-bcbd-28bc724591fa.jpg"
                },
                {
                    "nama" : "Kelinci New Zealand White",
                    "harga" : 350000.00,
                    "gambar" : "https://kemuning.co.id/wp-content/uploads/2023/06/bunny-breed-guide-new-zealand-white-rabbit-1030x929.jpg"
                },
                {
                    "nama": "Kelinci New Zealand Red",
                    "harga": 1500000.00,
                    "gambar": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQosRtw9CnLPUKUDJHDpDUHUFZyWeqPEowR3w&s"
                },
                {
                    "nama": "Kelinci New Zealand Broken Red",
                    "harga": 1500000.00,
                    "gambar": "https://images.tokopedia.net/img/cache/500-square/product-1/2020/5/8/7753971/7753971_3867da08-2d58-46d3-8e13-2c30da3e0da9_720_720.jpg"
                },
                {
                    "nama": "Kelinci Rex",
                    "harga": 325000.00,
                    "gambar": "https://images.tokopedia.net/img/cache/500-square/product-1/2019/10/14/18832197/18832197_4ec1535a-a90a-4015-a107-230a05d89a1f_2048_1536.jpg"
                },
                {
                    "nama": "Kelinci Fuzzy Lop",
                    "harga": 400000.00,
                    "gambar": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhbDwAZUeEN6t-RmbZzTqYc3H4P7TW3c32gVx6L236eJ4wyfC8MkOcQZMhX3_-SqAJ6iNaw58evxEMeSJhiyO0j0t6dPcy1zISGwzi1bzMB7FVa4fmuI1NJRKAENWglwJljztjEKHMtBys/s1600/american+fuzzy+lop.jpg"
                },
                {
                    "nama": "Kelinci Dutch",
                    "harga": 400000.00,
                    "gambar": "https://starfarm.co.id/wp-content/uploads/2020/03/cara-merawat-kelinci-dutch-star-farm.jpg"
                },
                {
                    "nama": "Kelinci Holland Lop",
                    "harga": 600000.00,
                    "gambar": "https://images.tokopedia.net/img/cache/700/VqbcmM/2021/4/15/63cefe53-94d6-4ed0-995e-67b77865e4ed.jpg"
                },
                {
                    "nama": "Kelinci Australian",
                    "harga": 225000.00,
                    "gambar": "https://img.orbitindonesia.com/202312280531392933245498.jpg"
                },
                {
                    "nama": "Kelinci Anggora",
                    "harga": 375000.00,
                    "gambar": "https://assets.pikiran-rakyat.com/crop/0x0:0x0/720x0/webp/photo/2024/07/10/1964977304.jpg"
                },
            ]

# Tampilkan "tabel" dengan gambar
            for kelinci in data_kelinci:
                kolom1, kolom2 = st.columns([1, 3])
    
                with kolom1:
                    st.image(kelinci["gambar"], width=100)

                with kolom2:
                    st.markdown(f"*{kelinci['nama']}*")
                    st.markdown(f"Harga: Rp {kelinci['harga']:,}")

                st.markdown("---")

        elif sub_menu_jenis_kelinci == "Kalkulator Harga Kelinci":
            st.title("🐇 Kalkulator Harga Kelinci 🐇")

# Daftar jenis kelinci dan harga per ekor
            jenis_kelinci = {
                "Hyla" : 500000.00,
                "Hycole" : 400000.00,
                "New zealand " : 350000.00,
                "New zealand broken blue" :1500000.00,
                "New zealand blue" : 1500000.00,
                "New zealand white" : 350000.00 ,
                "New zealand red" : 1500000.00,
                "New zealand broken red" : 1500000.00,
                "Rex" : 325000.00 ,
                "Fuzzy lop": 400000.00,
                "Dutch" : 400000.00,
                "Holland lop": 600000.00,
                "Australian rabbit" : 225000.00,
                "Anggora" : 375000.00

            }

# Buat daftar pilihan dropdown: "Jenis Kelinci (Rp harga)"
            pilihan_jenis = [f"{jenis} (Rp {harga:,})" for jenis, harga in jenis_kelinci.items()]

# Selectbox untuk jenis kelinci
            jenis_dipilih = st.selectbox("Pilih jenis kelinci", pilihan_jenis)

# Ambil nama dan harga dari pilihan
            nama_kelinci = jenis_dipilih.split(" (")[0]
            harga_kelinci = jenis_kelinci[nama_kelinci]

# Selectbox untuk jumlah
            jumlah_kelinci = st.number_input("Masukkan jumlah kelinci", min_value=0, value=1)

# Hitung total
            total_harga = jumlah_kelinci * harga_kelinci

# Tampilkan hasil
            st.markdown("---")
            st.subheader("🧾 Ringkasan Harga")
            st.write(f"Jenis kelinci: *{nama_kelinci}*")
            st.write(f"Harga per ekor: *Rp {harga_kelinci:,.0f}*")
            st.write(f"Jumlah: *{jumlah_kelinci} ekor*")
            st.success(f"Total harga: Rp {total_harga:,.0f}")

# Sidebar submenu Siklus
    with st.sidebar:
        if selected == "Siklus Akuntansi":
            with st.expander("Siklus") :
                sub_menu_siklus = st.radio("Pilih opsi:", ["Neraca Saldo Periode Sebelumnya", "Jurnal Umum", "Buku Besar", "Neraca Saldo", "Jurnal Penyesuaian", "Jurnal Penutup", "Neraca Saldo Setelah Penutupan", "Jurnal Pembalik"])

# input data berdasarkan submenu Siklus
    if selected == "Siklus Akuntansi":
        if sub_menu_siklus == "Neraca Saldo Periode Sebelumnya":
            st.subheader("NERACA SALDO PERIODE SEBELUMNYA")
            st.markdown("Periode 31 Maret 2025")

            data = {
                    "Nama Akun" : [
                    "Kas", "Persediaan", "Perlengkapan", "Persediaan Kelinci",
                    "Utang Bank", "Modal",
                    "JUMLAH"
                    ],
                    "Debit (Rp)" : [
                    21100000.00, 13297000.00, 13155000.00, 184725000.00,
                    None, None,
                    232277000.00
                    ],
                    "Kredit (Rp)" : [
                        None, None, None, None,
                        70000000.00, 162277000.00,
                        232277000.00
                    ]
                }

            df = pd.DataFrame(data)

        # Format tampilan agar mirip tabel akuntansi
            st.dataframe(df.style.format({
                    "Debit (Rp)": "Rp {:,.2f}",
                    "Kredit (Rp)": "Rp {:,.2f}"
                }))

        elif sub_menu_siklus == "Jurnal Umum":
            st.subheader("JURNAL UMUM")
            st.markdown("Periode 30 April 2025")
            data = {
                "Tanggal" : [
                    "4/04/2025", None,
                    "4/05/2025", None,
                    "4/06/2025", None,
                    "4/07/2025", None,
                    "4/08/2025", None,
                    "4/09/2025", None, None,
                    "4/10/2025", None,
                    "4/12/2025", None,
                    "4/13/2025", None,
                    "4/15/2025", None,
                    "4/16/2025", None,
                    "4/18/2025", None,
                    "4/19/2025", None,
                    "4/20/2025", None,
                    "4/25/2025", None,
                    None
                ],
                "Keterangan" : [
                    "Persediaan Kelinci", "    Kas",
                    "Kas", "    Penjualan",
                    "Beban Pemeliharaan", "    Kas",
                    "Kas", "    Penjualan",
                    "Kas", "    Penjualan",
                    "Utang Bank", "Beban Bunga", "    Kas",
                    "Perlengkapan", "    Kas",
                    "Kas", "    Penjualan",
                    "Beban Pengiriman", "    Kas",
                    "Beban Listrik", "    Kas",
                    "Beban Air", "    Kas",
                    "Persediaan Kelinci", "    Kas",
                    "Kas", "    Penjualan",
                    "Persediaan", "    Kas",
                    "Beban Gaji", "    Kas",
                    "JUMLAH"
                ],
                "Debit (Rp)" : [
                    2000000.00, None,
                    9000000.00, None,
                    350000.00, None,
                    7500000.00, None,
                    5600000.00, None,
                    1000000.00, 100000, None,
                    300000.00, None,
                    12000000.00, None,
                    150000.00, None,
                    250000.00, None,
                    100000.00, None,
                    1500000.00, None,
                    10000000.00, None,
                    600000.00, None,
                    1000000.00, None,
                    51450000.00
                ],
                "Kredit (Rp)" : [
                    None, 2000000.00,
                    None, 9000000.00,
                    None, 350000.00,
                    None, 7500000.00,
                    None, 5600000.00,
                    None, None, 1100000.00,
                    None, 300000.00,
                    None, 12000000.00,
                    None, 150000.00,
                    None, 250000.00,
                    None, 100000.00,
                    None, 1500000.00,
                    None, 10000000.00,
                    None, 600000.00,
                    None, 1000000.00,
                    51450000.00
                ]
            }

            df = pd.DataFrame(data)

            # Format tampilan agar mirip tabel akuntansi
            st.dataframe(df.style.format({
                "Debit (Rp)": "Rp {:,.2f}",
                "Kredit (Rp)": "Rp {:,.2f}"
                }))


        elif sub_menu_siklus == "Buku Besar":
            st.subheader("BUKU BESAR")
            st.markdown("**Periode 30 April 2025**")

            # Data Kas
            data_kas = {
                "Tanggal": ["1-Apr", "1-Apr", "2-Apr", "3-Apr", "5-Apr", "7-Apr", "8-Apr", "10-Apr", "12-Apr", "13-Apr", "15-Apr", "16-Apr", "18-Apr", "19-Apr", "20-Apr", "25-Apr", "", ""],
                "Debit (Rp)": [21100000.00, None, 9000000.00, None, 7500000.00, 5600000.00, None, None, 12000000.00, None, None, None, None, 10000000.00, None, None, 65200000.00, 57800000.00],
                "Kredit (Rp)": [None, 2000000.00, None, 350000.00, None, None, 1100000.00, 300000.00, None, 150000.00, 250000.00, 100000.00, 1500000.00, None, 600000.00, 1000000.00, 7350000.00, None]
                }
            
            df_kas = pd.DataFrame(data_kas)
            # Menampilkan judul
            st.subheader("Kas")
            st.dataframe(df_kas.style.format({
                 "Debit (Rp)": "Rp {:,.2f}",
                 "Kredit (Rp)": "Rp {:,.2f}"
                 }))
            
            # Data Perlengkapan
            data_persediaan = {
                "Tanggal": ["1-Apr", "20-Apr", ""],
                "Debit (Rp)": [13297000.00, 600000.00, 13897000.00],
                "Kredit (Rp)": [0, 0, 0]
                }
            df_persediaan = pd.DataFrame(data_persediaan)
            # Menampilkan judul
            st.subheader("Persediaan")
            st.dataframe(df_persediaan.style.format({
                 "Debit (Rp)": "Rp {:,.2f}",
                 "Kredit (Rp)": "Rp {:,.2f}"
                 }))

            # Data Perlengkapan
            data_perlengkapan = {
                "Tanggal": ["1-Apr", "10-Apr", ""],
                "Debit (Rp)": [13155000.00, 300000.00, 13455000.00],
                "Kredit (Rp)": [0, 0, 0]
                }
            df_perlengkapan = pd.DataFrame(data_perlengkapan)
            # Menampilkan judul
            st.subheader("Perlengkapan")
            st.dataframe(df_perlengkapan.style.format({
                 "Debit (Rp)": "Rp {:,.2f}",
                 "Kredit (Rp)": "Rp {:,.2f}"
                 }))
        
            # Data Persediaan Kelinci
            data_persediaan_kelinci = {
                "Tanggal": ["1-Apr", "1-Apr", "18-Apr", ""],
                "Debit (Rp)": [184725000.00, 2000000.00, 1500000.00, 188225000.00],
                "Kredit (Rp)": [0, 0, 0, 0]
                }
            df_persediaan_kelinci = pd.DataFrame(data_persediaan_kelinci)
            # Menampilkan judul
            st.subheader("Persediaan Kelinci")
            st.dataframe(df_persediaan_kelinci.style.format({
                 "Debit (Rp)": "Rp {:,.2f}",
                 "Kredit (Rp)": "Rp {:,.2f}"
                 }))
            
            # Data Utang Bank
            data_utang_bank = {
                "Tanggal": ["1-Apr", "8-Apr", ""],
                "Debit (Rp)": [None, 1000000.00, None],
                "Kredit (Rp)": [70000000.00, None, 69000000.00]
                }
            df_utang_bank = pd.DataFrame(data_utang_bank)
            # Menampilkan judul
            st.subheader("Utang Bank")
            st.dataframe(df_utang_bank.style.format({
                 "Debit (Rp)": "Rp {:,.2f}",
                 "Kredit (Rp)": "Rp {:,.2f}"
                 }))
            
            # Data Utang Gaji
            data_utang_gaji = {
                "Tanggal": ["30-Apr"],
                "Debit (Rp)": [0],
                "Kredit (Rp)": [193548.00]
                }
            df_utang_gaji = pd.DataFrame(data_utang_gaji)
            # Menampilkan judul
            st.subheader("Utang Gaji")
            st.dataframe(df_utang_gaji.style.format({
                 "Debit (Rp)": "Rp {:,.2f}",
                 "Kredit (Rp)": "Rp {:,.2f}"
                 }))
            
            # Data Modal
            data_modal = {
                "Tanggal": ["1-Apr"],
                "Debit (Rp)": [0],
                "Kredit (Rp)": [162277000.00]
                }
            df_modal = pd.DataFrame(data_modal)
            # Menampilkan judul
            st.subheader("Modal")
            st.dataframe(df_modal.style.format({
                 "Debit (Rp)": "Rp {:,.2f}",
                 "Kredit (Rp)": "Rp {:,.2f}"
                 }))
            
            # Data Penjualan
            data_penjualan = {
                "Tanggal": ["2-Apr", "5-Apr", "7-Apr", "12-Apr", "19-Apr", "JUMLAH"],
                "Debit (Rp)": [0, 0, 0, 0, 0, 0],
                "Kredit (Rp)": [9000000.00, 7500000.00, 5600000.00, 12000000.00, 10000000.00, 44100000.00]
                }
            df_penjualan = pd.DataFrame(data_penjualan)
            # Menampilkan judul
            st.subheader("Penjualan")
            st.dataframe(df_penjualan.style.format({
                 "Debit (Rp)": "Rp {:,.2f}",
                 "Kredit (Rp)": "Rp {:,.2f}"
                 }))
            
            # Data Beban Pemeliharaan
            data_beban_pemeliharaan = {
                "Tanggal": ["3-Apr"],
                "Debit (Rp)": [350000.00],
                "Kredit (Rp)": [0]
                }
            df_beban_pemeliharaan = pd.DataFrame(data_beban_pemeliharaan)
            # Menampilkan judul
            st.subheader("Beban Pemeliharaan")
            st.dataframe(df_beban_pemeliharaan.style.format({
                 "Debit (Rp)": "Rp {:,.2f}",
                 "Kredit (Rp)": "Rp {:,.2f}"
                 }))
            
            # Data Beban Bunga
            data_beban_bunga = {
                "Tanggal": ["8-Apr"],
                "Debit (Rp)": [100000.00],
                "Kredit (Rp)": [0]
                }
            df_beban_bunga = pd.DataFrame(data_beban_bunga)
            # Menampilkan judul
            st.subheader("Beban Bunga")
            st.dataframe(df_beban_bunga.style.format({
                 "Debit (Rp)": "Rp {:,.2f}",
                 "Kredit (Rp)": "Rp {:,.2f}"
                 }))
            
            # Data Beban Pengiriman
            data_beban_pengiriman = {
                "Tanggal": ["13-Apr"],
                "Debit (Rp)": [150000.00],
                "Kredit (Rp)": [0]
                }
            df_beban_pengiriman = pd.DataFrame(data_beban_pengiriman)
            # Menampilkan judul
            st.subheader("Beban Pengiriman")
            st.dataframe(df_beban_pengiriman.style.format({
                 "Debit (Rp)": "Rp {:,.2f}",
                 "Kredit (Rp)": "Rp {:,.2f}"
                 }))
            
            # Data Beban Listrik
            data_beban_listrik = {
                "Tanggal": ["15-Apr"],
                "Debit (Rp)": [250000.00],
                "Kredit (Rp)": [0]
                }
            df_beban_listrik = pd.DataFrame(data_beban_listrik)
            # Menampilkan judul
            st.subheader("Beban Listrik")
            st.dataframe(df_beban_listrik.style.format({
                 "Debit (Rp)": "Rp {:,.2f}",
                 "Kredit (Rp)": "Rp {:,.2f}"
                 }))
            
            # Data Beban Air
            data_beban_air = {
                "Tanggal": ["16-Apr"],
                "Debit (Rp)": [100000.00],
                "Kredit (Rp)": [0]
                }
            df_beban_air = pd.DataFrame(data_beban_air)
            # Menampilkan judul
            st.subheader("Beban Air")
            st.dataframe(df_beban_air.style.format({
                 "Debit (Rp)": "Rp {:,.2f}",
                 "Kredit (Rp)": "Rp {:,.2f}"
                 }))
            
            # Data Beban Gaji
            data_beban_gaji = {
                "Tanggal": ["25-Apr"],
                "Debit (Rp)": [1000000.00],
                "Kredit (Rp)": [0]
                }
            df_beban_gaji = pd.DataFrame(data_beban_gaji)
            # Menampilkan judul
            st.subheader("Beban Gaji")
            st.dataframe(df_beban_gaji.style.format({
                 "Debit (Rp)": "Rp {:,.2f}",
                 "Kredit (Rp)": "Rp {:,.2f}"
                 }))

        elif sub_menu_siklus == "Neraca Saldo":
            st.subheader("NERACA SALDO")
            st.markdown("**Periode 30 April 2025**")

            data = {
                "Keterangan" : [
                    "Kas", "Persediaan", "Perlengkapan", "Persediaan Kelinci",
                    "Utang Bank", "Modal", "Penjualan",
                    "Beban Pemeliharaan", "Beban Bunga", "Beban Pengiriman", "Beban Listrik", "Beban Air", "Beban Gaji",
                    "Jumlah"
                ],
                "Debit (Rp)" : [
                    57850000.00, 13897000.00, 13455000.00, 188225000.00,
                    None, None, None,
                    350000.00, 100000.00, 150000.00, 250000.00, 100000.00, 1000000.00, 275377000.00
                ],
                "Kredit (Rp)" : [
                    None, None, None, None,
                    69000000.00, 162277000.00, 44100000.00,
                    None, None, None, None, None, None, 275377000
                ]
            }

            df = pd.DataFrame(data)

        # Format tampilan agar mirip tabel akuntansi
            st.dataframe(df.style.format({
                "Debit (Rp)": "Rp {:,.2f}",
                "Kredit (Rp)": "Rp {:,.2f}"
            }))

    
        elif sub_menu_siklus == "Jurnal Penyesuaian":
            st.subheader("JURNAL PENYESUAIAN")
            kontak = st.write("**Periode 30 April 2025**")

            data = {
                "Keterangan" : [
                    "Beban Gaji", "     Utang Gaji"
                ],
                "Debit (Rp)" : [
                    193548.00, None
                ],
                "Kredit (Rp)" : [
                    None, 193548.00
                ]
            }

            df = pd.DataFrame(data)

        # Format tampilan agar mirip tabel akuntansi
            st.dataframe(df.style.format({
                "Debit (Rp)": "Rp {:,.2f}",
                "Kredit (Rp)": "Rp {:,.2f}"
            }))

        elif sub_menu_siklus == "Jurnal Penutup":
            st.subheader("JURNAL PENUTUP")
            st.markdown("**Periode 30 April 2025**")

            data = {
                "Tanggal": [
                    "4/30/2025", "", 
                    "4/30/2025", "", "", "", "", "", "",
                    "4/30/2025", "",
                    ""
                ],
                "Keterangan": [
                    "Penjualan", "Ikhtisar laba rugi",
                    "Ikhtisar laba rugi", "  Beban Pemeliharaan", "  Beban Bunga", "  Beban Pengiriman", "  Beban Listrik", "  Beban Air", "  Beban Gaji",
                    "Ikhtisar laba rugi", "  Modal",
                    "TOTAL"
                ],
                "Debit (Rp)": [
                    44100000.00, None,
                    2143548.00, None, None, None, None, None, None,
                    None, None,
                    46243548.00
                ],
                "Kredit (Rp)": [
                    None, 44100000.00,
                    None, 350000.00, 100000.00, 150000.00, 250000.00, 100000.00, 1193548.00,
                    None, None,
                    46243548.00
                ]
            }

            df = pd.DataFrame(data)

        # Format tampilan agar mirip tabel akuntansi
            st.dataframe(df.style.format({
                "Debit (Rp)": "Rp {:,.2f}",
                "Kredit (Rp)": "Rp {:,.2f}"
            }))

        elif sub_menu_siklus == "Neraca Saldo Setelah Penutupan":
            st.subheader("NERACA SALDO SETELAH PENUTUPAN")
            st.markdown("**Periode 30 April 2025**")

        # Data Neraca Saldo Setelah Penutupan
            data = {
                "Keterangan": ["Kas", "Persediaan", "Perlengkapan", "Persediaan Kelinci", "Utang Gaji", "Utang Bank", "Modal"],
                "Debit (Rp)": [57850000, 13897000, 13455000, 188225000, None, None, None],
                "Kredit (Rp)": [None, None, None, None, 193548, 69000000, 204233452]
            }

        # Buat DataFrame
            df = pd.DataFrame(data)

        # Hitung total debit dan kredit
            total_debit = df["Debit (Rp)"].sum()
            total_kredit = df["Kredit (Rp)"].sum()

        # Tambahkan baris total
            total_row = pd.DataFrame({
                "Keterangan": ["JUMLAH"],
                "Debit (Rp)": [total_debit],
                "Kredit (Rp)": [total_kredit]
            })

            df = pd.concat([df, total_row], ignore_index=True)

        # Tampilkan DataFrame di Streamlit
            st.dataframe(df.style.format({"Debit (Rp)": "Rp {:,.2f}", "Kredit (Rp)": "Rp {:,.2f}"}))

    
        elif sub_menu_siklus == "Jurnal Pembalik":
            st.subheader("JURNAL PEMBALIK")
            st.markdown("Per 1 Mei 2025")

            data = {
                "Keterangan" : [
                    "Utang Gaji", "     Beban Gaji"
                ],
                "Debit (Rp)" : [
                    193548.00, None
                ],
                "Kredit (Rp)" : [
                    None, 193548.00
                ]
            }

            df = pd.DataFrame(data)
            
            # Format tampilan agar mirip tabel akuntansi
            st.dataframe(df.style.format({
                "Debit (Rp)": "Rp {:,.2f}",
                "Kredit (Rp)": "Rp {:,.2f}"
            }))


# Sidebar submenu Lapkeu
    with st.sidebar:
        if selected == "Laporan Keuangan":
            with st.expander("Lapkeu") :
                sub_menu_lapkeu = st.radio("Pilih opsi:", ["Laporan Laba Rugi", "Laporan Perubahan Modal", "Laporan Posisi Keuangan"])

# input data berdasarkan submenu Siklus
    if selected == "Laporan Keuangan":
        if sub_menu_lapkeu == "Laporan Laba Rugi":
                st.subheader("LAPORAN LABA RUGI")
                st.markdown("**Untuk Periode yang Berakhir 30 April 2025**")

                data = {
                        "None" : [
                        "Pendapatan", "    Penjualan", "Beban", "    Beban Pemeliharaan", "    Beban Bunga", "    Beban Pengiriman",
                        "    Beban Listrik", "    Beban Air", "    Beban Gaji", "Total Beban", 
                        "TOTAL"
                    ],
                    "(Rp)" : [
                        None, 44100000.00, None, 350000.00, 100000.00, 150000.00,
                        250000.00, 100000.00, 1193548.00, 2143548.00,
                        41956452.00
                    ] 
                }

                df = pd.DataFrame(data)

                # Format tampilan agar mirip tabel akuntansi
                st.dataframe(df.style.format({
                    "(Rp)": "Rp {:,.2f}"
                }))


    #isi lap perubahan modal
        elif sub_menu_lapkeu == "Laporan Perubahan Modal":
                st.subheader("LAPORAN PERUBAHAN MODAL")
                st.markdown("**Periode yang berakhir 30 April 2025**")

                data_perubahan_modal = [
                    ("Modal Awal 31 Maret", 162_277_000),
                    ("Laba Bersih", 41_956_452),
                    ("Penambahan Modal", 41_956_452),
                    ("Modal Akhir 30 April 2025", 204_233_452),
                ]

                for keterangan, jumlah in data_perubahan_modal:
                    col1, col2 = st.columns([4, 2])
                    with col1:
                        if "Akhir" in keterangan:
                            st.markdown(f"**{keterangan}**")
                        else:
                            st.write(keterangan)
                    with col2:
                        if "Akhir" in keterangan:
                            st.markdown(f"**Rp {jumlah:,.2f}**")
                        else:
                            st.write(f"Rp {jumlah:,.2f}")

        elif sub_menu_lapkeu == "Laporan Posisi Keuangan":
                st.title("LAPORAN POSISI KEUANGAN")
                st.subheader("Periode 30 April 2025")

                data = {
                    "Aset" : [
                        "Kas", 
                        "Persediaan", 
                        "Perlengkapan",
                        "Jumlah Aset Lancar",
                        "Aset Biologis",
                        "Jumlah Aset Tidak Lancar",
                        "TOTAL ASET"
                    ],
                    "Jumlah Aset (Rp)" : [
                        57850000.00, 
                        13897000.00, 
                        13455000.00, 
                        85202000.00, 
                        188225000.00, 
                        188225000.00, 
                        273427000.00
                    ],
                    "Liabilitas & Ekuitas" : [
                        "Utang Gaji",
                        "Utang Bank",
                        "TOTAL LIABILITAS",
                        "-",
                        "Modal",
                        "TOTAL EKUITAS",
                        "TOTAL LIABILITAS & EKUITAS"
                    ],
                    "Jumlah Liabilitas & Ekuitas (Rp)" : [
                        193548.00, 
                        69000000.00, 
                        69193548.00, 
                        None, 
                        204233452.00, 
                        204233452.00, 
                        273427000.00
                    ]
                }

                df = pd.DataFrame(data)

                # Format tampilan agar mirip tabel akuntansi
                st.dataframe(df.style.format({
                    "Debit (Rp)": "Rp {:,.2f}",
                    "Kredit (Rp)": "Rp {:,.2f}"
                }))

# Sidebar submenu tambah transaksi
    with st.sidebar:
        if selected == "Tambah Transaksi":
            with st.expander("Transaksi") :
                sub_menu_transaksi = st.radio("Pilih opsi:", ["Jurnal", "Neraca Saldo", "Laporan Keuangan"])
        
    if selected == "Tambah Transaksi":
        if sub_menu_transaksi == "Jurnal":
                if 'jurnal_umum' not in st.session_state:
                    st.session_state['jurnal_umum'] = pd.DataFrame(columns=["Tanggal", "Akun", "Debit", "Kredit"])

                st.subheader("JURNAL")
                # Form Tambah Transaksi
                with st.form("form_transaksi"):
                    tanggal = st.date_input("Tanggal Transaksi")
                    akun = st.selectbox("Akun", ["Kas","Persediaan", "Perlengkapan", "Persediaan Kelinci", "Utang Bank", "Utang Gaji", "Modal", "Penjualan", "Beban Pemeliharaan", "Beban Bunga", "Beban Pengiriman",
                                                 "Beban Listrik", "Beban Air", "Beban Gaji"])
                    debit = st.number_input("Debit (Rp)", min_value=0.0, step=1000.0, format="%.2f")
                    kredit = st.number_input("Kredit (Rp)", min_value=0.0, step=1000.0, format="%.2f")
                    submit = st.form_submit_button("Tambah")

                if submit:
                    st.session_state['jurnal_umum'] = pd.concat([
                        st.session_state['jurnal_umum'],
                        pd.DataFrame([{
                            "Tanggal" : tanggal,
                            "Akun" : akun,
                            "Debit" : debit,
                            "Kredit" : kredit
                        }])
                    ], ignore_index=True)
                    st.success("Transaksi berhasil ditambahkan!")
                             
                st.subheader("BUKU BESAR")
                akun_terpilih = st.selectbox("Pilih Akun", st.session_state['jurnal_umum']["Akun"].unique())

                    #Filter berdasarkan akun
                buku_besar = st.session_state['jurnal_umum']
                buku_besar = buku_besar[buku_besar["Akun"] == akun_terpilih]
                st.table(buku_besar)

        if sub_menu_transaksi == "Laporan Keuangan":
                st.title("Laporan Keuangan")
                st.header("LAPORAN LABA RUGI")

    # Pastikan jurnal sudah ada
                if 'jurnal_umum' in st.session_state and not st.session_state['jurnal_umum'].empty:
                    df = st.session_state['jurnal_umum']

        # Klasifikasi akun
                    akun_pendapatan = ["Penjualan"]
                    akun_beban = ["Beban Pemeliharaan", "Beban Bunga", "Beban Pengiriman", "Beban Listrik", "Beban Air", "Beban Gaji"]

                    pendapatan_df = df[df["Akun"].isin(akun_pendapatan)]
                    beban_df = df[df["Akun"].isin(akun_beban)]

                    total_pendapatan = pendapatan_df["Kredit"].sum()  # Pendapatan di kolom Kredit
                    total_beban = beban_df["Debit"].sum()             # Beban di kolom Debit
                    laba_bersih = total_pendapatan - total_beban

        # Tampilkan laporan
                    st.write("### Pendapatan")
                    st.table(pendapatan_df[["Tanggal", "Akun", "Debit", "Kredit"]])
                    st.write(f"**Total Pendapatan:** Rp {total_pendapatan:,.2f}")

                    st.write("### Beban")
                    st.table(beban_df[["Tanggal", "Akun", "Debit", "Kredit"]])
                    st.write(f"**Total Beban:** Rp {total_beban:,.2f}")

                    st.markdown("---")
                    st.write("### **Laba Bersih:**")
                    st.success(f"Rp {laba_bersih:,.2f}")
                else:
                    st.warning("Belum ada data di Jurnal Umum.")

                st.subheader("LAPORAN PERUBAHAN MODAL")
                if 'jurnal_umum' in st.session_state and not st.session_state['jurnal_umum'].empty:
                    df = st.session_state['jurnal_umum']

        # Ambil akun relevan
                    akun_modal_awal = "Modal"
                    akun_tambahan_modal = "Tambahan Modal"
                    akun_prive = "Prive"
                    akun_pendapatan = ["Penjualan"]
                    akun_beban = ["Beban Pemeliharaan", "Beban Bunga", "Beban Pengiriman", "Beban Listrik", "Beban Air", "Beban Gaji"]

        # Modal awal (misal diinput di Kredit)
                    modal_awal = df[df["Akun"] == akun_modal_awal]["Kredit"].sum()

        # Tambahan modal (jika ada akun ini)
                    tambahan_modal = df[df["Akun"] == akun_tambahan_modal]["Kredit"].sum() if akun_tambahan_modal in df["Akun"].values else 0

        # Prive (biasanya di Debit karena mengurangi modal)
                    prive = df[df["Akun"] == akun_prive]["Debit"].sum() if akun_prive in df["Akun"].values else 0

        # Hitung Laba Bersih dari Laba Rugi
                    pendapatan = df[df["Akun"].isin(akun_pendapatan)]["Kredit"].sum()
                    beban = df[df["Akun"].isin(akun_beban)]["Debit"].sum()
                    laba_bersih = pendapatan - beban

        # Modal Akhir
                    modal_akhir = modal_awal + tambahan_modal + laba_bersih - prive

        # Tampilkan
                    st.write(f"**Modal Awal:** Rp {modal_awal:,.2f}")
                    st.write(f"**Tambahan Modal:** Rp {tambahan_modal:,.2f}")
                    st.write(f"**Laba Bersih:** Rp {laba_bersih:,.2f}")
                    st.write(f"**Prive:** Rp {prive:,.2f}")
                    st.markdown("---")
                    st.success(f"**Modal Akhir:** Rp {modal_akhir:,.2f}")
                else:
                    st.warning("Belum ada data di Jurnal Umum.")

                st.header("LAPORAN POSISI KEUANGAN (NERACA)")

                if 'jurnal_umum' in st.session_state and not st.session_state['jurnal_umum'].empty:
                    df = st.session_state['jurnal_umum']

        # Kelompokkan akun-akun
                    akun_aset = ["Kas", "Persediaan", "Perlengkapan", "Persediaan Kelinci"]
                    akun_kewajiban = ["Utang Bank", "Utang Gaji"]
                    akun_modal_awal = "Modal"
                    akun_prive = "Prive"
                    akun_pendapatan = ["Penjualan"]
                    akun_beban = ["Beban Pemeliharaan", "Beban Bunga", "Beban Pengiriman", "Beban Listrik", "Beban Air", "Beban Gaji"]

        # Hitung total aset (dari Debit)
                    total_aset = df[df["Akun"].isin(akun_aset)].groupby("Akun")["Debit"].sum()

        # Hitung total kewajiban (dari Kredit)
                    total_kewajiban = df[df["Akun"].isin(akun_kewajiban)].groupby("Akun")["Kredit"].sum()

        # Hitung Laba Bersih (dari Laba Rugi)
                    pendapatan = df[df["Akun"].isin(akun_pendapatan)]["Kredit"].sum()
                    beban = df[df["Akun"].isin(akun_beban)]["Debit"].sum()
                    laba_bersih = pendapatan - beban

        # Modal Awal
                    modal_awal = df[df["Akun"] == akun_modal_awal]["Kredit"].sum()

        # Prive (pengambilan)
                    prive = df[df["Akun"] == akun_prive]["Debit"].sum() if akun_prive in df["Akun"].values else 0

        # Modal Akhir
                    modal_akhir = modal_awal + laba_bersih - prive

        # === Tampilkan Aset ===
                    st.write("### Aset")
                    st.table(total_aset)
                    st.write(f"**Total Aset**: Rp {total_aset.sum():,.2f}")

        # === Tampilkan Kewajiban ===
                    st.write("### Kewajiban")
                    st.table(total_kewajiban)
                    st.write(f"**Total Kewajiban**: Rp {total_kewajiban.sum():,.2f}")

        # === Tampilkan Ekuitas ===
                    st.write("### Ekuitas")
                    st.write(f"Modal Akhir: Rp {modal_akhir:,.2f}")

        # === Total Kewajiban + Ekuitas ===
                    total_passiva = total_kewajiban.sum() + modal_akhir
                    st.markdown("---")
                    st.success(f"**Total Kewajiban + Ekuitas**: Rp {total_passiva:,.2f}")

        # === Validasi Neraca Seimbang ===
                    if abs(total_aset.sum() - total_passiva) < 1:
                        st.success("Neraca Seimbang")
                    else:
                        st.error("Neraca Tidak Seimbang")
                else:
                        st.warning("Belum ada data di Jurnal Umum.")
                
        if sub_menu_transaksi == "Neraca Saldo":
            st.header("NERACA SALDO")
            st.subheader("Periode 30 April 2025")

            if 'jurnal_umum' in st.session_state and not st.session_state['jurnal_umum'].empty:
                df = st.session_state['jurnal_umum']

    # Group akun, hitung total debit dan kredit
                neraca_saldo = df.groupby("Akun").agg({
                    "Debit": "sum",
                    "Kredit": "sum"
                }).reset_index()

    # Tampilkan tabel
                st.table(neraca_saldo)

    # Validasi
                total_debit = neraca_saldo["Debit"].sum()
                total_kredit = neraca_saldo["Kredit"].sum()

                st.markdown("---")
                st.write(f"**Total Debit:** Rp {total_debit:,.2f}")
                st.write(f"**Total Kredit:** Rp {total_kredit:,.2f}")

                if abs(total_debit - total_kredit) < 1:
                    st.success("Neraca Saldo Seimbang")
                else:
                    st.error("Neraca Saldo Tidak Seimbang")
        else:
            st.warning("Belum ada data di Jurnal Umum.")

    with st.sidebar:
        if st.button("Logout"):
            st.session_state["login_status"] = False
            st.rerun()








