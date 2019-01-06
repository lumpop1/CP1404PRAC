# create your Song class in this file
class Song:
    # the constructor of song
    def __init__(self,title='',artist='',year=0,is_required = ''):
        self.title = title
        self.artist = artist
        self.year = year
        self.is_required = is_required

    # displaying song details in the status message
    def __str__(self):
        if self.is_required == 'n':
            self.is_required = 'learned'
            return 'You have learned {} by {} ({})'.format(self.title,self.artist,self,self.is_required)
        else:
            self.is_requiredc='y'
            return 'You have not learned {} by {} ({})'.format(self.title, self.artist,self.is_required)

    def add_learned(self):
        self.is_required = 'n'
        return self.is_required



