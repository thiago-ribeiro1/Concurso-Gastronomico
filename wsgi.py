import sys
import os
from website import create_app

sys.path.insert(0, os.path.dirname(__file__))

app = create_app()
