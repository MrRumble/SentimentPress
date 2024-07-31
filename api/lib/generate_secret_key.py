import secrets
import string


def generate_secret_key(length=32):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    my_secret_key = ''.join(secrets.choice(alphabet) for _ in range(length))
    return my_secret_key


# Generate a 32-character secret key
secret_key = generate_secret_key()
print(f"Your new secret key is: {secret_key}")
print("Make sure to save this securely and don't share it!")
