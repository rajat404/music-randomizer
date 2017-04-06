import os
import platform
import random

from kivy.app import App
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout


class MusicScreen(GridLayout):
    song_title = StringProperty('')

    def __init__(self, **kwargs):
        super(MusicScreen, self).__init__(**kwargs)
        self.song_list = []
        self.song_count = 0
        self.play_time = 5
        self.sound = None
        self.load_songs()

    def stop_song(self, dt):
        """
        Stop the current track, and play the next (random) song
        """
        self.sound.stop()
        self.play_song()

    def load_songs(self, *args, **kwargs):
        """
        Load songs from Music directory
        """
        current_platform = platform.system()
        if current_platform == 'Darwin':
            self.music_dir = '/Users/rajat404/Music'
        else:
            self.music_dir = '/sdcard/Music'
        music_files = os.listdir(self.music_dir)
        self.song_list = [x for x in music_files if x.endswith('mp3')]
        self.song_count = len(self.song_list)

    def get_length(self, dt):
        """
        Get the length of the current song,
        navigate to 1/3rd of the song's length and unmute.
        After playing for few seconds, move to next track.
        """
        new_length = int(self.sound.length/3.0)
        self.sound.seek(new_length)
        self.sound.volume = 1
        Clock.schedule_once(self.stop_song, self.play_time)

    def play_song(self, *args, **kwargs):
        """
        Get a random song, and play
        """
        self.song_title = self.song_list[random.randrange(0, self.song_count)]
        self.sound = SoundLoader.load('{}/{}'.format(self.music_dir, self.song_title))
        print('*'*100)
        print(self.song_title)
        if self.sound:
            # Mute the phone
            self.sound.volume = 0
            # Play the song, in order to get it's length
            self.sound.play()
            # There needs to be a lag to get the song length after playing
            Clock.schedule_once(self.get_length, 0.3)
        else:
            print('Sound not found')


class MusicRandomizer(App):
    pass


if __name__ == '__main__':
    MusicRandomizer().run()
