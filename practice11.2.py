from PIL import Image

image_path = "1.jpg"

if not image_path.lower().endswith(('.jpg', '.jpeg', '.png')):
    print(f"Ошибка: файл '{image_path}' не JPG/PNG")
else:
    try:
        with Image.open(image_path) as img:
            img.show()

            width, height = img.size
            print(f"1. Размер: {width}x{height} пикселей")
            print(f"2. Формат: {img.format}")
            print(f"3. Цветовая модель: {img.mode}")

    except FileNotFoundError:
        print(f"Ошибка: файл '{image_path}' не найден!")
