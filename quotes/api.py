from flask import Flask, jsonify
from .quote_service import QuoteService

app = Flask(__name__)
service = QuoteService()


@app.get("/random")
def get_quote():
    return jsonify({"quote": service.get_random_quote()})

@app.get("/")
@app.get("/")
def index():
    return """
    <html>
        <head>
            <meta charset="utf-8">
            <title>Генератор цитат</title>
            <style>
                body {
                    background: linear-gradient(135deg, #667eea, #764ba2);
                    font-family: Arial, sans-serif;
                    height: 100vh;
                    margin: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }

                .card {
                    background: white;
                    padding: 40px;
                    border-radius: 16px;
                    width: 420px;
                    text-align: center;
                    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
                }

                h1 {
                    margin-top: 0;
                    color: #333;
                }

                #quote {
                    font-size: 20px;
                    margin: 30px 0;
                    color: #555;
                    min-height: 60px;
                    transition: opacity 0.3s;
                }

                button {
                    background: #667eea;
                    color: white;
                    border: none;
                    padding: 12px 24px;
                    font-size: 16px;
                    border-radius: 8px;
                    cursor: pointer;
                }

                button:hover {
                    background: #5a67d8;
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Генератор цитат</h1>

                <p id="quote">Загрузка...</p>

                <button onclick="loadQuote()">Новая цитата</button>
            </div>

            <script>
                async function loadQuote() {
                    const quoteEl = document.getElementById('quote');
                    quoteEl.style.opacity = 0;

                    const response = await fetch('/random');
                    const data = await response.json();

                    setTimeout(() => {
                        quoteEl.innerText = data.quote;
                        quoteEl.style.opacity = 1;
                    }, 300);
                }

                loadQuote();
            </script>
        </body>
    </html>
    """
