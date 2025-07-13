# eoq_calculator.py

import math

def hitung_eoq(D, S, H):
    """
    Menghitung EOQ (Economic Order Quantity)
    D: Permintaan tahunan
    S: Biaya pemesanan
    H: Biaya penyimpanan
    """
    eoq = math.sqrt((2 * D * S) / H)
    total_order = D / eoq
    total_cost = (eoq / 2 * H) + (D / eoq * S)
    return eoq, total_cost, total_order

def tampilkan_hasil(D, S, H):
    eoq, total_cost, total_order = hitung_eoq(D, S, H)
    print("=== Hasil Perhitungan EOQ untuk Produksi Es Krim ===")
    print(f"Permintaan tahunan (liter): {D}")
    print(f"Biaya pemesanan per pesanan: Rp{S:,.0f}")
    print(f"Biaya penyimpanan per liter/tahun: Rp{H:,.0f}")
    print(f"\n>> EOQ (Jumlah optimal pemesanan): {eoq:.2f} liter")
    print(f">> Jumlah pemesanan per tahun: {total_order:.2f} kali")
    print(f">> Total biaya persediaan tahunan: Rp{total_cost:,.2f}")

# Studi kasus es krim
if __name__ == "__main__":
    permintaan_tahunan = 10000   # D
    biaya_pemesanan = 200000     # S
    biaya_penyimpanan = 500      # H

    tampilkan_hasil(permintaan_tahunan, biaya_pemesanan, biaya_penyimpanan)

