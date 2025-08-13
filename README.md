# Raspberry Pi Pico WH as HID for Keystroke Injection
A step-by-step guide to turn your Raspberry Pi Pico WH into a HID device. Works as a rubber ducky and you can remotely add payloads.
I have used a Raspberry pi pico wh for this project.

---
## Installation
***NOTE: To edit safely (setup mode): Use a jumper wire to connect GP0 (pin 1) to GND (pin 3) on Pico WH before plugging into your computer.***
1. Download CircuitPython UF2 file for Raspberry Pi Pico W from [CircuitPython for rpi pico](https://circuitpython.org/board/raspberry_pi_pico_w/). Download the latest release.
2. Connect Pico WH to your computer via USB while holding the `BOOTSEL` button. It appears as a drive named RPI-RP2.
3. Copy the entire "lib" folder to the root of the `CIRCUITPY` drive.
4. Copy code.py and duckyinpython.py to the root of CIRCUITPY.
5. Create a payload file: Open a text editor, write DuckyScript code or you can check out the payloads in this repository.
6. Save the file as payload.dd in the root of CIRCUITPY.
7. Remove the jumper. Plug Pico into target computer; it emulates a keyboard and injects the payload keystrokes.

---
## Connecting to the pico via its AP
edit the secrets.py file and change ssid of your pico and set the password. You then need to connect to the AP using the credentials.
Open a web browser and go to 198.162.4.1 (this is the default ip of the pico), here you can add or edit your payloads remotely after you plus it in to the target computer.

---
## Example payload
This code here will open the powershell using the Win+r key and type ipconfig command which displays the IP configuration on the target.
```text
REM Opens PowerShell and runs ipconfig
DELAY 1000
GUI r
DELAY 500
STRING powershell
ENTER
DELAY 1500
STRING ipconfig
ENTER
```
Here you can change the `DELAY` time to 2 sec or other as some computers might take more time than 1 sec.<br>

---
NOTE:
This is just an example code, you can try to create your payloads and save it to the root of the rpi as an `.dd` file after completing the installation process as explained above.
