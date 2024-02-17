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
