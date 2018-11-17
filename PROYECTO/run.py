#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

from app import app
app.run(debug=True, port = 16066,host = '0.0.0.0')
