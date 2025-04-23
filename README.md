# BST Portal - Yakında Burada

Bu, asıl BST Portal projesi tamamlanana kadar kullanılacak geçici bir "Yakında Burada" Django projesidir.

## Özellikler

- Şık ve modern tasarım
- Responsive tasarım (mobil cihazlara uyumlu)
- Sosyal medya bağlantıları
- İletişim bilgileri

## Kurulum

1. Projeyi klonlayın:
```
git clone https://github.com/kullanici/bst_portal.git
cd bst_portal
```

2. Gerekli paketleri yükleyin:
```
pip install -r requirements.txt
```

3. Veritabanı migrasyonlarını uygulayın:
```
python manage.py migrate
```

4. Geliştirme sunucusunu başlatın:
```
python manage.py runserver
```

5. Tarayıcınızda `http://127.0.0.1:8000` adresine gidin.

## Proje Yapısı

- `bst_portal/` - Ana proje klasörü
- `coming_soon/` - "Yakında Burada" uygulaması
  - `static/` - Statik dosyalar (CSS, JS, görseller)
  - `templates/` - HTML şablonları

## Özelleştirme

- Renkleri ve stilleri değiştirmek için `coming_soon/static/coming_soon/css/style.css` dosyasını düzenleyin
- İletişim bilgilerini ve diğer içeriği değiştirmek için `coming_soon/templates/coming_soon/index.html` dosyasını düzenleyin

## Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır. 
