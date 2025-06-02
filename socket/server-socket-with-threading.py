import socket
import threading
import datetime
import sys
import signal
import time

from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'verysecret'

server_name = socket.gethostname()
#server_ip = socket.gethostbyname(server_name)
server_ip = '127.0.0.1'
port = 8000

@app.route('/')
def index():
    return "Welcome to CM Flask app"

@app.route('/getserver')
def getserver_page():
    return render_template('server.html', host=server_name, port=port)

def timenow() -> str:
    return str(datetime.datetime.now())

def handle_client(client_socket, addr):
    try:
        while True:
            request = client_socket.recv(1024).decode('utf-8')
            if request.lower() == "close":
                client_socket.send("closed".encode('utf-8'))
                break
            print(timenow() + ' ' + f"Received: {request}")

            response = "accepted"
            client_socket.send(response.encode('utf-8'))
    except KeyboardInterrupt:
        print("\n"+ timenow() + ' ' + f"Error: Interrupted by user")
    except Exception as e:
        print(timenow() + ' ' + f"Error when handling client: {e}")
    finally:
        client_socket.close()
        print(timenow() + ' ' + f"Connection to client ({addr[0]}:{addr[1]}) closed")

def run_flask():
    # Allow all host to access server
    #app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False, threaded=True)
    
    # Allow only local host to access server
    app.run(port=5000, debug=True, use_reloader=False, threaded=True)

def run_server():

    try:
        # create a socket object
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # bind the socket to the host and port
        server.bind((server_ip, port))
        # listen for incoming connections
        server.listen()
        print(timenow() + ' ' + f"Listening on {server_ip}:{port}")

        while True:
            # accept a client connection
            client_socket, addr = server.accept()
            print(timenow() + ' ' + f"Accepted connection from {addr[0]}:{addr[1]}")
            # start a new thread to handle the client
            thread = threading.Thread(target=handle_client, args=(client_socket, addr,))
            thread.start()
    except KeyboardInterrupt:
        print("\n"+ timenow() + ' ' + f"Error: Interrupted by user")
    except Exception as e:
        print(timenow() + ' ' + f"Error: {e}")
    finally:
        server.close()
        print(timenow() + ' ' + f"Info: Server socket closed")

def signal_handler(sig, frame):
    print(timenow() + ' ' + f"Info: Signal received, shutting down flask and socket ...")
    sys.exit(0)


if __name__ == "__main__":

    signal.signal(signal.SIGINT, signal_handler)

    stop_thread = False
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()       
    socket_thread = threading.Thread(target=run_server)
    socket_thread.daemon = True
    socket_thread.start()

    print(timenow() + ' ' + 'Info: Threads started ...')
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break
