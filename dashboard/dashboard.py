import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

st.title("Air Quality Dashboard")
df = pd.read_csv('dashboard/main_data.csv')

st.dataframe(df, height=400)

st.title("Hubungan Antara Konsentrasi PM2.5 serta PM10 dengan Variabel Lainnya")

df['year_month'] = df['year'].astype(str) + '-' + df['month'].astype(str)
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
df_agg_month = df.groupby(['station', 'year_month'])[numeric_columns].mean().reset_index()

scatter_color = 'blue' 
line_color = 'red'      

plt.figure(figsize=(16, 12))

plt.subplot(3, 2, 1)
sns.regplot(x='PM2.5', y='NO2', data=df_agg_month, color=line_color, scatter_kws={'s':50, 'alpha':0.8, 'color': scatter_color}, line_kws={'color':line_color})
plt.title('Korelasi PM2.5 dengan NO2 (r={:.2f})'.format(pearsonr(df_agg_month['PM2.5'], df_agg_month['NO2'])[0]), fontsize=12)

plt.subplot(3, 2, 2)
sns.regplot(x='PM2.5', y='CO', data=df_agg_month, color=line_color, scatter_kws={'s':50, 'alpha':0.8, 'color': scatter_color}, line_kws={'color':line_color})
plt.title('Korelasi PM2.5 dengan CO (r={:.2f})'.format(pearsonr(df_agg_month['PM2.5'], df_agg_month['CO'])[0]), fontsize=12)

plt.subplot(3, 2, 3)
sns.regplot(x='PM2.5', y='O3', data=df_agg_month, color=line_color, scatter_kws={'s':50, 'alpha':0.8, 'color': scatter_color}, line_kws={'color':line_color})
plt.title('Korelasi PM2.5 dengan Ozon (O3) (r={:.2f})'.format(pearsonr(df_agg_month['PM2.5'], df_agg_month['O3'])[0]), fontsize=12)

plt.subplot(3, 2, 4)
sns.regplot(x='TEMP', y='PM2.5', data=df_agg_month, color=line_color, scatter_kws={'s':50, 'alpha':0.8, 'color': scatter_color}, line_kws={'color':line_color})
plt.title('Pengaruh Suhu terhadap PM2.5 (r={:.2f})'.format(pearsonr(df_agg_month['TEMP'], df_agg_month['PM2.5'])[0]), fontsize=12)

plt.subplot(3, 2, 5)
sns.regplot(x='WSPM', y='PM2.5', data=df_agg_month, color=line_color, scatter_kws={'s':50, 'alpha':0.8, 'color': scatter_color}, line_kws={'color':line_color})
plt.title('Pengaruh Kecepatan Angin terhadap PM2.5 (r={:.2f})'.format(pearsonr(df_agg_month['WSPM'], df_agg_month['PM2.5'])[0]), fontsize=12)

plt.subplot(3, 2, 6)
sns.regplot(x='PRES', y='PM2.5', data=df_agg_month, color=line_color, scatter_kws={'s':50, 'alpha':0.8, 'color': scatter_color}, line_kws={'color':line_color})
plt.title('Pengaruh Tekanan Udara terhadap PM2.5 (r={:.2f})'.format(pearsonr(df_agg_month['PRES'], df_agg_month['PM2.5'])[0]), fontsize=12)

plt.tight_layout()
st.pyplot(plt)

scatter_color = 'blue'  
line_color = 'red'      

plt.figure(figsize=(16, 12))

plt.subplot(3, 2, 1)
sns.regplot(x='PM10', y='NO2', data=df_agg_month, color=line_color, scatter_kws={'s':50, 'alpha':0.8, 'color': scatter_color}, line_kws={'color':line_color})
plt.title('Korelasi PM10 dengan NO2 (r={:.2f})'.format(pearsonr(df_agg_month['PM10'], df_agg_month['NO2'])[0]), fontsize=12)

plt.subplot(3, 2, 2)
sns.regplot(x='PM10', y='CO', data=df_agg_month, color=line_color, scatter_kws={'s':50, 'alpha':0.8, 'color': scatter_color}, line_kws={'color':line_color})
plt.title('Korelasi PM10 dengan CO (r={:.2f})'.format(pearsonr(df_agg_month['PM10'], df_agg_month['CO'])[0]), fontsize=12)

plt.subplot(3, 2, 3)
sns.regplot(x='PM10', y='O3', data=df_agg_month, color=line_color, scatter_kws={'s':50, 'alpha':0.8, 'color': scatter_color}, line_kws={'color':line_color})
plt.title('Korelasi PM10 dengan Ozon (O3) (r={:.2f})'.format(pearsonr(df_agg_month['PM10'], df_agg_month['O3'])[0]), fontsize=12)

plt.subplot(3, 2, 4)
sns.regplot(x='TEMP', y='PM10', data=df_agg_month, color=line_color, scatter_kws={'s':50, 'alpha':0.8, 'color': scatter_color}, line_kws={'color':line_color})
plt.title('Pengaruh Suhu terhadap PM10 (r={:.2f})'.format(pearsonr(df_agg_month['TEMP'], df_agg_month['PM10'])[0]), fontsize=12)

