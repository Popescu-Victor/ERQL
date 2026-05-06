import dotenv



def login_to_env(username, password):
    dotenv.set_key(".env", "ILIAS_USER", username)
    dotenv.set_key(".env", "ILIAS_PASSWORD", password)
    config = dotenv.dotenv_values(".env")
    print(config)
