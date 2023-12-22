import pkg.bootstrapper.bootstrapper as bootstrapper
import pkg.server.server as server
import dotenv

import os


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
app = server.initialize_flask_app()
dotenv.load_dotenv()

bootstrapper.initialize_routes(app)


if __name__ == "__main__":
    app.config['JSON_SORT_KEYS'] = False
    app.run(port="8181")