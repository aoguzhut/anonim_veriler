import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker('tr_TR')

birimler = ['İmam-Hatip', 'Müezzin', 'Memur', 'V.H.K.İ.', 'Mühendis', 'Daire Başkanı', 'Tekniker', 'Teknisyen']
unvanlar = ['Uzman Doktor', 'Pratisyen', 'Doçent', 'Profesör', 'Asistan']
sehirler = ['Adana', 'Ankara', 'Antalya', 'Bursa', 'Diyarbakır', 'Erzurum', 'Eskişehir',
            'Gaziantep', 'İstanbul', 'İzmir', 'Kayseri', 'Konya', 'Malatya', 'Mersin', 'Samsun', 'Trabzon', 'Van', 'Rize']

def generate_tc():
    tc = [random.randint(1, 9)] + [random.randint(0, 9) for _ in range(8)]
    odd_sum = sum(tc[0:9:2])
    even_sum = sum(tc[1:8:2])
    digit10 = ((odd_sum * 7) - even_sum) % 10
    digit11 = (sum(tc[:9]) + digit10) % 10
    return ''.join(map(str, tc + [digit10, digit11]))

def random_date(start_year, end_year):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    delta = end - start
    return (start + timedelta(days=random.randint(0, delta.days))).date()

rows = []
for _ in range(100):
    ad_soyad = fake.name()
    birim = random.choice(birimler)
    unvan = random.choice(unvanlar)
    tc = generate_tc()
    dogum_tarihi = random_date(1960, 2005)
    dogum_yeri = random.choice(sehirler)
    kart_no = random.randint(10000000, 99999999)
    verilis_tarihi = random_date(2005, 2024)
    
    rows.append([
        ad_soyad, birim, unvan, tc, dogum_tarihi, dogum_yeri, kart_no, verilis_tarihi
    ])

df = pd.DataFrame(rows, columns=[
    "Ad Soyad", "Birim", "Unvan", "T.C. Kimlik No", "Doğum Tarihi",
    "Doğum Yeri", "Kart No", "Veriliş Tarihi"
])

df.to_csv("anonim_kimlik_verisi.csv", index=False, encoding="utf-8")
