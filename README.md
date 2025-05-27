# 🛡️ Log Analyzer for Intrusion Detection
### ⚔️ Your First Line of Defense Against Brute-Force Attacks

> **“Every attack leaves a trace. This tool makes sure you find it.”**  
A lightweight, Python-powered log analysis tool that scans SSH logs to detect and respond to brute-force attacks in real time.

![demo](assets/demo.png)

---

## 🚀 Project Summary

🔍 Built for cybersecurity enthusiasts and professionals, this project simulates what a SOC analyst does every day — scanning logs, identifying threats, and stopping them before they escalate.

Whether you’re prepping for a cybersecurity role or aiming to master system defense, this project proves your skill in:
- Automation
- Pattern recognition (regex)
- System hardening (iptables)

---

## 🛠️ Features at a Glance

| Feature                        | Description                                       |
|-------------------------------|---------------------------------------------------|
| 🚫 Failed Login Detection      | Scans logs for multiple failed SSH login attempts |
| 📊 Suspicious IP Reporting     | Lists brute-force IPs that breach set thresholds  |
| 🔥 Optional IP Blocking        | Uses Linux `iptables` to block repeat offenders   |
| 🧠 Regex-Based Intelligence     | Flexible pattern matching on any log format       |
| 🖥️ Works with Simulated Logs  | Includes sample logs for testing                  |

---

## 🧪 How It Works

```plaintext
[ Log File ] --> [ Pattern Matching (Regex) ] --> [ Count Attempts ] --> [ Flag/Block IPs ]


log-analyzer/
├── log_analyzer.py         # Main script
├── sample_auth.log         # Test log file
├── assets/
│   └── demo.png            # Screenshot (add this!)
└── README.md               # This file
