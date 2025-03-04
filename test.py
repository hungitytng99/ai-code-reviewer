import json

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}"

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                file.write(json.dumps(self.__dict__))
                print("User data saved successfully")
        except:
            print("Error saving user data")

def load_user_from_file(filename):
    try:
        file = open(filename, 'r')
        data = json.loads(file.read())
        file.close()
        return User(data['name'], data['age'], data['email'])
    except:
        print("Error loading user data")
        return None

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    return result

def main():
    user1 = User("Alice", 25, "alice@example.com")
    print(user1.get_details())

    user1.save_to_file("user_data.json")

    user2 = load_user_from_file("user_data.json")
    print(user2.get_details())

    print(divide_numbers(10, 0))

if __name__ == "__main__":
    main()
