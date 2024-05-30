from flask import Flask, request, render_template
import requests
from PIL import Image
from io import BytesIO
import easyocr
import openai

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['instagram_url']
        image = fetch_image(url)
        if image:
            extracted_text = extract_text(image)
            analysis_result = analyze_text_with_llm(extracted_text)
            return render_template('result.html', analysis=analysis_result, text=extracted_text)
        else:
            return "Failed to retrieve image. Please check the URL and try again."
    return render_template('index.html')

def fetch_image(url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        response.raw.decode_content = True
        image = Image.open(response.raw)
        return image
    else:
        return None

def extract_text(image):
    reader = easyocr.Reader(['en'])
    results = reader.readtext(image)
    return ' '.join([result[1] for result in results])

openai.api_key = 'sk-proj-iny7Jne7gdnU75FVK2dMT3BlbkFJNShzyiYaBNuyJ6eo7z5w'

def analyze_text_with_llm(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Analyze the following text for harmful content related to self-injury or eating disorders."}, 
                  {"role": "user", "content": text}]
    )
    return response['choices'][0]['message']['content']

if __name__ == '__main__':
    app.run(debug=True)
