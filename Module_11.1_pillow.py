from PIL import Image, ImageFilter, ImageOps

# Открываем изображение
image = Image.open('images.jpg')
print("Оригинальное изображение:")
image.show()

# Изменение размера изображения
resized_image = image.resize((800, 600))
print("Измененное изображение (800x600):")
resized_image.show()

# Применение фильтра размытия с радиусом размытия 7
blurred_image = image.filter(ImageFilter.BoxBlur(7))
print("Изображение с примененным фильтром размытия:")
blurred_image.show()

# Инвертирование цветов изображения
inverted_image = ImageOps.invert(image)
print("Инвертированное изображение:")
inverted_image.show()

# Увеличение яркости изображения
bright_image = ImageEnhance.Brightness(image)
bright_image = bright_image.enhance(2.5)
print("Увеличение яркости изображения:")
bright_image.show()

# Перевернутое изображения
mirror_image = ImageOps.mirror(image)
print("Перевернутое изображение:")
mirror_image.show()
