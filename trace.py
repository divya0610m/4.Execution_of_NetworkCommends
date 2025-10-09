import subprocess

def traceroute(host):
    print(f"Traceroute to {host}:\n")
    try:
        output = subprocess.check_output(["tracert", "-d", host], stderr=subprocess.STDOUT, text=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print("Error executing traceroute:")
        print(e.output)

if __name__ == "__main__":
    target = input("Enter the website or IP to traceroute: ")
    traceroute(target)
