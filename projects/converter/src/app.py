from flask import Flask
from api.routes.login import api as login_api

def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.dev_settings')
    app.register_blueprint(login_api, url_prefix='/api')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
