import port_scan
try:
    Target_ip = input("[+] * Enter the target ip u want to scan : ")
    port_numbers = int(input("[+] * Enter the Amout Number of ports That u want To Scan : "))
    vul_path = input("[+] * Enter the Path of the vulnerable File : ")
    print("\n")

    try:
        target = port_scan.PortScan(Target_ip,port_numbers)
        target.scan()
    except ValueError:
        print("\n Error")
    except KeyboardInterrupt:
        print("\n Error")
    
except KeyboardInterrupt:
    print("\n")
    print("Error")
except ValueError:
    print("\n")
    print("Error")


