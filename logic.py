from googletrans import Translator
import easyocr


translator = Translator()

def tran(text, dest='en'):
    a = translator.translate(text, dest)
    return a.text

def text_recognition(file_path):
    reader = easyocr.Reader(["ru", "en"])
    result_list = reader.readtext(file_path, detail=0)
    result = ''
    for s in result_list:
        result += f'{s} '
    return result