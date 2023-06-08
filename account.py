ACCOUNT_FILE_NAME = "account.txt"


def read_user_account() -> list:
    try:
        with open(ACCOUNT_FILE_NAME, "r") as f:
            file_data = f.read()
            account = file_data.split(':')

            # Delete escape sequence
            # TODO: refactor in a function
            account = list(map(lambda x: "".join(
                [c for c in x if c.isalpha()]), account))
        return account
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    print(read_user_account())
