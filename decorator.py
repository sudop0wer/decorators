
class User:

    all = {}
    logged_in = False

    def __init__(self, user_id, user_password):
        self.user_id = user_id
        self.user_password = user_password
        User.all.setdefault(user_id, user_password)

    def log_in(self):
        user_id = input("Type user ID(username): ")
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

    def log_out(self):
        self.logged_in = False
        print("Logged out successfully! ")


def requires_authentication(func):
    def checks_auth(user, *args, **kwargs):
        if user.logged_in:
            return func(user, *args, **kwargs)
        else:
            print("Error! User must be authenticated to perform this action.")
    return checks_auth

@requires_authentication
def post_message(user):
    message = input("What message do you want to post? ")
    print(f"Message posted: {message}")

@requires_authentication
def view_profile(user):
    profile = input("What profile do you want to see? ")
    if User.all.get(profile) is None:
        print("Profile not found")
    else:
        print(f"User {profile} has the password {User.all[profile]}")

def browse_public_feed(user):
    if not user.logged_in:
        print("You are not currently login in, but you can still browse the feed.")

    print("Why look at others when you are the best? ")

# Test Users
user1 = User('alex', 'password123')
user2 = User('mark', 'cisco123!')
user3 = User('radu', 'danu')

user1.log_in()
#user1.log_out()

post_message(user1)
post_message(user2)

view_profile(user1)
view_profile(user2)

#browse_public_feed(user1)
browse_public_feed(user2)


