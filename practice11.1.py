from PIL import Image
import os

if not os.path.exists('result'):
    os.mkdir('result')

all_files = os.listdir() #список всех файлов

for file in all_files:
    if file.lower().endswith(('.jpg', '.png', '.jpeg')):
        try:
            img = Image.open(file)

            bw_img = img.convert('L')
            bw_img.save(f'result/bw_{file}')
            print(f'Обработано: {file}')

        except:
            print(f'Не получилось обработать {file}')

print('папкa result')