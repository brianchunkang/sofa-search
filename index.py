from flask import Flask, request
app = Flask(__name__, static_url_path='')

@app.route('/')
def static_page():
    return app.send_static_file('sofa.html')

if __name__ == '__main__':
    app.run()
