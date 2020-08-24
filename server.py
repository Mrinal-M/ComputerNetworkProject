import socket
import random
from threading import Thread

#qndict is a dictionary which contains the questions and the corresponding answers
qndict={"q1":"1","q2":"2","q3":"3","q4":"4","q5":"5","q6":"6","q7":"7","q8":"8","q9":"9","q10":"10","q11":"11","q12":"12","q13":"13","q14":"14","q15":"15","q16":"16","q17":"17","q18":"18","q19":"19","q20":"20"}
#qnlist is the set of questions
qnlist=["q1","q2","q3","q4","q5","q6","q7","q8","q9","q10","q11","q12","q13","q14","q15","q16","q17","q18","q19","q20"]

#clientlist maintains the list of players playing the game
#portlist maintains the ports through which the clients are connected
#bz keeps track whether any player(client) has pressed the buzzer. If any client has already pressed the bz then bz[0]=1
#no is the pointer to which question to be asked. Even though no is incremented by 1 in the function, the random shuffle of the questions ensure that the order of questions is not sequential

clientlist= []
portlist=[]
bz=0
no=0


random.shuffle(qnlist)
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())
port=1235
address=(ip,port)
server.bind(address)
def clienthandler():
    '''The function handles the client operations.
    The client can send answers and press buzzer for each question.
    Once a question is broadcasted by the server, whoever presses the buzzer first will get to answer the question.
    The functions takes care of the condition and allows the player who first pressed the buzzer to answer.
    If the answer is right, the score gets incremented and if the score is 5 the player is declared the winner and the game is OVER!!!
    If the player provides a wrong answer then the next question is broadcasted'''
    global no,bz
    client,addr=server.accept()
    #server.accept() returns a new socket and address of client. Address is a tuple (ip,port)
    clientlist.append(client)
    portlist.append(addr[1])
    count=0#keeps track of the score
    print("Got a connection from {}:{}".format(addr[0],addr[1]))
    while count<5:
        if(len(clientlist)==3 and bz==0) :
            broadcast(qnlist[no])
            no=no+1
        data=client.recv(1024)
        if(data[0:2]=="bz" and bz!=1 ):
            bz=1
            ans=client.recv(1024)
            #print qnlist[no-1]
            #print (qndict[qnlist[no-1]])
            if (len(qndict[qnlist[no-1]])==2 and ans[0:2]==qndict[qnlist[no-1]]) or (len(qndict[qnlist[no-1]])==1 and ans[0:1]==qndict[qnlist[no-1]]):
                count=count+1
                print ("score of {},{},is {}".format(addr[0],addr[1],count))
                #qnlist.remove(qnlist[no])
                bz=0
                if count==5:
                    print ("game won by {}:{}".format(addr[0],addr[1]))
                    for client in clientlist:
                        client.close()
                        break
            else:
                print ("Wrong Answer")
                bz=0
        elif(data=="disconnect"):
            client.send("Goodbyeeeee")
            client.close()
            break
        else:
            print ("SORRY you are LATE!")

        
        
            
#setting up the server

n=20
def broadcast(message):
    '''A message is braodcasted to each client in the clientlist'''
    for client in clientlist:
        client.send(message)

print("Started listening on {}:{}".format(ip,port))
server.listen(5)
#client1,addr1=server.accept()
#print "got a connection from ",addr1[0],":",addr1[1]
#client2,addr2=server.accept()
#print "got a connection from ",addr2[0],":",addr2[1]
#client3,addr3=server.accept()
#print "got a connection from ",addr3[0],":",addr3[1]
for i in range(3):
    Thread(target=clienthandler).start()
#server.close()
