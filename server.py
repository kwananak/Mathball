import socket
import select
import math
import time


HEADER_LENTGH = 10
IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))

server_socket.listen(2)

sockets_list = [server_socket]

clients = {}

print("server running")

class Etat:
    def __init__(self):
        self.pret = False
        self.qt_manches = []
        self.reponse1 = ""
        self.reponse2 = ""

    def switch(self):
        self.pret = True


serveur = Etat()

frappes = []

while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            sockets_list.append(client_socket)
            clients[client_socket] = client_socket

            if len(sockets_list) == 3:
                client_socket.send(("flip").encode("utf-8"))
            else:
                client_socket.send(("flop").encode("utf-8"))

            print(f"Accepted new connection from {client_address[0]}:{client_address[1]}")

        else:
            message = notified_socket.recv(1024).decode("utf-8")

            if message is False:
                print("Closed connection")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            if len(message) > 6:
                if message[:6] == "lancer":
                    for client_socket in clients:
                        client_socket.send(message.encode("utf-8"))
                if message[:6] == "frappe":
                    coup = [message, time.time_ns()]
                    frappes.append(coup)
                    print(frappes)
                    if len(frappes) == 2:
                        if frappes[0][1] < frappes[1][1]:
                            for client_socket in clients:
                                client_socket.send(frappes[0][0].encode("utf-8"))
                        else:
                            for client_socket in clients:
                                client_socket.send(frappes[1][0].encode("utf-8"))
                        frappes = []

            match message:
                case "jouer":
                    if serveur.pret:
                        reponse = "commencer"
                        for client_socket in clients:
                            client_socket.send(reponse.encode("utf-8"))
                    else:
                        serveur.switch()
                case "1":
                    serveur.qt_manches.append(1)
                    if len(serveur.qt_manches) == 2:
                        for client_socket in clients:
                            client_socket.send(
                                str(math.floor((serveur.qt_manches[0] + serveur.qt_manches[1]) / 2)).encode("utf-8"))
                case "2":
                    serveur.qt_manches.append(2)
                    if len(serveur.qt_manches) == 2:
                        for client_socket in clients:
                            client_socket.send(
                                str(math.floor((serveur.qt_manches[0] + serveur.qt_manches[1]) / 2)).encode("utf-8"))
                case "3":
                    serveur.qt_manches.append(3)
                    if len(serveur.qt_manches) == 2:
                        for client_socket in clients:
                            client_socket.send(
                                str(math.floor((serveur.qt_manches[0] + serveur.qt_manches[1]) / 2)).encode("utf-8"))
                case "4":
                    serveur.qt_manches.append(4)
                    if len(serveur.qt_manches) == 2:
                        for client_socket in clients:
                            client_socket.send(
                                str(math.floor((serveur.qt_manches[0] + serveur.qt_manches[1]) / 2)).encode("utf-8"))
                case "5":
                    serveur.qt_manches.append(5)
                    if len(serveur.qt_manches) == 2:
                        for client_socket in clients:
                            client_socket.send(
                                str(math.floor((serveur.qt_manches[0] + serveur.qt_manches[1]) / 2)).encode("utf-8"))

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
