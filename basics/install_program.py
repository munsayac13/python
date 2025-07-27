import getpass
import subprocess


installed_programs = []
username = getpass.getuser()

print("Welcome! ", username)
print("")

while True:
    action = input("Type install, show, or exit: ")

    match action:
        case 'install':
            try:

                # Choose program to install
                program_to_install = input ("Type program to install: ")
                print("Installing Program: ", program_to_install)
                subprocess.run(["sudo", "apt", "update"], check=True)
                print("apt update successful!")

                # Install package
                subprocess.run(["sudo", "apt", "install", "-y", program_to_install], check=True)
                print(program_to_install, "installed successfully")

            except subprocess.CalledProcessError as e:
                print(f"Apt command occured an error: {e}")
                print(f"Return code: {e.returncode}")
                print(f"Output: {e.output}")
                print(f"Stderr: {e.stderr}")
            except FileNotFoundError:
                print("Error: command 'apt' not found!")

        case 'show':
            print("Following are the list of all installed applications")
            subprocess.run(["sudo", "apt", "list", "--installed"])

        case 'exit':
            
            break
print("Thanks for using! We'll see you next time.")
print("Good Bye!")