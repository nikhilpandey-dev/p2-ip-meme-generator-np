from typing import List
from .IngestorInterface import IngestorInterface
from QuoteEngine import QuoteModel
import docx


class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path=path):
            raise Exception('Sorry unable to ingest docx file.')

        try:
            quotes: List[QuoteModel] = list()
            doc = docx.Document(path)
            for para in doc.paragraphs:
                if para.text != '':
                    text = para.text.replace('"', '')
                    # Splitting the string into a list containing body & author
                    parsed = text.split(' - ')
                    new_quote = QuoteModel(parsed[0], parsed[1])
                    quotes.append(new_quote)
            return quotes
        except Exception as e:
            print("The following error occurred:\n", e)
