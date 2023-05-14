import random
import time

# sql init
percentage = 0
device_storage = [
    "\x1b[1;32mKB\x1b[1;32m",
    "\x1b[1;32mMG\x1b[1;32m",
    "\x1b[1;32mByte\x1b[1;32m",
]
memory_moved = 128

# download links
repo_link = "https://github.com"
max_repo_link_num = random.randint(45, 100)
repo_link_num = 0

# cpu components

memory_ram = [128, 256, 512, 1024, 2048]
pc_comp = [
    "000x1000000",
    "shl0010000x00",
    "10101x0x1",
    "0x110x01",
    "1x0xx10",
    "x110011x",
    "0110x01",
    "x01x01x0",
    "110xx01",
    "x10x1x0",
    "010101x0",
    "x0111x0x",
]
time_scanned = 0
first_scan = False
"""
1: ask matrix mode
2: you want to continue?
3: function
"""


def start():
    print("1: SQL Injection\n2: Download links\n3: CPU components")
    one = input("Choose a number: ")
    if int(one) == 1:
        sql_injection_init()
    elif int(one) == 2:
        download_links()
    elif int(one) == 3:
        cpu_components()
    else:
        print("Invalid responde")
        start()


def sql_injection_init():
    global percentage
    while True and percentage < 101:
        if not percentage == 100:
            if not percentage < 50:
                percentage += 1
                print(
                    f"SQL Injection compilation {percentage}% ... \x1b[1;32m{random.randint(memory_moved, 4080)} {random.choice(device_storage)}\x1b[0m"
                )
                time.sleep(random.randint(1, 5))
            else:
                percentage += 1
                print(
                    f"SQL Injection compilation {percentage}% ... \x1b[1;32m{random.randint(memory_moved, 4080)} {random.choice(device_storage)}\x1b[0m"
                )
                time.sleep(random.uniform(0.004, 2.4))
        else:
            print("SQL Injection completed.")
            # download_links()
            # break
            again = input("Do you want to continue? Y/N\n")
            if again == "Y":
                start()
            elif again == "N":
                exit()
            else:
                print("Invalid responde")
                start()


def download_links():
    global repo_link_num
    while repo_link_num != max_repo_link_num:
        print(
            f"Download recourses from \033[1;34m{repo_link}/{random.randint(111111, 99999999)}/{random.randint(111111, 9999999999)}\033[0m ..."
        )
        repo_link_num += 1
        time.sleep(random.randint(1, 5))
        if repo_link_num == max_repo_link_num:
            print("Download completed")
            # cpu_components()
            # break
            again = input("Do you want to continue? Y/N\n")
            if again == "Y":
                start()
            elif again == "N":
                exit()
            else:
                print("Invalid responde")
                start()


def cpu_components():
    global first_scan, time_scanned
    if not first_scan:
        print("Starting to scan the hard drives ...")
        first_scan = True
        time.sleep(5)
        cpu_components()
    else:
        while time_scanned < 1000:
            if time_scanned < 120:
                print(
                    f"Scanning hard drives... {random.choice(pc_comp)}\n[{random.choice(memory_ram)} MG scanned]\n Pinging ..."
                )
                time_scanned += 1
                time.sleep(0.04)
            else:
                print(
                    f"Scanning hard drives... {random.choice(pc_comp)}\n[{random.choice(memory_ram)} MG scanned]"
                )
                time_scanned += 1
                time.sleep(0.09)
        if time_scanned == 1000:
            print("Scanning completed.")
            again = input("Do you want to continue? Y/N\n")
            if again == "Y":
                start()
            elif again == "N":
                exit()
            else:
                print("Invalid responde")
                start()


start()
