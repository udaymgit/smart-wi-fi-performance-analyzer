import pywifi
import time

wifi = pywifi.PyWiFi()

iface = wifi.interfaces()[0]

print("Scanning WiFi Networks...\n")

iface.scan()

time.sleep(3)

results = iface.scan_results()

for network in results:

    signal = network.signal
    freq = network.freq

    if signal >= -50:
        quality = "Excellent"
    elif signal >= -60:
        quality = "Good"
    elif signal >= -70:
        quality = "Fair"
    else:
        quality = "Weak"

    channel = int((freq - 2407) / 5)

    print(
        f"SSID: {network.ssid}\n"
        f"Signal: {signal} dBm\n"
        f"Frequency: {freq} MHz\n"
        f"Channel: {channel}\n"
        f"Quality: {quality}\n"
        f"{'-'*40}"
    )