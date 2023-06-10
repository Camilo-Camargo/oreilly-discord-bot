import subprocess
import asyncio
from account import read_user_account
from account import create_account
PYTHON_BIN_PATH = "./.oreilly-discord-bot/bin/python"


async def safaribook(msg, bookid):

    account = read_user_account()
    if (account == []):
        account = create_account

    [email, password] = account

    command = f'{PYTHON_BIN_PATH} ./third_party/safaribooks/safaribooks.py'
    args = f"--cred '{email}':'{password}' {bookid}"

    process = await asyncio.create_subprocess_shell(
        f'{command} {args}',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    while process.returncode is None:
        for i in range(1, 10):
            await msg.edit(content=f'Retrieving {"."*i}')
            await asyncio.sleep(0.1)
        await asyncio.sleep(1)

    output_process, stderr = await process.communicate()

    output_path = output_process[
        output_process.find('Done:'):-1
    ].split('\n')[0]

    return output_path.replace('Done:', '')[1:].strip()


if __name__ == "__main__":
    [email, password] = read_user_account()
    print(safaribook(email, password, 9781789343625))
