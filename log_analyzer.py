import re
from collections import defaultdict

# Change this to '/var/log/auth.log' on Linux
LOG_FILE = "sample_auth.log"
THRESHOLD = 3

def parse_log(file_path):
    failed_attempts = defaultdict(int)
    with open(file_path, 'r') as file:
        for line in file:
            if "Failed password" in line:
                match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
                if match:
                    ip = match.group(1)
                    failed_attempts[ip] += 1
    return failed_attempts

def print_suspicious_ips(attempts):
    print("\nSuspicious IPs (more than {} failed attempts):".format(THRESHOLD))
    for ip, count in attempts.items():
        if count > THRESHOLD:
            print(f"{ip} => {count} failed attempts")

if __name__ == "__main__":
    attempts = parse_log(LOG_FILE)
    print_suspicious_ips(attempts)
