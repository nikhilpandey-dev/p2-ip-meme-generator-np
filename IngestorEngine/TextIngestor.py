from typing import List
from .IngestorInterface import IngestorInterface
from QuoteEngine import QuoteModel
import re


class TextIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path=path):
            raise Exception('Sorry unable to ingest text file.')

        try:
            quotes: List[QuoteModel] = list()
            with open(path, 'r') as infile:
                # Read the text cintents into a big string
                contents: str = infile.read()
                # Remove all white space from the contents
                contents = contents.strip()
                contents = contents.replace('"', '')
                # Split the string into a list by line breaks.
                quotes_list = contents.split('\n')
                for q in quotes_list:
                    """ Splitting a string based on multiple delimiters.
                        The source of this line of code is inspired
                         from the following stackoverflow question:
                        https://stackoverflow.com/questions/4998629/split-string-with-multiple-delimiters-in-python
                        and the specific answer:
                        https://stackoverflow.com/a/4998688
                    """
                    quotes_body: List[str] = re.split("- | ' '", q)
                    quote: QuoteModel = QuoteModel(quotes_body[0],
                                                   quotes_body[1])
                    quotes.append(quote)
            infile.close()
            return quotes
        except Exception as e:
            print("The following error occurred:\n", e)
