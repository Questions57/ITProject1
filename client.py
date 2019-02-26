import socket
import sys


queries = []
file = open("PROJI-HNS.txt", "r")

#looping through each line to fill table info
for line in file: 
	queries.append(line)

file.close() 
print(queries)

#def client():
try:
	cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("[C]: Client socket created")
except:
	print('socket open error: {} \n'.format(err))
	exit()

rs_port = sys.argv[2] #port on which RS is listening
ts_port = sys.argv[3] #port on which TS is listening
rs_hostname = sys.argv[1] #hostname of machine running RS

rs_host_addr = socket.gethostbyname(rs_hostname) #address of RS host
print("ADDRESS: "+rs_host_addr)

rs_binding = (rs_host_addr, int(rs_port))
cs.connect(rs_binding) 


output = []
queryString = ""
for query in queries:
	queryString += query + " "

print("QUERY STRING: "+ queryString)
cs.sendall(queryString)
data = cs.recv(1024)
print("DATA: "+data)
output = data.split(',')

outputFile = open("RESOLVED.txt", "w")
for line in output:
	print("LINE: " + line)
	outputFile.write(line+"\n")

outputFile.close()


cs.close()
exit()