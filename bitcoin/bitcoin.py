import requests
import sys

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("u trash")

try:
    r = requests.get()
except requests.RequestException:

