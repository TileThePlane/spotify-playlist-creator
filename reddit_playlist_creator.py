import praw
import spotipy
from keys import spotify_keys, reddit_keys
from scopes import reddit_scopes, spotify_scopes
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.util import prompt_for_user_token

#sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
#    client_id=keys['client_id'], client_secret=keys['client_secret']
#))

sp = prompt_for_user_token(username="kvonderw@uci.edu",
                            scope=spotify_scopes.playlist_modify_public,
                            client_id=spotify_scopes.client_id,
                            client_secret=spotify_scopes.client_secret,
                            redirect_uri='http://127.0.0.1:8080'
                           )


results = sp.user_playlist_create(spotipy.search(q='weezer', limit=20))

for i, t in enumerate(results['tracks']['items']):
    print(" ", i, t['name'])
