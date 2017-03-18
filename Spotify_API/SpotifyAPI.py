import spotipy
import spotipy.util as util
import pandas as pd
import csv

def create_client():
    username = 'hmwang'
    scope = 'user-library-read'
    client_id = '8c02fc8f22344a06b1f2ca8b61efef30'
    client_secret = 'ae68ed70bf7445578e3e9fbb224e2292'
    redirect_uri = 'http://localhost:8888/callback'

    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
    Client = spotipy.client.Spotify(auth=token)
    return Client

def get_playlist_info(playlist):
    owner_id = playlist['owner']['id']
    playlist_id = playlist['id']
    playlist_name = playlist['name']
    playlist_dict =  {'owner_id': owner_id, 'playlist_id': playlist_id, 'playlist_name': playlist_name}
    return playlist_dict

def get_track_info(tracks):
    return tracks['track']
#     album_id = track['album']['id']
#     track_dict = {'track_id': track_id, 'track_name': track_name, 'track_primary_artist': track_primary_artist, 'album_id': album_id}
#     return track_dict

def get_album_info(album_id):
    album_info = Client.album(album_id)
    album_info['album_name'] = album_info['name']
    album_info['album_id'] = album_info['id']
    del album_info['uri']
    del album_info['id']
    del album_info['name']
    return album_info

def get_audio_features(track_id):
    audio_features = Client.audio_features([track_id])[0]
    return audio_features

def get_playlist_res(playlist_info):
    res = Client.user_playlist(playlist_info['owner_id'], playlist_info['playlist_id'])
    return res

def get_tracks(playlist_res):
    tracks = playlist_res['tracks']['items']
    track_info = map(get_track_info, tracks)
    return track_info
Client = create_client()

playlists = (Client.featured_playlists(timestamp="2016-12-31T20:00:00"))
data_dict = {}

i = 0

playlist_items = playlists['playlists']['items']
playlist_info = map(get_playlist_info, playlist_items)
playlist_res = map(get_playlist_res, playlist_info)
track_info = map(get_tracks, playlist_res)

for tracks in track_info:
    print pd.DataFrame(tracks)


# for playlist in playlists['playlists']['items']:
#     playlist_dict = get_playlist_info(playlist)
#
#     playlist_res = Client.user_playlist(playlist_dict['owner_id'], playlist_dict['playlist_id'])
#     for track in playlist_res['tracks']['items']:
#         track_dict = get_track_info(track['track'])
#         album_info = get_album_info(track_dict['album_id'])
#         audio_features = get_audio_features(track_dict['track_id'])
#
#         for key in playlist_dict.keys():
#             if key in data_dict:
#                 data_dict[key].append(playlist_dict[key])
#             else:
#                 data_dict[key] = [playlist_dict[key]]
#
#         for key in album_info.keys():
#             if key in data_dict:
#                 data_dict[key].append(album_info[key])
#             else:
#                 data_dict[key] = [album_info[key]]
#
#         for key in track_dict.keys():
#             if key in data_dict:
#                 data_dict[key].append(track_dict[key])
#             else:
#                 data_dict[key] = [track_dict[key]]
#
#         for key in audio_features.keys():
#             if key in data_dict:
#                 data_dict[key].append(audio_features[key])
#             else:
#                 data_dict[key] = [audio_features[key]]
#
#         print "Song %s completed" % (i)
#         i += 1
#
# f = open('SpotifyData.csv','wb')
# w = csv.DictWriter(f, data_dict.keys())
# w.writerows(data_dict)
# f.close()







# print playlists['playlists']
# tracks = Client.search('Pitbull')['tracks']['items']
# for track in tracks:
#      pprint(track)
     # uri = track['uri']
     # pprint(Client.audio_features([uri]))
# track = '3T1CKrdMfrXJC5VXC19LUm'
# pprint(Spotify.audio_features([track]))
