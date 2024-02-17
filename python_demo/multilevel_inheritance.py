class google():
    def __init__(self):
        print("welcome to  google chrome")
    def search_bar(self):
        print("you can search all")
    def gmail(self):
        print("you can access gmail")
    def yahoo(self):
        print("you can access yahoo")
class gmail(google):
    def __init__(self):
        print("we are using gmail for mail")
    def inbox(self):
        print("i can sent  and receive mails")
    def compose(self):
        print("i can sent email")
class I_explorar(gmail):
    def __init__(self):
        pass
class social_media(I_explorar):
    def __init__(self):
        print("i can access all social media web pages")
        super().__init__()
        super().search_bar()
        super().gmail()
        super().yahoo()
        super().inbox()
        super().compose()
s=social_media()
