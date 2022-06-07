import socket, sys, time # Imprdib need moodulid


s=socket.socket() # Loob socket objekti
host=socket.gethostname() # Hosti nimi
port=8080 # Port
s.bind((host,port)) # Bindi host ja port
print('') # prindib
print('Hostname: '+host) # Prindib hosti nime
print('') # prindib
print('[+] Server started on port ' + str(port)) # Prindib serveri porti
print('')  # prindib
print('server is waiting for connection...') # Prindib serveri ootamise teade
print('')  # prindib
s.listen(1) # Loob serveri kuulamise
conn, addr = s.accept() # Accepti klienti
print('[+] Got connection from ' + str(addr)) # Prindib kliendi aadressi
print('')  # prindib
while 1: # Loob serveri kuulamise
    message = input(str('>> ')) # Küsib klientilt sõnumit
    message = message.encode() # Kodeerib sõnum
    conn.send(message) # Saadab kliendile sõnumit
    print('[+] Message sent') # Prindib sõnumi saatmise teate
    print('')  # prindib
    incoming_message = conn.recv(1024) # Võtab kliendilt sõnumit
    incoming_message = incoming_message.decode() # Dekodeerib sõnum
    print('[+] Message received: ' + incoming_message) # Prindib sõnumi
    print('')  # prindib