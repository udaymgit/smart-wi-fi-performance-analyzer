# 📡 Smart WiFi Performance Analyzer

A Python-based network analysis tool that scans nearby WiFi networks, evaluates signal strength, identifies channel congestion, and recommends the optimal WiFi channel for improved wireless performance.

---

## 🚀 Overview

WiFi performance often degrades because of weak signal strength, channel interference, and network congestion.

The Smart WiFi Performance Analyzer helps users:

- Scan nearby WiFi networks
- Analyze signal quality
- Identify strongest available networks
- Detect channel congestion
- Recommend the best WiFi channel
- Visualize network performance
- Export analysis reports

This project provides practical insights into wireless network optimization using Python and data visualization.

---

## ✨ Features

### 📡 Network Scanning
- Detect nearby WiFi networks
- Retrieve SSID information
- Measure signal strength

### 📶 Signal Analysis
- Analyze signal quality
- Identify strongest network
- Compare available networks

### 🎯 Channel Recommendation
- Detect congested channels
- Recommend the best WiFi channel
- Improve network performance

### 📊 Data Visualization
- Generate signal strength charts
- Visualize network distribution
- Display performance metrics

### 📁 Report Generation
- Export results to CSV
- Save network analysis data
- Generate reusable reports

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core Development |
| Streamlit | Interactive Dashboard |
| Pandas | Data Processing |
| PyWiFi | WiFi Scanning |
| Matplotlib | Data Visualization |

---

## 📂 Project Structure

```text
smart-wi-fi-performance-analyzer/
│
├── app.py
├── scanner.py
├── visualization.py
├── wifi_analysis.csv
├── requirements.txt
├── README.md
```

---

## 📸 Preview

### Dashboard

<img width="1920" height="1020" alt="2026-06-17" src="https://github.com/user-attachments/assets/7a1d590f-b3c5-4eb5-8481-796dcf4ea595" />


```markdown
![Dashboard](images/dashboard.png)
```
```

### Network Visualization

```markdown
![Visualization](images/visualization.png)
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/udaymgit/smart-wi-fi-performance-analyzer.git
cd smart-wi-fi-performance-analyzer
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

After running:

```text
Local URL: http://localhost:8501
```

Open the URL in your browser.

---

## 📈 Example Output

### Network Scan

```text
SSID: Home_WiFi
Signal: -42 dBm
Frequency: 2412 MHz
Channel: 1
Quality: Excellent
```

### Channel Recommendation

```text
Recommended Channel: 11
```

### Strongest Network

```text
Strongest Signal: Home_WiFi (-42 dBm)
```

---

## 🔄 Workflow

```text
Scan WiFi Networks
       ↓
Collect Signal Data
       ↓
Analyze Network Quality
       ↓
Detect Channel Congestion
       ↓
Recommend Best Channel
       ↓
Generate Visual Reports
       ↓
Export CSV Report
```

---

## 📊 Skills Demonstrated

- Computer Networking
- Wireless Network Analysis
- Python Development
- Data Analysis
- Data Visualization
- Streamlit Dashboard Development
- Performance Optimization

---

## 🎯 Real-World Applications

- Home WiFi Optimization
- Office Network Analysis
- Wireless Troubleshooting
- Channel Congestion Detection
- Network Performance Monitoring

---

## 🔮 Future Enhancements

- Real-Time Monitoring Dashboard
- Speed Test Integration
- Historical Performance Tracking
- Network Security Analysis
- Automatic Optimization Suggestions

---

## 👨‍💻 Author

**Uday M**

GitHub: https://github.com/udaymgit

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
