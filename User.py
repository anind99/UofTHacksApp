class User:

    def __init__(self, username, password):
        self.username = username    # Unique
        self.password = password
        self.features = []

    def __eq__(self, other):
        return self.username == other.username

    def __str__(self):
        print(f'Username: {self.username} \n features: {self.features} \n')