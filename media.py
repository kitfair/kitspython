import webbrowser

#import fresh_tomatoes

class Movie:

    def __init__(self, title, storyline, poster_image, trailer_youtube_url):

        self._title = title
        self._poster_image_url = poster_image
        self._storyline = storyline
        self._trailer_youtube_url = trailer_youtube_url



    def title(self):
        pass
    def storyline(self):
        pass
    def poster_image(self):
        pass
    def trailer_youtube_url(self):
        pass
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url())



def main():
    toy_story = Movie("Toy Story", "Toys that come to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://youtu.be/KYz2wyBy3kc")
    toy_story.show_trailer()

if __name__ == '__main__':
    main()
    exit(0)