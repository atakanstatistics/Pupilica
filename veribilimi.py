import pandas as pd

# veriyi içeri aktar
veri = pd.read_csv("datasets/olimpiyatlar.csv")
veri_head = veri.head(15)

"""
Veride İncelenecekler

veride nan değerler var, cikart veya doldur
games columnı gereksiz, veriden drop
her sporcu madalya alamamış: nan = madalya alamamis
id gereksiz
bir kişi iki takıma katılmış? 1900 yılında iki ülke var mıydı?
ülke kısatlması veya takim gereksiz
1920'den önceki veriler güvenilir mi?

"""


veri.info() # Önce verimize uzaktan bakıyoruz.

colum = veri.columns
veri.rename(columns = {
	"ID" : "id",
	"Name" : "isim",
	"Sex" : "cinsiyet",
	"Age" : "yas",
	"Height": "boy",
	"Weight": "kilo",
	"Team": "takim",
	"NOC" : "uok", # ulusal olimpiyat komite
	"Games" : "oyunlar",
	"Year" : "yil",
	"Season": "sezon",
	"City": "sehir",
	"Sport": "spor",
	"Event": "etkinlik",
	"Medal": "madalya"
    }, inplace = True)

# gereksiz/yararsiz verinin çıkartılması

veri = veri.drop(["id","oyunlar"], axis=1) #liste sütun adlarınnı silmek





















