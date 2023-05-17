from PIL import Image
from pytesseract import pytesseract
from flask import Flask, request,jsonify
app = Flask(__name__)

@app.route('/')
def imaget():
    path_to_tesseract = r"C:\Users\Raashi M.Y\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
    image_path = r"C:\Users\Raashi M.Y\Desktop\Miniproj\sample2.png"
    img = Image.open(image_path)
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(img)
    return text
@app.route('/addfile',methods=["POST"])
def add_guide():
    image_path = request.json['image_path']
app.run()