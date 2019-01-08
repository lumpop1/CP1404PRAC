class ProgrammingLanguage:
    def __init__(self,Typing='',Reflection='',Year=0):
        self.Typing = Typing
        self.Reflection=Reflection
        self.Year=Year

    def is_dynamic(self,Typing):
        Typing = False
        if Typing == 'Dynamic':
            return True
        else:
            return False

    def is_yes(self,Reflection):
        Reflection = False
        if Reflection == 'Yes':
            return True
        else:
            return False






