
class User:

    all = {}
    logged_in = False

    def __init__(self, user_id, user_password):
        self.user_id = user_id
        self.user_password = user_password
        User.all.setdefault(user_id, user_password)

    def log_in(self, user_id='', user_password=''):
        user_id = input("Type user ID: ")
        #if User.all.get(user_id) is None:
        if user_id != self.user_id:
            print("Wrong username")
        else:
            user_password = input("Type your password: ")
            if User.all[user_id] == user_password:
                print("Login successfully!")
                self.logged_in = True
            else:
                print("Wrong password! Retry")

    def log_out(self, user_id=''):
        self.logged_in = False


# def requires_authentication(func):

user1 = User('alex', 'password123')
user2 = User('mark', 'cisco123!')
user3 = User('radu', 'danu')


user1.log_in()
user1.log_out()


#print(user1.logged_in)
#print(f"User 1 logged in: {user1.logged_in}")
#print(f"User 2 logged in: {user2.logged_in}")
#print(f"User 3 logged in: {user3.logged_in}")
#print(User.all)