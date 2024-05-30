# InHealth

- Instagram API: https://github.com/subzeroid/instagrapi?tab=readme-ov-file
- Harmful content detection model: https://francesconatali.com/personalprojects/ML/toxic-text-detection/
- OCR: https://github.com/JaidedAI/EasyOCR

## Instruction

### Data Collection
- insAPI.ipynb : This is the jupyter notebook we used to call the Instagrapi and collect data. In this notebook, we log in with our sock puppet account and query for data about hashtags, medias, posts, and captions.


### OCR + LLM
- app.py: The Python file we wrote includes the logic to fetch the image, pass it to the LLM, and generate results.
- index.html: the HTML to paste and submit the image URL
- result.html: the HTML that returns the analysis results about the image
- requirements.txt: requirements packages needed to run the program
