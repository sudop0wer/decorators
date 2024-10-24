
class User:

    all = {}

    def __init__(self, user_id, user_password, logged_in=False):
        self.user_id = user_id
        self.user_password = user_password
        User.all.setdefault(user_id, user_password)

    #def log_in(self, user_id, user_password):
    #    if all.get(f"{user_id}"):



# def requires_authentication(func):

user1 = User('alex', 'password123')
user2 = User('mark', 'cisco123!')
user3 = User('radu', 'danu')

print(User.all)