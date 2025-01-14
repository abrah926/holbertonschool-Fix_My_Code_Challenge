from user import User  # Assuming you rename `3-user.py` to `user.py`

# Create a new user
user = User()

# Test ID generation
print(f"User ID: {user.id}")
assert user.id is not None, "User ID should not be None"

# Test password setting and hashing
password = "myPassword123"
user.password = password
print(f"Hashed Password: {user.password}")
assert user.password is not None, "Password should not be None"

# Validate password
assert user.is_valid_password(password), "Password validation failed"
assert not user.is_valid_password("wrongPassword"), "Password validation should fail for incorrect password"
