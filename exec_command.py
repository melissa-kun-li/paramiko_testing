import paramiko
from contextlib import contextmanager

@contextmanager
def connection(addr):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(addr, username='melissali', key_filename='/home/melissali/.ssh/id_rsa')
    yield client

def run():
    with connection('192.168.2.249') as conn:
        file_transfer(conn)
        cmd = 'cd /tmp; python3 remotes.py'
        execute_command(conn, cmd)

def execute_command(conn, cmd, stdin=""):
    _stdin, _stdout, _stderr = conn.exec_command(cmd)
    if stdin:
        _stdin.write(stdin)
        _stdin.flush()
        _stdin.channel.shutdown_write()
    out = ''
    for line in _stdout:
        out += line
    # print(type(out))
    print(out)
    err = ''
    for line in _stderr:
        err += line
    # print(err)
    code = _stdout.channel.recv_exit_status()
    print(code)

def file_transfer(conn):
    sftp_client = conn.open_sftp()
    sftp_client.put('/home/melissali/Downloads/remotes.py', '/tmp/remotes.py')

run()