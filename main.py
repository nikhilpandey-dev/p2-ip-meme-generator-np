from IngestorEngine import Ingestor

print('Text Ingestor')
print(Ingestor.parse('./_data/SimpleLines/SimpleLines.txt'))

print('Docx Ingestor')
print(Ingestor.parse('./_data/SimpleLines/SimpleLines.docx'))

print('CSV Ingestor')
print(Ingestor.parse('./_data/SimpleLines/SimpleLines.csv'))

print('PDF Ingestor')
print(Ingestor.parse('./_data/SimpleLines/SimpleLines.pdf'))
