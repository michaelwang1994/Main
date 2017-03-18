import spotipy

urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
sp = spotipy.Spotify()

sp.trace = True # turn on tracing
sp.trace_out = True # turn on trace out

artist = sp.artist(urn)
print(artist)

user = sp.user('plamere')
print(user)