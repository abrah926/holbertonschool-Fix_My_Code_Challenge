from user import User  # Remember to rename `3-user.py` to `user.py` if not it wont run.

user = User()

print(f"User ID: {user.id}")
assert user.id is not None, "User ID should not be None"

password = "myPassword123"
user.password = password
print(f"Hashed Password: {user.password}")
assert user.password is not None, "Password should not be None"

assert user.is_valid_password(password), "Password validation failed"
assert not user.is_valid_password("wrongPassword"), "Password validation should fail for incorrect password"
