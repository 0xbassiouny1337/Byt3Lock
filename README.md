# Byt3Lock - Ransomware Awareness Demonstration

## Description
Byt3Lock is a Python script designed to simulate a ransomware-like lock screen, created solely for educational purposes to raise awareness about cybersecurity threats. It should only be used with proper authorization and ethical considerations.

## Features
- **Realistic Lock Screen Simulation:** Byt3Lock creates a graphical user interface (GUI) using the tkinter library, displaying a lock screen with labels and buttons, closely resembling a system lock.
  
- **Password-Protected Unlock Mechanism:** Users must enter a password to unlock the program. The password is hardcoded as "123" in the script for demonstration purposes, but it is not secure and should not be used in any production environment.

- **Limited Login Attempts:** Byt3Lock allows a limited number of password attempts (default: 4). After exceeding this limit, it displays a warning message and takes different actions based on the operating system:
  - On Windows, it attempts to trigger the Blue Screen of Death (BSOD).
  - On Linux, it simulates a kernel panic.

- **Background Key Press Suppression:** The script uses the keyboard library to suppress keyboard events, making it difficult for users to interact with the system outside the program.

- **Startup Configuration:** Byt3Lock has functionality to add itself to the startup programs so that it runs automatically when the system boots up. This feature should be used responsibly and only with proper authorization.

- **Full-Screen Mode:** It runs in full-screen mode, hiding the rest of the desktop for a more immersive experience.

- **Uninstall Function:** The script provides a function to remove itself from startup programs and clean up when the user successfully unlocks the program.

## Potential Dangers and Misuse
Byt3Lock's appearance and behavior resemble ransomware, which can cause fear and panic among users. It's essential to use this script responsibly and ethically. Potential risks and misuse include:
- Unauthorized Access: Installing this program without proper authorization could lead to unauthorized access to someone else's computer.
- Destructive Actions: Initiating actions like simulating a kernel panic on Linux or attempting to trigger a BSOD on Windows could potentially lead to data loss or system instability.
- Social Engineering: The program's interface might convince users to enter sensitive information, thinking it's required to unlock the system.
- Privacy Invasion: Installing this script on someone's computer without their consent could be used to monitor their activities.

## Usage
1. Execute the `locker.py` script using Python.(u must use sudo)
2. Enter the password "123" to unlock the program.
3. Experiment with the script responsibly and with proper authorization.

## Disclaimer
This script is for educational purposes only. Unauthorized use for malicious intent is strictly prohibited and may have legal consequences. Always use this script responsibly and with ethical considerations in mind.

**Please note:** Byt3Lock should never be used with malicious intent or on systems without proper authorization. Unauthorized use of such scripts can have serious legal and ethical consequences.

---

**IMPORTANT:** Please do not use this script for any malicious purposes. Its primary use is to educate and raise awareness about cybersecurity threats and should only be used in controlled and authorized environments for that purpose.
