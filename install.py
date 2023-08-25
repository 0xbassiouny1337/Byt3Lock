import subprocess

required_libraries = [
    "keyboard",
    "ctypes",
    "platform",
    "getpass",
    "os",
    "sys"
]

def is_library_installed(library_name):
    try:
        __import__(library_name)
        return True
    except ImportError:
        return False

def install_library(library_name):
    try:
        subprocess.check_call(["pip", "install", library_name])
        print(f"Installed {library_name} successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to install {library_name}.")

def main():
    for library in required_libraries:
        if not is_library_installed(library):
            install_library(library)

    tkinter_required_libraries = [
        "tkinter",
        "tkinter.messagebox",
        "functools",
    ]

    for library in tkinter_required_libraries:
        if not is_library_installed(library):
            install_library(library)

    try:
        import keyboard
    except ImportError:
        install_library("keyboard")

if __name__ == "__main__":
    main()
