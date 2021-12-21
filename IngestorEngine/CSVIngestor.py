from typing import List
from .IngestorInterface import IngestorInterface
from QuoteEngine import QuoteModel
import pandas


class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path=path):
            raise Exception('Sorry unable to ingest CSV file.')

        try:
            quotes: List[QuoteModel] = list()
            df = pandas.read_csv(path, header=0)
            for _, row in df.iterrows():
                new_quote = QuoteModel(row['body'], row['author'])
                quotes.append(new_quote)
            return quotes
        except Exception as e:
            print("The following error occurred:\n", e)
