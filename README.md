# Anonim Veri Oluşturucu

Bu proje, test ve geliştirme amacıyla anonimleştirilmiş kimlik verileri oluşturmak için bir Python betiği içerir.

## Açıklama

`anonimler.py` betiği, aşağıdaki alanları içeren rastgele veriler üretir:

*   Ad Soyad
*   Birim
*   Unvan
*   T.C. Kimlik No
*   Doğum Tarihi
*   Doğum Yeri
*   Kart No
*   Veriliş Tarihi

Oluşturulan veriler, `anonim_kimlik_verisi.csv` adlı bir CSV dosyasına kaydedilir.

## Bağımlılıklar

Bu betiği çalıştırmak için aşağıdaki Python kütüphanelerinin kurulu olması gerekir:

*   pandas
*   Faker

Bu bağımlılıkları pip kullanarak kurabilirsiniz:

```bash
pip install pandas Faker
```

## Kullanım

Betiği çalıştırmak için terminalinizde aşağıdaki komutu kullanın:

```bash
python anonimler.py
```

Bu komut, betiğin bulunduğu dizinde `anonim_kimlik_verisi.csv` dosyasını oluşturacaktır.

## Veri Alanları

*   **Ad Soyad**: `Faker` kütüphanesi kullanılarak oluşturulmuş rastgele Türkçe ad ve soyadlar.
*   **Birim**: Önceden tanımlanmış bir listeden rastgele seçilen birim adları (`İmam-Hatip`, `Müezzin`, `Memur`, vb.).
*   **Unvan**: Önceden tanımlanmış bir listeden rastgele seçilen unvanlar (`Uzman Doktor`, `Pratisyen`, `Doçent`, vb.).
*   **T.C. Kimlik No**: Geçerli bir algoritma kullanılarak oluşturulmuş rastgele 11 haneli T.C. Kimlik Numaraları.
*   **Doğum Tarihi**: 1960 ve 2005 yılları arasında rastgele bir tarih.
*   **Doğum Yeri**: Önceden tanımlanmış bir şehir listesinden (`Adana`, `Ankara`, `İstanbul`, vb.) rastgele seçilen bir şehir.
*   **Kart No**: 10000000 ile 99999999 arasında rastgele 8 haneli bir numara.
*   **Veriliş Tarihi**: 2005 ve 2024 yılları arasında rastgele bir tarih.

## Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen bir pull request açın veya sorunları bildirin.
