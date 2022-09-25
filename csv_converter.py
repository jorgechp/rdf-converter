import subprocess


def convert(input_file: str, query_file: str) -> bytes:
    arguments = ['tarql-1.2/bin/tarql', query_file, input_file]
    command = ' '.join(arguments)
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if not err:
        return out
    else:
        raise InterruptedError(err)
