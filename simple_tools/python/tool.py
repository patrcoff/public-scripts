#a script to search for iso files on C drive which sumarises them etc, classifies by keywords such as ubuntu, windows etc
#another script to give brief network overview and a few network diagnostics (such as ping, traceroute etc which creates a report)
#or a more generic troubleshooting script
import socket
import subprocess
import psutil #not in default python libraries and requires visual studios cpp build studios??? or is that just powershell talking shit?
#or is this a windows 11 issue?

#ping some addresses to test connectivity#
def ping(address):
    command = 'ping -n 1 ' + address
    response = subprocess.run(command,universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #0 means successful ping, 1 is unsuccesful
    return response

def hardware():
    cpu = psutil.cpu_percent(4)
    ram = psutil.virtual_memory()[2] #this function returns a tuple with ram info, 3rd field is % usage
    return [cpu,ram]

def linebreak():
    print('\n---------------------------------------------------------------------------------------------\n')

def resolve(address):
    command = 'nslookup ' + address
    response = subprocess.run(command,universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return response
    #take address and see if can be resolved
    #return resolved address if possible, original address if not



#commands to implement/network info to extract
#wifi or lan?
#do you have an ip
#can you reach google (by ip)
#can you reach google (by fqdn)
#can you reach caftex, other local servers etc
#can you resolve addresses [list of common addresses]
#trace to a couple of known destinations - get info on whether problems exist within our network or outside/with other issue i.e. dns
#down detector api? to know if issue is us or them
#
#computer hardware info
#ram usage
#processor usage
#disk usage
#disk type - for making suggestions
#computer software info (version, updates etc)
#uptime
#


#def nslookup(address)





#TESTING BELOW WHILE WRITING FUNCTIONS
hostname = socket.gethostname() #add try/excepts in case of no IP
ip_address = socket.gethostbyname(hostname)
linebreak()
print('\n\nDevice hostname: ',hostname)
print('IP Address: ', ip_address,'\n')
print('Processor: ', hardware()[0],'%')
print('RAM: ', hardware()[1],'%\n')
linebreak()

print('\nPing 8.8.8.8:\n', ping('8.8.8.8'))
linebreak()
print('\nResolve google.com:\n',resolve('www.google.com'),'\n\n\n')
input('Press enter to close.')
