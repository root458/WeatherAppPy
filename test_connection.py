import socket

def test_connection():
    try:
        socket.create_connection(('google.com', 80))
        return True
    except Exception:
        return False
        
# print(test_connection())