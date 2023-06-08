import subprocess
from account import read_user_account
PYTHON_BIN_PATH = "./.oreilly-discord-bot/bin/python"


def safaribook(email, password, bookid):
    command = f'{PYTHON_BIN_PATH} ./third_party/safaribooks/safaribooks.py'
    args = f"--cred '{email}':'{password}' {bookid}"

    print(f'{command} {args}')
    output_process = subprocess.run(f'{command} {args}', shell=True)
    print(output_process.stdout)


if __name__ == "__main__":
    [email, password] = read_user_account()
    print(email, password)
    safaribook(email, password, 9781789343625)
    print("Hello World")
