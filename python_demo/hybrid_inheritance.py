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

class google():
    def __init__(self):
        print("welcome to google chrome")
    def google_account(self):
        print("you can login this account")
    def search_bar(self):
        print("you can search any webpages")
    def software(self):
        print("you can download multiple softwares")   
class email():
    
    def login(self):
        print("you can login gmail")
    def compose(self):
        print("you can compose and sent mail")
    def inbox(self):
        print("you can reciving the mail")
class browser(google,email):
    def __init__(self):
        super().__init__()
        super().google_account()
        super().search_bar()
        super().software()
        super().login()
        super().compose()
        super().inbox()

b=browser()
