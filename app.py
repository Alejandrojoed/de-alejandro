from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>¿Quieres ser mi novia?</title>
            <style>
                body {
                    text-align: center;
                    font-family: Arial, sans-serif;
                    margin-top: 50px;
                }
                .button {
                    padding: 15px 30px;
                    font-size: 20px;
                    cursor: pointer;
                    border-radius: 5px;
                    border: 2px solid #4CAF50;
                    background-color: #f0f0f0;
                }
                .button:hover {
                    background-color: #ddd;
                }
                #noButton {
                    position: relative;
                }
            </style>
        </head>
        <body>
            <h1>¿Quieres ser mi novia?</h1>
            <button class="button" id="yesButton" onclick="yesResponse()">Sí</button>
            <button class="button" id="noButton" onclick="noResponse()">No</button>

            <script>
                function yesResponse() {
                    alert('¡Yo también! Jsjs');
                }

                function noResponse() {
                    var noButton = document.getElementById('noButton');
                    var randomX = Math.random() * 300;
                    var randomY = Math.random() * 200;
                    noButton.style.position = 'absolute';
                    noButton.style.left = randomX + 'px';
                    noButton.style.top = randomY + 'px';
                }
            </script>
        </body>
        </html>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    