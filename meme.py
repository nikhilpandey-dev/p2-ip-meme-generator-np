import os
import random
import argparse
# @TODO Import your Ingestor and MemeEngine classes
# @TODO Completed
from QuoteEngine import QuoteModel
from IngestorEngine import Ingestor
from MemeEngine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]
        
        print('Image arrays are: ', imgs)

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    print('Path is: ', path)
    return path


if __name__ == "__main__":
    # @TODO Use ArguentParser to parse the following CLI arguments
    parser = argparse.ArgumentParser(description="Putting quote on the image")
    # path - path to an image file
    img_default = "./_data/photos/dog/"
    parser.add_argument('--path', type=str, default=img_default, help="Picture on which you want to put a quote")
    
    # body - quote body to add to the image
    body_default = "Every dog must have his day."
    parser.add_argument('--body', type=str, default=body_default, help='Please give your quote about the dog')
    
    # author - quote author to add to the image
    author_default = "Unknown"
    parser.add_argument('--author', type=str, default=author_default, help='Please provide the author name')
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
