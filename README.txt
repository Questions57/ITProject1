Adarsh Patel  aap237
Shiv Rattan   ssr108


1.) A recursive query puts burden of the name resolution on the called server. And in an iterative query the contacted server replies with the name of the server to contact. In our program, the socket is created in the client and then connected through the open port with the root server. After binding, listening, and accepting are all over, the root server iterates through its table to see if there any occurences of the hostname. If there is a match, it returns it back, otherwise it returns the TSHostname. If it was a match, it outputs the string as is. If not, the client goes to TS to look for the queried hostname. 


2.) There doesn't seem to be any gaping holes with our code. In our testing, the code seems to work perfectly fine and smoothly from the instructions provided. 

3.) A major component on creating any project is communication, and since both of us are college students, it was hard to make our schedules align and get the program done as quickly as possible. 

A problem that we ran in to when designing this code was how to deal with sending multiple messages. When we wanted to send an entire list of information to one of the servers through the socket, the connection would close after one message being sent in a loop. So we fixed this by converting the query list into an elongated string that sent at once using sendall. 

But apart from that, another problem that we faced when creating the algorithm for the code was understanding how we were going to store and traverse through the different host names, domain names, and DNS records.

4.) This project gave insight on how a lightweight version of DNS would work. It was really interesting to see how some of the most integral parts of modern day Internet are so simple in their foundation, but made more complex through possible edge-cases (i.e. data corruption, reliable transfers, etc).


