from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import threading
import argparse
import urllib.parse as urlparse

import pandas as pd
import networkx as nx
from perceval.backends.core import mbox as percMBOX

import json
import os

from datetime import datetime
import urllib
import logging
logging.getLogger(percMBOX.__name__).setLevel(logging.ERROR)


perceval = percMBOX.MBox('https://groups.google.com/d/forum/repo-discuss', 'Mbox')
issues = perceval.fetch(from_date=datetime(2018,5,30))
print(issues)
for item in issues:
    print(item['data'])
