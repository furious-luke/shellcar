import subprocess
import shlex


def run_command_3_7(command):
    print(f'Running command: {command}')
    try:
        stdout = subprocess.check_output(shlex.split(command))
        print('Stdout: ')
        print(stdout)
        return {
            'ec': 0,
            'stdout': stdout
        }
    except subprocess.CalledProcessError as e:
        print('Errored: ')
        print(e.output)
        return {
            'ec': e.returncode,
            'stdout': e.output
        }


def run_command_3_8(command):
    result = subprocess.run(shlex.split(command), capture_output=True)
    return {
        'ec': result.returncode,
        'stdout': result.stdout,
        'stderr': result.stderr
    }


run_command = run_command_3_7
