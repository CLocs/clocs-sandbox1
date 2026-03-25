import os
import pylast

API_KEY = "6a5a0634ab240616da562d497658060e"
API_SECRET = "82f9fc14ebf1ade19ff1eb64dbaa7729"
USER_AGENT = 'music_trip_tracker'
SESSION_KEY_FILE = os.path.join(os.path.expanduser("~"), ".session_key")

username = "clocs0"
password_hash = pylast.md5("Lcr3gg!e")

headers_default = {
    'user-agent': USER_AGENT
}
payload_default = {
    'api_key': API_KEY,
    'method': 'chart.gettopartists',
    'format': 'json'
}
