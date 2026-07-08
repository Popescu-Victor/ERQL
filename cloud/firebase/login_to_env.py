import dotenv

# When using ERQL to scrape the same page on a regular basis it's better to have login details stored in an .env file instead of rewriting them every time.

def login_to_env(username, password):
    dotenv.set_key(".env", "ILIAS_USER", username)
    dotenv.set_key(".env", "ILIAS_PASSWORD", password)
    config = dotenv.dotenv_values(".env")
    print(config)
