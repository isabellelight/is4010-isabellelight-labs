
users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False},
]


def calculate_average_age(users):
   
    total_age = 0
    count = 0

    try:
        for user in users:
            age = user.get("age")
            if isinstance(age, int):
                total_age += age
                count += 1

        if count == 0:
            print("error: cannot calculate average age of an empty list.")
            return 0.0

        return total_age / count

    except TypeError:
        print("error: invalid data type in users list.")
        return 0.0


def get_active_user_emails(users):
 
    emails = []

    try:
        for user in users:
            if user.get("is_active") and user.get("email"):
                emails.append(user.get("email"))

        return emails

    except (TypeError, KeyError):
        print("error: invalid user data.")
        return []


if __name__ == "__main__":
    avg_age = calculate_average_age(users)
    print(f"average user age: {avg_age:.2f}")

    active_emails = get_active_user_emails(users)
    print(f"active user emails: {active_emails}")