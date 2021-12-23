import os
import random
import argparse
# Import your Ingestor and MemeEngine classes
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
    parser = argparse.ArgumentParser(description="Generates meme and prints their path")
    parser.add_argument("--path", type=str, default=None,
                    help="path to an image file")
    body_default = "Every dog has its day"
    parser.add_argument("--body", type=str,
                        default=None,
                        help="quote body to add to the image")
    parser.add_argument("--author", type=str,
                        default=None,
                        help="quote author to add to the image")
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
