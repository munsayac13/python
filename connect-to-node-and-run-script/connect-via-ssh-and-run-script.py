import paramiko as p

def connect_to_server(hostname, user, userpass, command):
    sshclient = p.SSHClient()
    sshclient.set_missing_host_key_policy(p.AutoAddPolicy())
    sshclient.connect(hostname, username=user, password=userpass)

    stdin, stdout, stderr = sshclient.exec_command(command)
    print(stdout.read().decode())

    sshclient.close()

if __name__ == "__main__":
    #connect_to_server("192.168.44.133", "devops", "devops", "./backup-postgres.sh")
    connect_to_server("192.168.44.133", "devops", "devops", "free -m; df -h")
