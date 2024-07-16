import socket
import time
from colorama import Fore, Style

wait = 5

# Function to check network connectivity
def is_connected():
    try:
        # Set a timeout to avoid waiting indefinitely
        socket.setdefaulttimeout(3)
        socket.gethostbyname("8.8.8.8")  # Ping Google's DNS server
        return True
    except socket.gaierror:
        return False
    except socket.timeout:
        return False


print(Style.BRIGHT)
while True:
    if is_connected():
        print(f"{Fore.GREEN}[CONNECTED] {Fore.WHITE} Network connection is working and active")
    else:
        print(f"{Fore.RED}[ERROR] Network connection is down")

    time.sleep(wait)
