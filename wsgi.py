#!/usr/bin/env python
# coding=utf-8
# author: xsl

import os
import leancloud

APP_ID = os.environ['LEANCLOUD_APP_ID'] 
APP_KEY = os.environ['LEANCLOUD_APP_KEY']
MASTER_KEY = os.environ['LEANCLOUD_APP_MASTER_KEY']

leancloud.init(APP_ID, app_key=APP_KEY, master_key=MASTER_KEY)
leancloud.use_master_key(False)

from app import app
from cloud import engine

app = engine.wrap(app)
application = app
