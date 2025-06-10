from flask import Flask
from flask_cors import CORS
from routes.candidate_routes import candidate_bp
from routes.jobroles_routes import jobrole_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(candidate_bp, url_prefix='/api')
app.register_blueprint(jobrole_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)