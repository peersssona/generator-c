from quotes.quote_service import QuoteService


def test_quote_not_empty():
    service = QuoteService()
    quote = service.get_random_quote()

    assert isinstance(quote, str)
    assert len(quote) > 0