plt.subplot(3, 2, 5)
sns.regplot(x='WSPM', y='PM10', data=df_agg_month, color=line_color, scatter_kws={'s':50, 'alpha':0.8, 'color': scatter_color}, line_kws={'color':line_color})
plt.title('Pengaruh Kecepatan Angin terhadap PM10 (r={:.2f})'.format(pearsonr(df_agg_month['WSPM'], df_agg_month['PM10'])[0]), fontsize=12)

plt.subplot(3, 2, 6)
sns.regplot(x='PRES', y='PM10', data=df_agg_month, color=line_color, scatter_kws={'s':50, 'alpha':0.8, 'color': scatter_color}, line_kws={'color':line_color})
plt.title('Pengaruh Tekanan Udara terhadap PM10 (r={:.2f})'.format(pearsonr(df_agg_month['PRES'], df_agg_month['PM10'])[0]), fontsize=12)

plt.tight_layout()
st.pyplot(plt)

st.markdown("""
1. **NO2 dan CO** memiliki korelasi positif yang kuat dengan **PM2.5** (r=0.73 untuk NO2, r=0.80 untuk CO) dan **PM10** (r=0.73 untuk NO2, r=0.62 untuk CO). Ini menunjukkan bahwa polusi dari kendaraan bermotor dan industri secara signifikan meningkatkan konsentrasi PM2.5 dan PM10.

2. **Ozon (O3)** memiliki korelasi negatif dengan **PM2.5** (r=-0.55) dan **PM10** (r=-0.43), artinya peningkatan Ozon menurunkan konsentrasi PM, kemungkinan terkait reaksi kimia di atmosfer.

3. **Suhu (TEMP)** memiliki korelasi negatif sedang dengan **PM2.5** (r=-0.46) dan **PM10** (r=-0.39), menunjukkan bahwa suhu yang lebih tinggi menurunkan konsentrasi polutan.

4. **Kecepatan Angin (WSPM)** menunjukkan hubungan lemah dengan **PM2.5** (r=-0.22) dan **PM10** (r=-0.04), menandakan dampaknya kecil pada penyebaran polusi.

5. **Tekanan Udara (PRES)** memiliki korelasi positif sedang dengan **PM2.5** (r=0.50) dan **PM10** (r=0.40), menunjukkan bahwa tekanan udara tinggi meningkatkan konsentrasi polutan.
""")
st.markdown(
    """
    <style>
    .centered-title {
        text-align: justify;
        text-align-last: justify;
    }
    </style>
    <h1 class="centered-title">Dinamika Perubahan Konsentrasi Rata-Rata PM2.5 dan PM10 di Setiap Stasiun Selama Periode 2013-2017</h1>
    """, 
    unsafe_allow_html=True
)
mean_pm25 = df_agg_month['PM2.5'].mean()

g = sns.FacetGrid(df_agg_month, col="station", col_wrap=4, height=3.5, aspect=1.2)
g.map(sns.lineplot, 'year_month', 'PM2.5', marker='o', color='blue')

for ax in g.axes.flat:
    ax.axhline(mean_pm25, ls='--', color='red', label=f'Rata-Rata Total: {mean_pm25:.2f}')
    ax.grid(True, axis='y', linestyle='--', alpha=0.7)  
    
g.set_titles("{col_name}")
g.set_axis_labels("Bulan", "PM2.5")
g.set_xticklabels(rotation=45)

plt.subplots_adjust(top=0.9)

g.fig.suptitle('Perbandingan Rata-Rata PM2.5 per Stasiun Tahun 2013-2017', fontsize=16, x=0.5)

plt.legend(loc='upper right', bbox_to_anchor=(1.5, 1))

plt.tight_layout()
st.pyplot(plt)
st.markdown("""
#### Dinamika Konsentrasi PM2.5:

Secara umum, fluktuasi konsentrasi PM2.5 di setiap stasiun menunjukkan variasi yang signifikan dari bulan ke bulan selama periode 2013-2017.

Perbedaan signifikan antara stasiun dapat dilihat dari tingkat variasi bulanan di beberapa stasiun, terutama di **Dongsi** dan **GuCheng**. Stasiun yang lebih rendah polutannya adalah **Huairou** dan **Shunyi**.

Faktor yang mungkin menyebabkan perbedaan tingkat polusi termasuk aktivitas industri dan kepadatan penduduk di daerah tersebut.
""")

st.markdown("<hr style='margin-top: 50px; margin-bottom: 50px;'>", unsafe_allow_html=True)
mean_pm25 = df_agg_month['PM10'].mean()

g = sns.FacetGrid(df_agg_month, col="station", col_wrap=4, height=3.5, aspect=1.2)
g.map(sns.lineplot, 'year_month', 'PM10', marker='o', color='blue')

for ax in g.axes.flat:
    ax.axhline(mean_pm25, ls='--', color='red', label=f'Rata-Rata Total: {mean_pm25:.2f}')
    ax.grid(True, axis='y', linestyle='--', alpha=0.7)  
    
