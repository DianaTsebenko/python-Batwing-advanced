class UserDB:
    users = [{"name": "diana", "email": "diana@gmail.com", "password": "diana22"}]

    def get_all(self):
        return self.users

    def retrieve_by_email(self, email):
        for user in self.users:
            if user["email"] == email:
                return user
        return None

    def add(self, name, email, password_hash):
        user = {
            "name": name,
            "email": email,
            "password": password_hash
        }
        self.users.append(user)
        return user

    def update_by_email(self, email, name, password):
        # TODO: refactor
        for user in self.users:
            if user["email"] == email:
                user["name"] = name
                user["password"] = password
                return user
        return None

    def delete_by_email(self, email):
        self.users = [user for user in self.users if user["email"] != email]
