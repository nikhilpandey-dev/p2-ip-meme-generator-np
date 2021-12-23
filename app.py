import random
import os
import requests
from flask import Flask, render_template, abort, request
from typing import List

# Import your Ingestor and MemeEngine classes
from QuoteEngine import QuoteModel
from IngestorEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Using the Ingestor class to parse all files in the
    # quote_files variable
    quotes: List[QuoteModel] = list()
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    # Using the pythons standard library os class to find all
    # images within the images images_path directory
    imgs: List[str] = list()
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # Using the random python standard library class to:

    # 1. select a random image from imgs array
    img: str = random.choice(imgs)
    # 2. select a random quote from the quotes array
    quote: QuoteModel = random.choice(quotes)
    path: str = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.

    """
    making provision for the backup image url, body and quote,
     in case I don't get any
    """
    image_url = ("http://thecatandthedog.com/wp-content/uploads/2020/11/"
                 "105992231-1561667465295gettyimages-521697453.jpeg")
    """ Steaps for getting image data from url and
         saving it to disk using request
        1. Get the image url
        2. Use requests.get to fetch image data
        3. Create a temp file
        4. Write image data in temp file created at step 3
    """
    form_img_url = request.form.get("image_url")
    backup_img_url = ("https://pixabay.com/get/"
                      "gd1d20cefd6a2bf195717756ffbd7dac76986402fdac93dede9f8"
                      "c6ea9ceb1fb66bfd8338f80bb5b4821566e43ef914b7_640.jpg")
    image_url = form_img_url if form_img_url else backup_img_url

    r = requests.get(image_url, stream=True).content
    flask_temp = f'./static/img-flask-{random.randint(0, 100)}.jpg'
    with open(flask_temp, 'wb') as f:
        f.write(r)
    # else:
    #     r = requests.get(image_url, stream=True).content
    #     flask_temp = f'./static/img-flask-{random.randint(0, 100)}.jpg'
    #     with open(flask_temp, 'wb') as f:
    #         f.write(r)

    print('Tmp is: ', flask_temp)
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.

    backup_quote_body = "Every dog must have his day"
    form_body = request.form.get("body", "")
    body = form_body if form_body else backup_quote_body
    backup_quote_author = "Unknown"
    form_author = request.form.get("author", "")
    author = form_author if form_author else backup_quote_author
    quote: QuoteModel = QuoteModel(body=body, author=author)
    path = meme.make_meme(flask_temp, quote.body, quote.author)
    print(path)
    # 3. Remove the temporary saved image.
    os.remove(flask_temp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
