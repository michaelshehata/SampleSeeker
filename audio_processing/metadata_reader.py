from mutagen import File

def read_metadata(path):
    f = File(path, easy=True)
    tags = {
      'title': f.get('title', [None])[0],
      'artist': f.get('artist', [None])[0],
      'genre': f.get('genre', [None])[0],
      'year':  f.get('date',  [None])[0]
    }
    return tags
