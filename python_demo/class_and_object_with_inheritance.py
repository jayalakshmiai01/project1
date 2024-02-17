class grandparents():
    def __init__(self,grandpaname,grandmaname,familyname):
        self.grandfathername=grandpaname
        self.grandmothername=grandmaname
        self.familyname=familyname
    def welcome(self):
        print("welcome to",self.familyname,"wishes from",self.grandfathername,"and",self.grandmothername)
x=grandparents("raju","savithri","RS")


class geetha(grandparents):
    def __init__(self,grandpaname,grandmaname,familyname,fathername,mothername):
        self.fathername=fathername
        self.mothername=mothername
        super(). __init__ (grandpaname,grandmaname,familyname)
    def thanks(self):
        print("hi.......! grandpa",self.grandfathername,"and",self.grandmothername,"we",self.fathername,"and",self.mothername,"thankyou for warm welcome to our",self.familyname,"familly")
x=geetha("raju","savithri","RS","geetha","xxx")


class akila(geetha):
    def __init__(self,grandpaname,grandmaname,familyname,fathername,mothername,adhvithmother,adhvithfather):
        self.adhvithmothername=adhvithmother
        self.advithfathername=adhvithfather
        super(). __init__(grandpaname,grandmaname,familyname,fathername,mothername)
    def its_my_pleasure(self):
        print("hi..........! grandpa",self.grandfathername,"and",self.grandmothername,"we",self.fathername,"and",self.mothername,"thankyou for warm welcome to our",self.familyname,"familly",self.adhvithmothername,"and",self.advithfathername,"it's my pleaseure")
x=akila("raju","savithri","RS","geetha","xxx","akila","vignesh")

x.welcome()
x.thanks()
x.its_my_pleasure()