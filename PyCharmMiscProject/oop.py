# OOP
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def sign_in(self):
        print(f"email: {self.email}, password: {self.password}")


class PlayerCharacter(User):
    attack = True

    def __init__(self, email, password, name, age=0):
        super().__init__(email, password)
        self.name = name
        self.age = age

    def run(self):
        return "run {}, run".format(self.name)

    def sign_in(self):
        print(f"User: {self.name}, email: {self.email}, password: {self.password}")

    @classmethod
    def create_player_with_age(cls, email, password, name, birth_date):
        # calulate the age based on birth_date
        age = 23
        return cls(email, password, name, age)

    @staticmethod
    def calculate_age(name, birtDate):
        pass


user_list = []

player1 = PlayerCharacter("cindy@ci.com", "ci_pass", "Cindy")
user_list.append(player1)
print(player1.run())

player2 = PlayerCharacter("tom@to.com", "to_ass_tom", "Tom")
player2.speed = 20
user_list.append(player2)
print(f"{player2.run()} at {player2.speed} km/h.")

print(PlayerCharacter.attack)

player3 = PlayerCharacter.create_player_with_age("bobo@bobo.com", "boooooopass", "Bob", "1984-03-16")
user_list.append(player3)
print(player3.run())

user = User("olaf@abc.com", "paassswwoord")
user_list.append(user)

for us in user_list:
    us.sign_in()

# print(help(player1))
print(dir(player1))
