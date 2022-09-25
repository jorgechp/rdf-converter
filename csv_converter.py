import subprocess


def convert(input_file: str, query_file: str, is_tab: bool = False) -> bytes:
    arguments = ['tarql-1.2/bin/tarql']
    if is_tab:
        arguments.append('--tabs')
    arguments.extend([query_file, input_file])
    command = ' '.join(arguments)
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if not err:
        return out
    else:
        raise InterruptedError(err)
