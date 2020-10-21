from src.manager import create_app

flask_app = create_app(__name__)
flask_app.run(host='0.0.0.0', port=5000)
