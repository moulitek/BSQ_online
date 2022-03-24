import subprocess

def call_system(command: str, timeout: int = 60) -> int:
    """Call an external command

    `command` The external command

    `timeout` The timeout of the script

    Returns the exit status of the command, or 124 on timeout.
    """
    return subprocess.call("timeout %ds %s 1> /dev/null 2> /dev/null" % (timeout, command), shell=True)
