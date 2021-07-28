import subprocess, threading
import os, time
from pyfiglet import Figlet
ip= ("10.0.0.21") # Si
#ip= (192.168.1.2) # No
x = 1
class GLOBALES():
    pass
Gb = GLOBALES()
Gb.Alarma = ''
def BannerIni(St):
    custom_fig = Figlet(font='cybermedium')
    print(custom_fig.renderText('ALARMA ANTENA!!'))
    if St == 1:
        print('Presione ENTER para salir...')
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
def ping(ip):
    clearConsole()
    BannerIni(0)
    time.sleep(1)
    PingStatus = subprocess.Popen(['ping', '-w', '2', ip])
    PingStatus.wait()
    clearConsole()
    return 'Y' if PingStatus.poll()==0 else 'N'
    
def alarma():
  #  print('inicio while')
    while True:
        if Gb.Alarma == 'start':
            BannerIni(1)
            print('AHHHHhhhhh')
            os.system('play -nq -t alsa synth {} sine {}'.format(1, 320))
            time.sleep(0.5)
            clearConsole()
        

if __name__ == '__main__':
     BannerIni(0)
     alarma= threading.Thread(target=alarma, daemon=True)    
     alarma.start()

     while True:
        t= ping(ip)
        if t == "Y":
            print('Si esta')
        else:
            Gb.Alarma = 'start'
            break
     try:
         input('Presione ENTER para salir...')
     except SyntaxError:
        pass
    #prgrama ds