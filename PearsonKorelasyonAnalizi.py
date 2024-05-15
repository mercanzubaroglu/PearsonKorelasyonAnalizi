import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Excel dosyasını pandas ile okuyarak veriyi yükleme
veri = pd.read_excel("Thyo.xlsx")

# Tarih sütununu datetime formatına dönüştürme
veri["Tarih"] = pd.to_datetime(veri["Tarih"], format="%d-%m-%Y")

# Tarih sütununu indeks olarak ayarlama
veri.set_index("Tarih", inplace=True)

# Kapanış ve AOF fiyatlarını karşılaştırmak için bir çizgi grafiği oluşturma
plt.figure(figsize=(8,5))
plt.plot(veri.index, veri["Kapanış(TL)"], label="Kapanış Fiyatı")
plt.plot(veri.index, veri["AOF(TL)"], label="AOF Fiyatı")
plt.xlabel("Tarih")
plt.ylabel("Fiyat (TL)")
plt.title("Kapanış Fiyatı ve AOF Fiyatı Karşılaştırması")
plt.legend()
plt.grid(True)
plt.show()

# Veri setindeki belirli sütunların bir kısmını yazdırma
print(veri[["Tarih","Kapanış(TL)","AOF(TL)"]])

# Kapanış ve AOF fiyatları arasındaki korelasyonu hesaplama
print(veri[["Kapanış(TL)","AOF(TL)"]].corr())

# Eksik verilerin sayısını yazdırma
eksik_veri = veri.isnull().sum()
print(eksik_veri)

# Eksik verilerin ısı haritasını görselleştirme
sns.heatmap(veri.isnull(), cbar=False)
plt.show()

# Pearson korelasyon matrisini görselleştirme
korelasyon = veri.corr(method='pearson')
plt.figure(figsize=(10,8))
sns.heatmap(korelasyon, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Pearson Korelasyon Matrisi')
plt.show()
#Bu kod, bir veri çerçevesindeki değişkenler arasındaki ilişkiyi görselleştirmek için kullanılır.
#Heatmap, korelasyon matrisindeki değerlerin renklerle gösterilmesini sağlar ve böylece değişkenler arasındaki ilişkiyi anlamaya yardımcı olur.

# Fiyat değişimlerinin entropisini hesaplama
fiyat_degisimleri = veri["Kapanış(TL)"].diff().dropna()
histogram, fiyat_araliklari = np.histogram(fiyat_degisimleri, bins='auto', density=True)
olasiliklar = histogram * np.diff(fiyat_araliklari)
entropi = -np.sum(olasiliklar * np.log2(olasiliklar + 1e-10))  # Sıfıra bölme hatasını önlemek için küçük bir değer eklenir
print("Hisse Senedi Fiyatlarının Entropisi:", entropi)
