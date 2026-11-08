'''
    Glibs Python scripts base tools
'''
#!/usr/bin/python3
import os
import subprocess

def clear_console():
    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"], check=False)
    else:
        subprocess.run(["clear"], check=False)

def str2num(s: str, default=None):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return default

def try_parse_int(s: str, default=None):
    try:
        return int(s)
    except ValueError:
        return default

def try_parse_float(s: str, default=None):
    try:
        return float(s)
    except ValueError:
        return default

















