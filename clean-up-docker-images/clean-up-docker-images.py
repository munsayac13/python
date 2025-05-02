import os

def cleanup_docker_in_host():
    # Stop and remove all containers
    print("Stopping docker containers ...")
    os.system("docker stop $(docker ps -a -q)")

    print("Removing docker processes ...")
    os.system("docker rm $(docker ps -a -q)")

    print("Removing all images that are dangling ...")
    os.system("docker rmi $(docker images -f 'dangling=true' -q)")

    print("Removing unused volumes ...")
    os.system("docker volume prune -f")

    print("Docker cleanup completed.")

if __name__ == "__main__":
    cleanup_docker_in_host()