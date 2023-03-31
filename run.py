from app import create_app, db
from flask_migrate import Migrate
"""
Entrance of this web project
"""

app = create_app('development')

# -------- Remote Server Deployment Configuration -------- #
HOST = '0.0.0.0'
PORT = 8000
# LINK = 'http://180.76.106.26:5007'
# -------------------------------------------------------- #

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=False)



