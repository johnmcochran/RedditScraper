import winreg
def get_environment_variables():
    environment_vars = {}

    try:
        user_key_path = r"Environment"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, user_key_path) as user_key:
            index = 0
            while True:
                try:
                    name, value, _ = winreg.EnumValue(user_key, index)
                    environment_vars[name] = value
                    index += 1
                except OSError:
                    break
    except Exception as e:
        print(f"Error accessing user environment variables: {e}")
    environment_vars = {k: v for k, v in environment_vars.items() if k in ('RedditScraperClientID', 'RedditScraperClientSecret')}
    return environment_vars

