import os

PATH = [
    '/usr/bin',
    '/usr/local/bin',
    '/bin',
    '/usr/sbin',
    '/usr/local/sbin',
    '/sbin',
]

def choose_python():
    py = ''
    for b in PATH:
        p = os.path.join(b, 'python3')
        if os.path.exists(p):
            py = p
            print(p)
            break
    if not py:
        print(None)

choose_python()
