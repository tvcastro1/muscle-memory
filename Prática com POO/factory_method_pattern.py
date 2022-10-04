# In serializer_demo.py

import json
import xml.etree.ElementTree as et


class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:
    # Implementação sem interface
    # def serialize(self, song, format):
    #     if format == 'JSON':
    #         song_info = {
    #             'id': song.song_id,
    #             'title': song.title,
    #             'artist': song.artist
    #         }
    #         return json.dumps(song_info)
    #     elif format == 'XML':
    #         song_info = et.Element('song', attrib={'id': song.song_id})
    #         title = et.SubElement(song_info, 'title')
    #         title.text = song.title
    #         artist = et.SubElement(song_info, 'artist')
    #         artist.text = song.artist
    #         return et.tostring(song_info, encoding='unicode')
    #     else:
    #         raise ValueError(format)

    # Código Refatorado para implementar interface de serialização. O código fica mais "limpo" e inteligível.
    def serialize(self, song, format):
        if format == 'JSON':
            return self._serialize_to_json(song)
        elif format == 'XML':
            return self._serialize_to_xml(song)
        else:
            raise ValueError(format)

    def _serialize_to_json(self, song):
        payload = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(payload)

    def _serialize_to_xml(self, song):
        song_element = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_element, 'title')
        title.text = song.title
        artist = et.SubElement(song_element, 'artist')
        artist.text = song.artist
        return et.tostring(song_element, encoding='unicode')


song = Song('1', 'Water of Love', 'Dire Straits')
serializer = SongSerializer()

print(serializer.serialize(song, 'JSON'))

print(serializer.serialize(song, 'XML'))
