from flask import Flask
import flaskcode

app = Flask(__name__)
app.config.from_object(flaskcode.default_config)
app.config['FLASKCODE_RESOURCE_BASEPATH'] = '/path/to/resource/folder'
app.register_blueprint(flaskcode.blueprint, url_prefix='/flaskcode')

@app.route('/')
def hello():
    render_template('code_editor.html')

if __name__ == '__main__':
    app.run()
