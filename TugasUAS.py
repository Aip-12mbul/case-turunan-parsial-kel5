import streamlit as st
import math
import plotly.express as px
import pandas as pd

#Judul Aplikasi
st.title('Menghitung Jumlah Pemesanan Optimal')

#Studi Kasus
st.markdown('Sebuah negara memerlukan 11.000 unit mesin fotokopi per tahun. Setiap kali memesan mesin fotokopi, negara tersebut dikenakan biaya pengiriman sebesar Rp.1.000.000. Biaya penyimpanan mesin fotokopi di gudang adalah Rp.5.000 per unit per tahun. Presiden ingin mengetahui berapa unit yang sebaiknya dipesan agar mendapat biaya total minimum?')

#Menampilkan rumus EOQ
st.latex(r'''EOQ = \sqrt{ \frac{2DS}{H} }''')

#Info Tambahan
st.markdown("""
**Keterangan:** 
- D = Permintaan tahunan (unit)
- S = Biaya pemesanan per pesanan
- H = Biaya penyimpanan per unit per tahun
""")

#Input angka
D = st.number_input("Permintaan tahunan (D)", 11000)
S = st.number_input("Biaya pemesanan per pesanan (S)", 1000000)
H = st.number_input("Biaya penyimpanan per unit per tahun (H)", 5000)
Hitung = st.button("Hitung EOQ")

#Hitung EOQ
if Hitung :
    eoq = math.sqrt((2 * D * S) / H)
    st.success(f"Jumlah Pemesanan Ekonomis (EOQ): {eoq:.2f} unit")
    
    #Interpretasi
    st.markdown('Negara sebaiknya memesan 2097 unit setiap kali memesan agar total biaya pemesanan dan penyimpanan minimum.')
    
    #Total biaya persediaan = biaya pemesanan + biaya penyimpanan
    jumlah_pemesanan = D / eoq
    total_biaya = (jumlah_pemesanan * S) + (eoq / 2 * H)
    
    st.info(f"Jumlah pemesanan per tahun: {jumlah_pemesanan:.2f} kali")
    st.info(f"Total biaya persediaan: Rp {total_biaya:,.2f}")
    
    #Data grafik
    df = pd.DataFrame({
        'Komponen Biaya': ['Biaya Pemesanan', 'Biaya Penyimpanan'],
        'Nilai (Rp)': [jumlah_pemesanan * S, (eoq / 2) * H]
    })
    
    fig = px.bar(df, x='Komponen Biaya', y='Nilai (Rp)',
                 title='Grafik Komponen Total Biaya Persediaan',
                 text='Nilai (Rp)',
                 labels={'Nilai (Rp)': 'Nilai dalam Rupiah'},
                 color='Komponen Biaya')
    
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_layout(yaxis_tickprefix='Rp ', yaxis_ticksuffix='')
    
    st.plotly_chart(fig)