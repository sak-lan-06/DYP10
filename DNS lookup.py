import socket

def main():
    # Prompt user for choice
    print("1. Enter Host Name\n2. Enter IP address")
    choice = int(input("Choice: "))
    
    if choice == 1:
        # Get the host name from the user
        host = input("\nEnter host name: ")
        try:
            # Get the IP address associated with the host name
            address = socket.gethostbyname(host)
            print(f"IP address: {address}")
            
            # Get the full host information (reverse lookup)
            host_name = socket.gethostbyaddr(address)
            print(f"Host name: {host_name[0]}")
            print(f"Host name and IP address: {host_name[0]} ({address})")
            
        except socket.gaierror:
            print(f"Could not find {host}")
    
    elif choice == 2:
        # Get the IP address from the user
        host = input("\nEnter IP address: ")
        try:
            # Get the host name associated with the IP address
            host_name = socket.gethostbyaddr(host)
            print(f"Host name: {host_name[0]}")
            print(f"IP address: {host}")
            print(f"Host name and IP address: {host_name[0]} ({host})")
            
        except socket.herror:
            print(f"Could not find {host}")
        except socket.gaierror:
            print(f"Invalid IP address format: {host}")
    
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
