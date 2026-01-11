from .quote_service import QuoteService


def run_cli():
    service = QuoteService()
    print(service.get_random_quote())
