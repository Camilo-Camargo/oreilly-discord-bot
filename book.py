import subprocess
from account import read_user_account
from account import create_account
PYTHON_BIN_PATH = "./.oreilly-discord-bot/bin/python"


async def safaribook(bookid):

    account = read_user_account()
    if (account == []):
        account = create_account

    [email, password] = account

    command = f'{PYTHON_BIN_PATH} ./third_party/safaribooks/safaribooks.py'
    args = f"--cred '{email}':'{password}' {bookid}"

    output_process = subprocess.run(f'{command} {args}',
                                    shell=True,
                                    capture_output=True,
                                    text=True
                                    ).stdout

    output_path = output_process[
        output_process.find('Done:'):-1
    ].split('\n')[0]

    return output_path.replace('Done:', '')[1:].strip()


if __name__ == "__main__":
    [email, password] = read_user_account()
    print(safaribook(email, password, 9781789343625))
