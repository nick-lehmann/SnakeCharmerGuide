from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/people')
def people():
    return """
    <html>
    <body>
        <h1>People</h1>
        <ul id="list">
            <li class="person">
                Lisa, 17
            </li>
            <li class="person">
                Frank, 21
            </li>
            <li class="person">
                Berta, 25
            </li>
        </ul>
    </body>
    </html>
    """


app.run()
