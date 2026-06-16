import pywifi
import time
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Smart WiFi Performance Analyzer",
    layout="wide"
)

st.title("📶 Smart WiFi Performance Analyzer")

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

with st.spinner("Scanning WiFi Networks..."):
    iface.scan()
    time.sleep(3)
    results = iface.scan_results()

data = []

for network in results:
    
    freq_mhz = network.freq / 1000

    if freq_mhz < 3000:
        channel = int((freq_mhz - 2407) / 5)
    else:
        channel = int((freq_mhz - 5000) / 5)

    data.append({
        "SSID": network.ssid,
        "Signal": network.signal,
        "Frequency": freq_mhz,
        "Channel": channel
    })

df = pd.DataFrame(data)

st.subheader("Available Networks")

st.dataframe(df)

strongest = df.loc[df["Signal"].idxmax()]

st.success(
    f"Strongest Network: {strongest['SSID']} "
    f"({strongest['Signal']} dBm)"
)

channel_count = df["Channel"].value_counts()

best_channel = channel_count.idxmin()

st.info(
    f"Recommended Channel: {best_channel}"
)

st.subheader("Signal Strength")

st.bar_chart(
    df.set_index("SSID")["Signal"]
)

st.subheader("Channel Congestion")

st.bar_chart(channel_count)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Networks Found",
    len(df)
)

col2.metric(
    "Strongest Signal",
    f"{strongest['Signal']} dBm"
)

col3.metric(
    "Recommended Channel",
    best_channel
)
csv = df.to_csv(index=False)

st.download_button(
    label="📥 Download CSV Report",
    data=csv,
    file_name="wifi_report.csv",
    mime="text/csv"
)