import qrcode, os, sys
from PIL import Image

def qrGenerator(link, file_name):
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        border=1
    )
    QRcode.add_data(link)
    QRcode.make(fit=True)

    QRimg = QRcode.make_image(fill_color="black", back_color="white").convert('RGB')

    QRimg.save(f'{file_name}.png')
    print('Kod QR został wygenerowany')

def rgbToCmyk(image_path):
    if not os.path.exists(image_path.strip('')):
        print("Plik o tej ścieżce nie istnieje")
        sys.exit(0)

    img = Image.open(image_path)
    cmyk_img = img.convert('CMYK')
    
    name, _ = os.path.splitext(image_path)
    output_name = f"{name}_cmyk.jpg"
    cmyk_img.save(output_name, quality=100)
    print(f"Zamiana RGB na CMYK została wykonana pomyślnie. Plik znajduje się w {os.path.abspath(output_name)}")

wybor = int(input("Wybierz, co chcesz zrobić:\n 1. Generowanie kodu QR\n 2. Zamiana RGB na CMYK\n"))

match wybor:
    case 1:
        qrGenerator(input("Wpisz pełny link do strony: "), input("Wpisz nazwę otrzymanego kodu QR (bez rozszerzenia): "))

    case 2:
        rgbToCmyk(input("Wpisz pełną ścieżkę do pliku: ").strip('"'))

    case _:
        print("Nie ma takiego numeru na liście wyboru")
        sys.exit(0)