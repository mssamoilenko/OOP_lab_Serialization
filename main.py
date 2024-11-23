import pickle
#task1
class UsersDict:
    def __init__(self):
        self.users_dict = {}

    def add_to_users_dict(self, key, value):
        if key in self.users_dict:
            print(f"Користувач з логіном '{key}' вже існує.")
        else:
            self.users_dict[key] = value
            print(f"Користувач '{key}' успішно доданий.")

    def del_users_dict(self, key, value):
        if key in self.users_dict:
            del self.users_dict[key]
            print(f"Користувач '{key}' успішно видалений.")
        else:
            print("Користувач не існує")

    def search_user(self, key):
        if key in self.users_dict:
            print(f"Користувача {key} знайдено! Пароль: {self.users_dict[key]}")
        else:
            print("Користувач не існує")

    def edit_user(self, key, new_value):
        if key in self.users_dict:
            self.users_dict[key] = new_value
            print(f"Пароль користувача '{key}' успішно змінено.")
        else:
            print("Користувач не існує")

    def save_data(self, filename):
        try:
            with open(filename, "wb") as file:
                pickle.dump(self.users_dict, file)
            print(f"Дані успішно збережені в файл {filename}")
        except pickle.PickleError as e:
            print(f"Помилка при серіалізації: {e}")

    def load_data(self, filename):
        try:
            with open(filename, "rb") as file:
                self.users_dict = pickle.load(file)
            print(f"Дані успішно завантажено з файлу {filename}")
        except pickle.UnpicklingError as e:
            print(f"Помилка при десеріалізації: {e}")
        except FileNotFoundError:
            print(f"Файл {filename} не знайдений")

users = UsersDict()
users.add_to_users_dict("user1", "password123")
users.add_to_users_dict("user2", "mypassword")
print(users.search_user("user1"))
users.edit_user("user1", "newpassword")
print(users.search_user("user1"))

users.save_data("list.pkl")
users.load_data("list.pkl")
ser_data = pickle.dumps(users.users_dict)
print(ser_data)
load_d = pickle.loads(ser_data)
print(load_d)

#task2
class UserSession:
    def __init__(self, user_id, auth_token):
        self.user_id = user_id
        self.auth_token = auth_token
        self.session_data = {}

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['auth_token']
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.auth_token = None
        print("Токен аутентифікації не був відновлений")

    def set_token(self, token):
        self.auth_token = token

    def get_token(self):
        return self.auth_token

    def __str__(self):
        return f"User ID: {self.user_id}, Auth Token: {self.auth_token}, Session Data: {self.session_data}"

session = UserSession("user123", "secure_token_abc123")
print("Before serialization:", session)
serialized_session = pickle.dumps(session)
loaded_session = pickle.loads(serialized_session)
print("After deserialization:", loaded_session)

