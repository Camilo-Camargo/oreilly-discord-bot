import re
import subprocess
import codecs
ACCOUNT_FILE_NAME = "account.txt"
DOCKER_OREILLY_TRIAL = "bilalcaliskan/oreilly-trial:latest"


def ansi_escape(text):
    # reference:
    # https://stackoverflow.com/questions/14693701/how-can-i-remove-the-ansi-escape-sequences-from-a-string-in-python
    pattern = re.compile(r'''
        \x1B  # ESC
        (?:   # 7-bit C1 Fe (except CSI)
            [@-Z\\-_]
        |     # or [ for CSI, followed by a control sequence
            \[
            [0-?]*  # Parameter bytes
            [ -/]*  # Intermediate bytes
            [@-~]   # Final byte
        )
    ''', re.VERBOSE)
    return pattern.sub('', text)


def read_user_account() -> list:
    try:
        with open(ACCOUNT_FILE_NAME, "r") as f:
            file_data = f.read()

        account = file_data.split(':')
        return account
    except FileNotFoundError:
        return []


def create_account() -> (str, str):
    output_docker_oreilly_trial = subprocess.run(
        f'docker run -i {DOCKER_OREILLY_TRIAL}',
        text=True,
        capture_output=True,
        shell=True,
    ).stdout

    output_docker_oreilly_trial = ansi_escape(output_docker_oreilly_trial)

    output_docker_oreilly_trial = output_docker_oreilly_trial.split('\n')
    account = output_docker_oreilly_trial[-2].split()[-2:]

    email = account[0].split('=')[-1]
    password = account[1].split('=')[-1]

    return (email, password)


def save_account(filename, account):
    with open(ACCOUNT_FILE_NAME, 'w') as f:
        f.write(f'{account[0]}:{account[1]}')


if __name__ == "__main__":
    account = read_user_account()
    if (len(account) == 0):
        new_account = create_account()
        save_account(new_account)
    print(account)
