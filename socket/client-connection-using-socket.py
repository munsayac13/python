import socket
import datetime

def timenow() -> str:
    return str(datetime.datetime.now())

def closesocket(client: socket):
    client.close()
    exit()

def run_client(server_ip: str = None):

    if server_ip == None:
        server_ip = "127.0.0.1"

    server_port = 8000

    try:
        # create a socket object
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
        # establish connection with server
        client.connect((server_ip, server_port))
        print(timenow() + ' ' + f"Info: Successful Connection to {server_ip}:{server_port}")
    except ConnectionError as ce:
        print(timenow() + ' ' + f"Error: {ce}")
        closesocket(client)

    try:
        while True:
            # get input message from user and send it to the server
            msg = input("Enter message: ")
            if msg == "quit" or msg == "exit":
                closesocket(client)

            client.send(msg.encode("utf-8")[:1024])

            # receive message from the server
            response = client.recv(1024)
            response = response.decode("utf-8")

            # if server sent us "closed" in the payload, we break out of
            # the loop and close our socket
            if response.lower() == "closed":
                break
            print(timenow() + ' ' + f"Received: {response}")

    except KeyboardInterrupt:
        print("\n"+ timenow() + ' ' + f"Error: Interrupted by user")
    except Exception as e:
        print(timenow() + ' ' + f"Error: {e}")
    finally:
        # close client socket (connection to the server)
        client.close()
        print(timenow() + ' ' + f"Info: Connection to server closed")

if __name__  == "__main__":
    run_client()