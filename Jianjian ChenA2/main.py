"""
Name: Chen Jianjian
Date:2018/1/06
Brief Project Description:
GitHub URL:
"""
from kivy.app import App
from kivy.lang import Builder
from Assignment2.songlist import SongList
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from Assignment2.song import Song
from kivy.uix.button import Button


# Create your main program in this file, using the LearnSongsApp class

class LearnSongsApp(App):
    """
        Main program: show the list of songs by GUI
        """
    status_text = StringProperty()  # the first status text
    status_text2 = StringProperty()  # the second status text
    current_sort = StringProperty()  # the current sorting of song list
    sort_choices = ListProperty()  # the sorting options of song list

    def __init__(self, **kwargs):

        super(LearnSongsApp, self).__init__(**kwargs)
        self.song_list = SongList()
        self.sort_choices = ["year", "artist"]
        self.current_sort = self.sort_choices[0]
        self.song_list.load_songs()

    def build(self):
        """
        Build the Kivy GUI
        """
        self.learn___ = "Songs to learn 2.0 by Chen Jianjian"  # Name the GUI's name
        self.title = self.learn___
        self.root = Builder.load_file('app.kv')  # Connect to Kivy app
        self.create_widgets()  # Create the songs button
        return self.root

    def change_sort(self, sorting_choice):
        """
        change the sorting of the song list

        """
        self.status_text = "Sorted by: {}".format(sorting_choice)
        self.song_list.sort(sorting_choice)
        self.root.ids.entriesBox.clear_widgets()
        self.create_widgets()
        sort_index = self.sort_choices.index(sorting_choice)
        self.current_sort = self.sort_choices[sort_index]

    def create_widgets(self):
        """
        Create Songs' buttons from the csv file

        """
        num_song = len(self.song_list.list_songs)  # Count the number of songs
        learned_song = 0
        for song in self.song_list.list_songs:  # find the songs
            name = self.button_Text(song.title, song.artist, song.year,song.is_required)  # showing the information in be the button)
            learned = song.is_required
            if learned == 'n':
                background_color = (1, 2, 1, 0.7)#if the song id learned show this color
                learned_song += 1
            else:
                # If the song is not learned show blue color
                background_color = (1, 3, 4, 0.6)
            # clicking a song to learn
            temp_button = Button(text=name, id=str(song.title),background_color=background_color)  # Add the song learned
            temp_button.bind(on_release=self.press_song)  # show the message of the status
            self.root.ids.entriesBox.add_widget(temp_button)  # add the song to the Kivy app
        self.status_text = 'To Learned: {}  Learned: {}'.format(num_song-learned_song,learned_song)

    def button_Text(self, title, artist, year, learned):  # show  messages
        if learned == "n":
            display_text = "{} by {} {} (Learned)".format(title,artist,year)
        else:
            display_text = "{} by {} {}".format(title,artist,year)

        return display_text

    def press_song(self, button):  # when you press the song button
        buttonText = button.text  # Determine the text on the buttons
        selectedSong = Song()
        for song in self.song_list.list_songs:
            songDisplayText = self.button_Text(song.title, song.artist, song.year, song.is_required)
            # show text in Button
            if buttonText == songDisplayText:
                selectedSong = song
                break

        selectedSong.add_learned()
        self.root.ids.entriesBox.clear_widgets()  # Apply to Kivy
        self.create_widgets()

        self.status_text2 = "You have learned {}".format(selectedSong.title)  # Display the status text 2

    def add_songs(self):
        """
        add a song to learn
        """

        # Check if have empty inputs
        if self.root.ids.song_title.text == "" or self.root.ids.song_artist.text == "" or self.root.ids.song_year.text == "":
            self.root.ids.status2.text = "All fields must be completed"
            return
        try:
            # Define song items inputted
            song_title = str(self.root.ids.song_title.text)
            song_artist = str(self.root.ids.song_artist.text)
            song_year = int(self.root.ids.song_year.text)
            is_required = "y"

            # Add the song to the song list
            self.song_list.add_to_list(song_title, song_artist, song_year, is_required)
            temp_button = Button(text=self.button_Text(song_title, song_artist, song_year, is_required))
            temp_button.bind(on_release=self.press_song)

            # the new song button color
            temp_button.background_color = (1, 3, 4, 0.6)
            self.root.ids.entriesBox.add_widget(temp_button)

            # empty inputs
            self.root.ids.song_title.text = ""
            self.root.ids.song_artist.text = ""
            self.root.ids.song_year.text = ""

        except ValueError:  # Display error when year input is not a number
            self.status_text2 = "Please enter a valid year"
        self.song_list.save_songs()

    def press_clear(self):
        """
        Clear status text and inputs

        """
        self.status_text = ""  # Clear status_text
        self.status_text2 = ""  # Clear status_text2
        self.root.ids.song_title.text = ''  # Clear title input
        self.root.ids.song_artist.text = ''  # Clear artist input
        self.root.ids.song_year.text = ''  # Clear year input


LearnSongsApp().run()
