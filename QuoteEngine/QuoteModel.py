class QuoteModel:

    def __init__(self, body: str, author: str) -> None:

        """Create a new QuoteModel"""
        # Moved double quote removal to QuoteModel for DRY
        self.body = body.replace('"', '')
        self.author = author

    def __repr__(self) -> str:
        return f'\"{self.body}\" - {self.author}'

    def __str__(self) -> str:
        return f"{self.body} - {self.author}"
