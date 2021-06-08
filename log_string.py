import paramiko
import logging
from io import StringIO

# create logger
paramiko_logger = paramiko.util.logging.getLogger()
paramiko_logger.setLevel(logging.DEBUG)

# create handler with StringIO object
log_string = StringIO()
ch = logging.StreamHandler(log_string)
ch.setLevel(logging.DEBUG)

# add handler to logger
paramiko_logger.addHandler(ch)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.load_host_keys('/home/melissali/.ssh/known_hosts')
client.load_system_host_keys()

try:
    client.connect('192.168.2.249', username='melissali', key_filename='/home/melissali/.ssh/id_rsa')
except paramiko.ssh_exception.AuthenticationException as e:
    client.close()
    print(e)
except OSError as e:
    client.close()
    print(e)

# remove handler from logger to stop future log records from being sent to it
paramiko_logger.removeHandler(ch)

# StringIO.getvalue() retrieves entire content of file
log_content = log_string.getvalue()

log_string.flush()
# log_string.close()

print(log_content)
# print(log_string.closed)