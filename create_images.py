# Geçici logo ve desen oluşturmak için basit bir script
import os
from PIL import Image, ImageDraw, ImageFont

# Klasörlerin varlığını kontrol et
image_dir = 'coming_soon/static/coming_soon/images'
os.makedirs(image_dir, exist_ok=True)

# Logo oluştur - Basit mavi bir daire içinde BST yazısı
def create_logo():
    img = Image.new('RGBA', (200, 200), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Daire çiz
    draw.ellipse((10, 10, 190, 190), fill=(30, 87, 153, 255))
    
    # Yazı ekle
    try:
        font = ImageFont.truetype("arial.ttf", 80)
    except IOError:
        font = ImageFont.load_default()
    
    draw.text((50, 60), "BST", font=font, fill=(255, 255, 255, 255))
    
    # Kaydet
    img.save(os.path.join(image_dir, 'logo.png'))
    print("Logo oluşturuldu!")

# Desen oluştur - Basit bir arka plan deseni
def create_pattern():
    img = Image.new('RGBA', (400, 400), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Desenler çiz
    for x in range(0, 400, 20):
        for y in range(0, 400, 20):
            draw.rectangle((x, y, x+10, y+10), fill=(30, 87, 153, 50))
    
    # Kaydet
    img.save(os.path.join(image_dir, 'pattern.png'))
    print("Desen oluşturuldu!")

if __name__ == "__main__":
    create_logo()
    create_pattern()
    print("Görseller başarıyla oluşturuldu!") 