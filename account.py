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

            # Delete escape sequence
            # TODO: refactor in a function
            account = list(map(lambda x: "".join(
                [c for c in x if c.isalpha()]), account))
        return account
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    account = read_user_account()
    if (len(account) == 0):
        output_docker_oreilly_trial = subprocess.run(
            f'docker run -i {DOCKER_OREILLY_TRIAL}',
            text=True,
            capture_output=True,
            shell=True,
        ).stdout

        output_docker_oreilly_trial = ansi_escape(output_docker_oreilly_trial)

        # with open('output.txt', 'w') as f:
        #    f.write(output_docker_oreailly_trial.stdout)

        # with open('output.txt', 'r') as f:
        #    output_docker_oreilly_trial = ansi_escape(f.read())

        # save generated password and email
        output_docker_oreilly_trial = output_docker_oreilly_trial.split('\n')
        account = output_docker_oreilly_trial[-2].split()[-2:]

        email = account[0].split('=')[-1]
        password = account[1].split('=')[-1]

        with open(ACCOUNT_FILE_NAME, 'w') as f:
            f.write(f'{email}:{password}')
