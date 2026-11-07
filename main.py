import subprocess
from config import DEVICE_IP


def connect_and_mirror():
    print(f"[*] Connecting to {DEVICE_IP}...")

    connect_result = subprocess.run(
        ["adb", "connect", DEVICE_IP],
        capture_output=True,
        text=True
    )

    print(connect_result.stdout)

    if "connected" in connect_result.stdout.lower():
        print("[+] Device connected successfully!")
        print("[+] Launching scrcpy...")

        subprocess.run([
            "scrcpy",
            "--stay-awake"
        ])
    else:
        print("[-] Failed to connect.")
        print("[-] Check Wireless Debugging, IP, Port and Wi-Fi.")


if __name__ == "__main__":
    connect_and_mirror()
