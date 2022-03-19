import os
import sys

# Link upper directory path for python module path. 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..' )))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))
