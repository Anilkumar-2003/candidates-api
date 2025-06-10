from flask import Flask
from flask_cors import CORS
import os
from flask_session import Session
from routes.candidate_routes import candidate_bp
from routes.jobrole_routes import jobrole_bp

app = Flask(__name__)
CORS(app, supports_credentials=True)  # Allow session cookies

# Session Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(24))
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
Session(app)

# Register Blueprints
app.register_blueprint(candidate_bp, url_prefix='/api')
app.register_blueprint(jobrole_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
