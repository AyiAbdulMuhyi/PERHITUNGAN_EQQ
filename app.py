# app.py
import streamlit as st
import math

st.set_page_config(page_title="Kalkulator EOQ", page_icon="📦")
st.title("📦 Aplikasi Perhitungan EOQ (Economic Order Quantity)")

st.markdown("Simulasi sistem persediaan bahan baku untuk menentukan jumlah pemesanan optimal.")

st.subheader("📥 Input Data")
D = st.number_input("Permintaan tahunan (D)", value=10000)
S = st.number_input("Biaya pemesanan per pesanan (S)", value=200000)
H = st.number_input("Biaya penyimpanan per unit per tahun (H)", value=500)

if st.button("Hitung EOQ"):
    if D > 0 and S > 0 and H > 0:
        eoq = math.sqrt((2 * D * S) / H)
        jumlah_pemesanan = D / eoq
        total_biaya = (eoq / 2 * H) + (D / eoq * S)

        st.subheader("📊 Hasil Perhitungan")
        st.success(f"Jumlah Pemesanan Optimal (EOQ): {eoq:.2f} unit")
        st.info(f"Jumlah Pemesanan per Tahun: {jumlah_pemesanan:.2f} kali")
        st.warning(f"Total Biaya Persediaan Tahunan: Rp {total_biaya:,.2f}")
    else:
        st.error("Mohon masukkan semua input dengan benar!")
