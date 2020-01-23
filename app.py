from flask import Flask, flash
import praw
from prawcore import exceptions
import spotipy
from keys import spotify_keys, reddit_keys
from scopes import scopes
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.util import prompt_for_user_token
from re import search

app = Flask(__name__)

@app.route("/build-playlist/<url>")
def build_playlist(url):
    reddit_client = praw.Reddit(client_id=reddit_keys.client_id,
                                client_secret=reddit_keys.client_secret,
                                user_agent='spotify-playlist-creator, /u/updateseason'
                                )
    sub_match = search(r'(?<=/r/)\w{0,20}', 'reddit.com/r/reno')
    if sub_match:
        subreddit = reddit_client.subreddit(sub_match.match(0).replace('/', ''))
    else:
        flash('{} does not appear to be a valid subreddit url'.format(url))
    try:
        subreddit.created_utc
    except exceptions.Redirect:
        flash("We couldn't find/r/{}".format(sub_match))

    flash(subreddit.hot())

    # sp = prompt_for_user_token(username="kvonderw@uci.edu",
    #                            scope=scopes.playlist_modify_public,
    #                            client_id=spotify_keys.client_id,
    #                            client_secret=spotify_keys.client_secret,
    #                            redirect_uri='http://127.0.0.1:8080'
    #                            )
    #
    # results = sp.user_playlist_create(spotipy.search(q='weezer', limit=20))
    #
    # for i, t in enumerate(results['tracks']['items']):
    #     print(" ", i, t['name'])

if __name__ == "__main__":
    app.run()
