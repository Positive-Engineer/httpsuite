""" Example of using httpsuite to communicate with an external web server using sockets.

1. Open a new socket.
2. Creates the request to be sent via Request object.
3. Connect to httpbin.org via socket.
4. Send generated request to server.
5. Receive raw response from server.
6. Parse the server's response with Response object.
7. Loads the response's body via JSON.
8. Close socket.
"""

from httpsuite import Request, Response
import socket
import json

# 1. Open a new socket.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Creates the request to be sent via Request object.
body = json.dumps({"hello": "world"})
request = Request(
    method="POST",
    target="/post",
    protocol="HTTP/1.1",
    headers={
        "Host": "httpbin.org",
        "Connection": "close",
        "Content-Length": len(body),
        "Accept": "*/*",
    },
    body=body,
)

# Prints the raw request.
print("====== Raw Request ======", "\n")
print(request.raw, "\n")

# 3. Connect to httpbin.org via socket.
s.connect(("httpbin.org", 80))

# 4. Send generated request to server.
s.sendall(request.raw)

# 5. Receive raw response from server.
response_raw = s.recv(4096)

# Prints the raw response.
print("====== Raw Response ======", "\n")
print(response_raw, "\n")

# 6. Parse the server's response with Response object.
response = Response.parse(response_raw)

# Prints the request and the response (pretty-print).
print("====== Request and Response ======", "\n")
print(request, "\n")
print(response, "\n")

# 7. Loads the response's body via JSON.
body = json.loads(response.body.string)

# Prints the loaded json ('dumps' for pretty-print).
print("====== Json ======", "\n")
print(json.dumps(body, indent=4))

# 8. Close socket.
s.close()
