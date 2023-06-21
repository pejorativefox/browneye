
import logging
import subprocess


def run_process(command, log=None, env=None, expected_return=[0,], cwd=None):
    """Run a process using popen with optional logging and squelch.

    arguments
    ---------
    command:            a command to execute. Can be a string or list
                        (as per the submodule documentation)
    log:                instance of logging.log.
    env:                environment variables to include when running.
    expected_return:    A list of valid valid return values from the process.
    """
    # if we have a string spit it into a list
    if type(command) is str:
        command = command.split(' ')
    # if we dont have a log, we can just create one
    if not log:
        log = logging.getLogger(command[0])

    log_header = 'Running: "{}"'.format(' '.join(command))
    log.info(log_header)
    proc = subprocess.Popen(command, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, env=env, cwd=cwd)
    for line in proc.stdout:
        line = line.strip()
        # need to check if the line is blank. Some tools output blank lines we
        # dont need
        #if line is not b'':
        log.info(line.decode("utf-8"))
    proc.wait()

    log_footer = 'Finished. returncode: {}'.format(proc.returncode)
    log.info(log_footer)
    return proc.returncode

