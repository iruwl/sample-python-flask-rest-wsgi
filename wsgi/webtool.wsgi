activate_this = '/home/irul/htdocs/piton/flask/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, '/home/irul/htdocs/piton')
from webtool import app as application

#disable print error which is causing app stopped
sys.stdout = sys.stderr
