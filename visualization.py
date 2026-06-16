import pywifi
import time
import pandas as pd
import matplotlib.pyplot as plt

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

print("Scanning Networks...")

iface.scan()
time.sleep(3)

results = iface.scan_results()

data = []

for network in results:

    data.append({
        "SSID": network.ssid,
        "Signal": network.signal,
        "Channel": int((network.freq - 2407) / 5)
    })

df = pd.DataFrame(data)

print(df)

channel_count = df["Channel"].value_counts()

plt.figure(figsize=(8,5))

channel_count.plot(kind="bar")

plt.title("Channel Congestion")

plt.xlabel("Channel")

plt.ylabel("Number of Networks")

plt.tight_layout()

plt.show()

strongest = df.loc[df["Signal"].idxmax()]

print("\nStrongest Network:\n")

print(strongest)