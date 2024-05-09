class User:
    def __init__(self,username):
       self.username = username
       self.user_id = None
    
class UserSystem:
    def ___init__(self):
        self.users=[]
        self.user_id =1

    def add_user(self,username):
        user = user(username)
        user.user_id= self.user_id
        self.user_id += 1
        self.users.append(user)
UserSystem = UserSystem()
UserSystem.add_user("Naserian")
UserSystem.add_user("Samuria")

print("username")
        