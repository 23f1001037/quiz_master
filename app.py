from flask import Flask, jsonify
import traceback
from config import Config  # Import the Config class
from routes import routes_bp  # Import the Blueprint

app = Flask(__name__)

# Apply Configuration
app.config.from_object(Config)

# Register Blueprint
app.register_blueprint(routes_bp)

# Import models inside app context
with app.app_context():
    import models  # Ensures database is initialized properly

# Error Handling for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    print(traceback.format_exc())  # Log full traceback for debugging
    return jsonify({"error": "Internal Server Error"}), 500  # Return JSON response

if __name__ == '__main__':
    app.run(debug=True)
