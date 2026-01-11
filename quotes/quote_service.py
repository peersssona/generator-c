import random
from .data_loader import load_quotes


class QuoteService:
    def __init__(self):
        self.quotes = load_quotes()

    def get_random_quote(self) -> str:
        return random.choice(self.quotes)
