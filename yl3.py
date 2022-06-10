import socket # Impordib socket mooduli
s = socket.socket() # Loob socket objekti
host = input(str("Sisestage saatja hosti aadress : ")) # host = "
port = 8080 # port on 8080
s.connect((host,port)) #saab serveri aadressi ja porti
print("Ühendatud ... ") # kontrollib, kas ühendus on loodud

filename = input(str("Sisestage sissetuleva faili failinimi : "))
file = open(filename, 'wb') # avab faili
file_data = s.recv(1024) # saadab faili
file.write(file_data) # kirjutab faili
file.close() # sulgeb faili
print("Fail on edukalt vastu võetud.")
import socket # Impordib socket mooduli

s = socket.socket() # Loob socket objekti
host = socket.gethostname()
port = 8080 # port on 8080
s.bind((host,port)) # saab serveri aadressi ja porti
s.listen(1)
print(host)
print("Waiting for any incoming connections ... ") # kontrollib, kas kasutaja on ühendatud
conn, addr = s.accept() # kuulab kasutajat
print(addr, "Has connected to the server") # kontrollib, kas kasutaja on ühendatud

filename = input(str("Please enter the filename of the file : ")) # küsib kasutajalt failinime
file = open(filename , 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Data has been transmitted successfully") # kontrollib, kas fail on edukalt saadetud