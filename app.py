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
    reader = easyocr.Reader(['en', 'ch_sim'])
    results = reader.readtext(image)
    return ' '.join([result[1] for result in results])

openai.api_key = 'api key'

def analyze_text_with_llm(text):
    prompt = """
    Analyze the following text for harmful content related to self-injury, eating disorders, or unauthentic weight loss product advice.
    The text would be Chinese or English, or combined.
    Please identify if the text contains any references or indications of the following:
    - Self-harm actions or methods
    - Negative body image or severe dieting behavior
    - Encouragement of disordered eating habits
    - Descriptions of self-injury or eating disorders
    - Promotion of unofficial or unauthentic weight loss products

    Provide reasoning for your decision.

    Examples:
    1. "I can't stop thinking about cutting myself." -> This text contains self-harm actions.
    2. "I haven't eaten in three days to lose weight." -> This text indicates severe dieting behavior.
    3. "I admire how thin they are; I wish I could be like that by skipping meals." -> This text encourages disordered eating habits.
    4. "I feel like I'm too fat even though everyone says I'm thin." -> This text shows negative body image.
    5. "Try this amazing weight loss pill that guarantees results in one week!" -> This text promotes unauthentic weight loss products.

    Text to analyze:
    """
    prompt += text

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that detects harmful content related to self-injury, eating disorders, or unauthentic weight loss product advice in provided texts. Your responses should be concise and specific, providing reasons for your decisions."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=250
    )
    return response['choices'][0]['message']['content']

if __name__ == '__main__':
    app.run(debug=True)
