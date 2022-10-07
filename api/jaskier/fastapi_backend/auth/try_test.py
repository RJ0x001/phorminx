# Python program to explain os.environ object

# importing os module
import os
from dotenv import load_dotenv
import pprint

load_dotenv('../../../.env')
# Get the list of user's
# environment variables
env_var = os.getenv("SECRET_KEY")

# Print the list of user's
# environment variables
print("User's Environment variable:")
print(env_var)
