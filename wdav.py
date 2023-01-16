import socket
from http.server import HTTPServer, SimpleHTTPRequestHandler
from appJar import gui
import webbrowser
import threading


# Function to start the server
def server(btn):
    if btn == "Start":
        host_name = socket.gethostbyname(socket.gethostname())
        port_number = 5050
        # Create an HTTP server
        httpd = HTTPServer((host_name, port_number), SimpleHTTPRequestHandler)
        # Start the server in a separate thread
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.start()
        app.setLabel("SL", f"Server: http://{host_name}:{port_number}")
        print("Server started at http://{}:{}".format(*httpd.socket.getsockname()))
    if btn == "Stop":
        if btn == "Stop":
            httpd.shutdown()
            server_thread.join()
            app.setLabel("SL", "Server: Offline")
            print("Server stopped.")
            app.infoBox("Server stopped", "Server has been stopped successfully")


def openbrowser(btn):
    print(f"Opening server in browser")
    host_name = socket.gethostbyname(socket.gethostname())
    port_number = 5050
    webbrowser.open(f"http://{host_name}:{port_number}")


app = gui()

# Add a button to start the server
app.addLabel("SL", "---.---.-.--")
app.setLabelFont(20)
app.setBg("White")
app.addButton("Start", server)
app.addButton("Stop", server)
app.addButton("Open In Browser", openbrowser)

# Start the GUI
app.go()
