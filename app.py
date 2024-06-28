from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return f'''
    <h3>Hello, Flask! From <i style="font-weight: bolder; color: red;">{os.uname().nodename}</i></h3>
    '''

@app.route('/about')
def about():
    return 'About Page'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
