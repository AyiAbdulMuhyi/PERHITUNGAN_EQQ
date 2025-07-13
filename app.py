# app.py
import streamlit as st
import math
import matplotlib.pyplot as plt 
import numpy as np

st.set_page_config(page_title="Kalkulator EOQ", page_icon="📦")
st.title("📦 Aplikasi Perhitungan EOQ (Economic Order Quantity)")

st.markdown("Simulasi sistem persediaan untuk menentukan jumlah pemesanan optimal (EOQ).")

st.subheader("📥 Input Data")
D = st.number_input("Permintaan tahunan (D)", value=10000)
S = st.number_input("Biaya pemesanan per pesanan (S)", value=200000)
H = st.number_input("Biaya penyimpanan per unit per tahun (H)", value=500)

if st.button("Hitung EOQ"):
    if D > 0 and S > 0 and H > 0:
        # Hitung EOQ
        eoq = math.sqrt((2 * D * S) / H)
        jumlah_pemesanan = D / eoq
        total_biaya = (eoq / 2 * H) + (D / eoq * S)

        st.subheader("📊 Hasil Perhitungan")
        st.success(f"Jumlah Pemesanan Optimal (EOQ): {eoq:.2f} unit")
        st.info(f"Jumlah Pemesanan per Tahun: {jumlah_pemesanan:.2f} kali")
        st.warning(f"Total Biaya Persediaan Tahunan: Rp {total_biaya:,.2f}")

        # Buat grafik: Total biaya vs jumlah pemesanan (Q)
        st.subheader("📈 Grafik Total Biaya vs Jumlah Pemesanan")
        Q = np.linspace(100, D, 100)
        biaya_penyimpanan = (Q / 2) * H
        biaya_pemesanan = (D / Q) * S
        total_cost = biaya_penyimpanan + biaya_pemesanan

        fig, ax = plt.subplots()
        ax.plot(Q, total_cost, label='Total Biaya', color='blue')
        ax.plot(Q, biaya_penyimpanan, '--', label='Biaya Penyimpanan', color='green')
        ax.plot(Q, biaya_pemesanan, '--', label='Biaya Pemesanan', color='red')
        ax.axvline(eoq, color='purple', linestyle=':', label=f'EOQ = {eoq:.2f}')
        ax.set_xlabel("Jumlah Pesanan (Q)")
        ax.set_ylabel("Biaya (Rp)")
        ax.set_title("Grafik Total Biaya vs Jumlah Pemesanan")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)
    else:
        st.error("Mohon masukkan semua input dengan benar!")
