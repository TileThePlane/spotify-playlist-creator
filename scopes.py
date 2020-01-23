from collections import namedtuple
from re import search
import praw
from keys import reddit_keys

_Spotify_Scopes = namedtuple('_Spotify_Scopes', (
        'gc_image_upload'
        'user_read_playback_state'
        'streaming'
        'user_read_email'
        'playlist_read_collaborative'
        'user_modify_playback_state'
        'user_read_private'
        'playlist_modify_public'
        'user_library_modify'
        'user_top_read'
        'user_read_currently_playing'
        'playlist_read_private'
        'user_follow_read'
        'app_remote_control'
        'user_read_recently_played'
        'playlist_modify_private'
        'user_follow_modify'
        'user_library_read'
    )
)

spotify_scopes = _Spotify_Scopes(
    'ugc-image-upload'
    'user-read-playback-state'
    'streaming'
    'user-read-email'
    'playlist-read-collaborative'
    'user-modify-playback-state'
    'user-read-private'
    'playlist-modify-public'
    'user-library-modify'
    'user-top-read'
    'user-read-currently-playing'
    'playlist-read-private'
    'user-follow-read'
    'app-remote-control'
    'user-read-recently-played'
    'playlist-modify-private'
    'user-follow-modify'
    'user-library-read'
)

_Reddit_Scopes = namedtuple('_Spotify_Scopes', (
        'identity',
        'edit',
        'flair',
        'history',
        'modconfig',
        'modflair',
        'modlog',
        'modposts',
        'modwiki',
        'mysubreddits',
        'privatemessages',
        'read',
        'report',
        'save',
        'submit',
        'subscribe',
        'vote',
        'wikiedit',
        'wikiread'
    )
)

reddit_scopes = _Reddit_Scopes(
    'identity',
    'edit',
    'flair',
    'history',
    'modconfig',
    'modflair',
    'modlog',
    'modposts',
    'modwiki',
    'mysubreddits',
    'privatemessages',
    'read',
    'report',
    'save',
    'submit',
    'subscribe',
    'vote',
    'wikiedit',
    'wikiread'
)
