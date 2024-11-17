import time
import webbrowser

from params import *


def auth_pylast(api_key, api_secret, username, password_hash) -> pylast.LastFMNetwork:
    network = pylast.LastFMNetwork(
        api_key=api_key,
        api_secret=api_secret,
        username=username,
        password_hash=password_hash,
    )
    if not os.path.exists(SESSION_KEY_FILE):
        skg = pylast.SessionKeyGenerator(network)
        url = skg.get_web_auth_url()

        print(f"Please authorize this script to access your account: {url}\n")
        webbrowser.open(url)

        while True:
            try:
                session_key = skg.get_web_auth_session_key(url)
                with open(SESSION_KEY_FILE, "w") as f:
                    f.write(session_key)
                break
            except pylast.WSError:
                time.sleep(1)
    else:
        session_key = open(SESSION_KEY_FILE).read()

    network.session_key = session_key
    return network


def get_lastfm_user_tracks():

    pass


if __name__ == '__main__':
    network = auth_pylast(API_KEY, API_SECRET, username, password_hash)

    get_lastfm_user_tracks()


