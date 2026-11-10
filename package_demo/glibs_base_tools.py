'''
    Glibs Python scripts base tools
'''
#!/usr/bin/python3
import json
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

class ApplicationConfig:
    def __init__(self, config_file_path: str):
        self.config_file_path = config_file_path
        self.config_data = {}
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file_path):
            with open(self.config_file_path, 'r', encoding='utf-8') as f:
                try:
                    self.config_data = json.load(f)
                except json.JSONDecodeError:
                    print(f"Error: Failed to parse JSON from {self.config_file_path}. Using empty config.")
                    self.config_data = {}
        else:
            print(f"Warning: Config file {self.config_file_path} does not exist. Using empty config.")
            self.config_data = {}

    def get(self, key: str, default=None):
        return self.config_data.get(key, default)

    def set(self, key: str, value):
        self.config_data[key] = value
        self.save_config()

    def save_config(self):
        with open(self.config_file_path, 'w', encoding='utf-8') as f:
            json.dump(self.config_data, f, ensure_ascii=False, indent=4)















