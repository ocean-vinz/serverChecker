import socket
import re
import os


SERVER=[]
PORT=80 #which port you want to connect to
CONNTIMEOUT=5 #Connection timeout in sec, because the default is none and will hang if not set
SITEOK=0
TOTALSITE=0
currentDir=os.getcwd()


def is_running(site, port, timeout):
    try:
        socket.setdefaulttimeout(timeout)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #the AF_INET and SOCK_Stream are the default values, it can be left empty
        sock.connect((site, port))
        return True
    except:
        return False


if __name__ == "__main__":

    with open(currentDir + '/serverlist.txt', 'r') as serverlist:
        for line in serverlist:
            line=re.sub(r'\n','',line) #removing the \n from the list
            SERVER.append(line)

    for site in SERVER:
        try:
            if is_running(site, PORT, CONNTIMEOUT):
                print(f"{site} is running!")
                SITEOK+=1
            else:
                print(f'There is NO response for server {site}')
        except:
            print('something went terribly wrong with the function')
        finally:
            TOTALSITE+=1
        
print('SUMMARY (OK/NOK): ' + str(SITEOK) + '/' + str(TOTALSITE))
