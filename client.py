import socket
import sys




def processTSMessage(lines, ts_port):
	tsHostname = lines[0].split()[1]
	tsQueryString = ""
	print("LINES TO PROCESS", lines)

	for line in lines:
		components = line.split()
		query = components[0]
		tsQueryString += query + " " 


	try:
		tsSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("[C]: Client socket for TS created")
	except:
		print('socket open error: {} \n'.format(err))
		exit()

	ts_host_addr = socket.gethostbyname(tsHostname) #address of RS host
	print("ADDRESS: "+ts_host_addr)

	ts_binding = (ts_host_addr, int(ts_port))
	tsSocket.connect(ts_binding) 

	tsSocket.sendall(tsQueryString)
	tsData = tsSocket.recv(2048)
	addresses = tsData.split(',')
	return addresses


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


rawOutput = []
queryString = ""
for query in queries:
	queryString += query + " "

print("QUERY STRING: "+ queryString)
cs.sendall(queryString)
data = cs.recv(1024)
print("DATA: "+data)
rawOutput = data.split(',')

outputFile = open("RESOLVED.txt", "w")

finalOutput = []
ts_lines = []
for line in rawOutput:
	print("LINE: " + line)
	if len(line.split()) == 3: #this line is acceptable final output
		finalOutput.append(line)
	elif len(line.split()) > 3:
		ts_lines.append(line) #this line needs to be processed and client needs to connect with TS

ts_addresses = processTSMessage(ts_lines, ts_port)
finalOutput += ts_addresses


for line in finalOutput:
	outputFile.write(line+"\n")

outputFile.close()


cs.close()
exit()