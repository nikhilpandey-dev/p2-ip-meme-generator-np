from typing import List
from .IngestorInterface import IngestorInterface
from QuoteEngine import QuoteModel
import subprocess
import os
import random
import logging
import traceback


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path=path):
            raise Exception('Sorry unable to ingest PDF file.')
        try:
            quotes: List[QuoteModel] = list()
            tmp = f"./tmp/pdf-to-text-{random.randint(1, 1000)}.txt"
            print('tmp file is:', tmp)
            call = subprocess.call(['pdftotext', path, tmp])
            file_ref = open(tmp, "r")
            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split(' - ')
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)
            # Closing the temp file
            file_ref.close()
            # Removing the temp file
            os.remove(tmp)
            return quotes
        except Exception as e:
            print("The following error occurred:\n", e)