g.set_titles("{col_name}")
g.set_axis_labels("Bulan", "PM10")
g.set_xticklabels(rotation=45)

plt.subplots_adjust(top=0.9)
g.fig.suptitle('Perbandingan Rata-Rata PM10 per Stasiun Tahun 2013-2017', fontsize=16)

plt.legend(loc='upper right', bbox_to_anchor=(1.5, 1))

plt.tight_layout()
st.pyplot(plt)
st.markdown("""
#### Dinamika Konsentrasi PM10:

Secara umum, fluktuasi konsentrasi PM10 di setiap stasiun menunjukkan variasi yang signifikan dari bulan ke bulan selama periode 2013-2017.

Perbedaan signifikan antara stasiun dapat dilihat dari tingkat variasi bulanan di beberapa stasiun, terutama di **Wanliu** dan **Wanshouxigong**. Stasiun yang lebih rendah polutannya adalah **Huairou** dan **Shunyi**.

Faktor yang mungkin menyebabkan perbedaan tingkat polusi termasuk aktivitas industri dan kepadatan penduduk di daerah tersebut.
""")
st.markdown(
    """
    <style>
    .justified-title {
        text-align: justify;
    }
    </style>
    <h1 class="justified-title">Perbedaan Distribusi Konsentrasi PM2.5 dan PM10 di Berbagai Stasiun</h1>
    """, 
    unsafe_allow_html=True
)
plt.figure(figsize=(14, 8))
sns.boxplot(data=df_agg_month, x='station', y='PM2.5', palette='Blues') 
plt.title('Distribusi PM2.5 di Setiap Stasiun', fontsize=16)
plt.xlabel('Stasiun', fontsize=12)
plt.ylabel('PM2.5', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

plt.figure(figsize=(14, 8))
sns.boxplot(data=df_agg_month, x='station', y='PM10', palette='Blues') 
plt.title('Distribusi PM10 di Setiap Stasiun', fontsize=16)
plt.xlabel('Stasiun', fontsize=12)
plt.ylabel('PM10', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)
st.markdown("""
- Konsentrasi PM2.5 bervariasi di tiap stasiun. Stasiun Dongsi dan Wanshouxigong memiliki rentang konsentrasi yang lebih tinggi, sementara Dingling memiliki konsentrasi terendah. Outlier terlihat di beberapa stasiun, terutama Changping dan Dongsi, yang mungkin menunjukkan kejadian polusi yang tidak biasa. 
- Konsentrasi PM10 juga menunjukkan variasi. GuCheng dan Wanliu memiliki konsentrasi PM10 lebih tinggi dibandingkan stasiun lain, dengan rentang nilai yang lebih besar. Dingling dan Huairou menunjukkan rentang konsentrasi PM10 yang lebih rendah.
""")
st.markdown(
    """
    <style>
    .justified-title {
        text-align: justify;
    }
    </style>
    <h1 class="justified-title">Distribusi PM2.5 dan PM10 Binned di Setiap Stasiun</h1>
    """, 
    unsafe_allow_html=True
)

bins_pm25 = [0, 50, 100, 150, np.inf]
bins_pm10 = [0, 50, 100, 150, np.inf]
labels = ['Low', 'Moderate', 'High', 'Very High']

df_agg_month['PM2.5_bin'] = pd.cut(df_agg_month['PM2.5'], bins=bins_pm25, labels=labels)
df_agg_month['PM10_bin'] = pd.cut(df_agg_month['PM10'], bins=bins_pm10, labels=labels)

print(df_agg_month[['station', 'year_month', 'PM2.5', 'PM2.5_bin', 'PM10', 'PM10_bin']].head())

plt.figure(figsize=(14, 7))

plt.subplot(1, 2, 1)
sns.countplot(x='station', hue='PM2.5_bin', data=df_agg_month, palette="Blues")
plt.title('Distribusi PM2.5 Binned di Setiap Stasiun')
plt.xticks(rotation=45)
plt.ylabel('Jumlah Observasi')
plt.xlabel('Stasiun')

plt.subplot(1, 2, 2)
sns.countplot(x='station', hue='PM10_bin', data=df_agg_month, palette="Blues")
plt.title('Distribusi PM10 Binned di Setiap Stasiun')
plt.xticks(rotation=45)
plt.ylabel('Jumlah Observasi')
plt.xlabel('Stasiun')

plt.tight_layout()
st.pyplot(plt)

st.markdown("""
- **Stasiun Aotizhongxin**: Mendominasi pada kategori PM2.5 dan PM10 dalam tingkat sedang (Moderate). 
- **Stasiun Dingling**: Menunjukkan lebih banyak pengamatan PM10 pada kategori sangat tinggi (Very High), dibandingkan PM2.5.
- **Stasiun GuanYuan dan Huairou**: Cenderung memiliki pengamatan rendah di semua kategori untuk kedua polutan.
- **Polusi PM2.5 dan PM10**: Secara umum, distribusi menunjukkan lebih banyak pengamatan di kategori Low hingga Moderate, dengan beberapa stasiun memiliki puncak di High dan Very High.
""")