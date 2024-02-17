class google():
    def __init__(self):
        print("welcome to google chrome")
    def google_account(self):
        print("you can login this account")
    def search_bar(self):
        print("you can search any webpages")
class email(google):
    def login(self):
        print("you can login gmail")
    def compose(self):
        print("you can compose and sent mail")

e=email()
e.google_account()
e.search_bar()
e.login()
e.compose()