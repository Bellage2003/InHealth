# InHealth

- Instagram API: https://github.com/subzeroid/instagrapi?tab=readme-ov-file
- Harmful content detection model: https://francesconatali.com/personalprojects/ML/toxic-text-detection/
- OCR: https://github.com/JaidedAI/EasyOCR

## Instruction

### Data Collection
- insAPI.ipynb : This is the jupyter notebook we used to call the Instagrapi and collect data. In this notebook, we log in with our sock puppet account and query for data about hashtags, medias, posts, and captions.

### Harmful Content Differentiation
- Instagram API.ipynb: We explored and collected the caption texts under the 5 most recent posts by searching for each hashtag. After collecting the caption text, we manually copy them into the Harmful Content Detection Model and validate the toxicity.

### Explore Patterns:
- Data_Collection&Explore_Pattern.ipynb: This notebook has an overview of all 40 hashtags. And, we also collected like and comment counts under 200 posts. We wrote functions to analyze the like and comment counts to understand how Instagram's engagement mechanism affect the spreading of sensitive content.

### OCR + LLM
- app.py: The Python file we wrote includes the logic to fetch the image, pass it to the LLM, and generate results.
- index.html: the HTML to paste and submit the image URL
- result.html: the HTML that returns the analysis results about the image
- requirements.txt: requirements packages needed to run the program
