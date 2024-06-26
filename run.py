import psutil;
import os;
import platform;
import datetime;

myOs = platform.system()

if(myOs == "Linux"):
    clear = "clear"
else:
    clear = "cls"


def bytes_to_gigas(value):
    return f'{value / 1024**3: .2f} GB'

def bytes_to_megas(value):
    return f'{value / 1024**2: .2f} MB'

def seconds_to_minutes(value):
    return f'{value / 60: .2f} minutos'

def seconds_to_hours(value):
    return f'{value / 60**2: .2f} horas'

isWorking = True

while(isWorking):
    os.system(clear)
    print("="*30)
    print("Monitoramento de hardware")
    print("="*30)
    print("[1] CPU")
    print("[2] Memória")
    print("[3] Rede")
    print("[4] Sensores")
    print("[5] Outras informações do sistema")
    print("[6] Sair")
    print("="*30)

    option = int(input("O que você quer monitorar?"))

    if(option == 1):
        os.system(clear)
        isWorkingCPU = True
        while(isWorkingCPU):

            print("="*30)
            print("Monitoramento da CPU")
            print("="*30)
            print("[1] Tempo de processamento")
            print("[2] Frequência")
            print("[3] Número de núcleos")
            print("[4] Utilização atual")
            print("[5] Voltar")
            print("="*30)
            option = int(input("O que você quer monitorar?"))

            if(option == 1):
                os.system(clear)
                user = seconds_to_hours(psutil.cpu_times().user)
                system = seconds_to_hours(psutil.cpu_times().system)
                idle = seconds_to_hours(psutil.cpu_times().idle)
                print("="*30)
                print("Tempo gasto por processamento: ")
                print("="*30)
                print("Usuário: ", user)
                print("Sistema: ", system)
                print("Inativo: ", idle)
                print("="*30)
                input("Aperte enter para voltar...")  
                os.system(clear)            
            elif(option == 2):
                os.system(clear)
                current = psutil.cpu_freq().current
                minF = psutil.cpu_freq().min
                maxF = psutil.cpu_freq().max

                print("="*30)
                print("Frequência da CPU: ")
                print("="*30)
                print("Frequência atual: ", current, "Mhz")
                print("Frequência mínima: ", minF, "Mhz")
                print("Frequência máxima: ", maxF, "Mhz")
                print("="*30)
                input("Aperte enter para voltar...")  
                os.system(clear) 
            elif(option == 3):
                os.system(clear)
                physicalCores = psutil.cpu_count(logical=False)
                logicalCores = psutil.cpu_count(logical=True)

                print("="*30)
                print("Número de núcleos: ")
                print("="*30)
                print("Núcleos físicos: ", physicalCores)
                print("Núcleos lógicos: ", logicalCores)
                print("="*30)
                input("Aperte enter para voltar...")  
                os.system(clear) 
            elif(option == 4):
                isWorkingCurrentUse = True

                print("="*30)
                print("Utilização atual: ")
                print("="*30)
                try:
                    while(isWorkingCurrentUse):
                        currentUse = psutil.cpu_percent(1)
                        print(currentUse, "%") 
                except KeyboardInterrupt:
                    pass
                    os.system(clear) 
            elif(option == 5):
                isWorkingCPU = False
    elif(option == 2):
        os.system(clear)
        isWorkingMemory = True
        while(isWorkingMemory):
            print("="*30)
            print("Monitoramento da memória")
            print("="*30)
            print("[1] Memória RAM")
            print("[2] Disco rígido")
            print("[3] Voltar")
            print("="*30)
            option = int(input("O que você quer monitorar?"))
                
            if(option == 1):
                os.system(clear)
                total = bytes_to_gigas(psutil.virtual_memory().total)
                used = bytes_to_gigas(psutil.virtual_memory().used)
                free = bytes_to_gigas(psutil.virtual_memory().free)

                print("="*30)
                print("Memória RAM: ")
                print("="*30)
                print("Total: ", total)
                print("Usado: ", used)
                print("Livre: ", free)
                print("="*30)
                input("Aperte enter para voltar...")  
                os.system(clear) 
            elif(option == 2):
                os.system(clear)
                total = bytes_to_gigas(psutil.disk_usage('/').total)
                used = bytes_to_gigas(psutil.disk_usage('/').used)
                free = bytes_to_gigas(psutil.disk_usage('/').free)

                print("="*30)
                print("Disco rígido: ")
                print("="*30)
                print("Total: ", total)
                print("Usado: ", used)
                print("Livre: ", free)
                print("="*30)
                input("Aperte enter para voltar...")  
                os.system(clear)
            elif(option == 3):
                isWorkingMemory = False 
    elif(option == 3):
        os.system(clear)
        isWorkingNetwork = True
        while(isWorkingNetwork):
            print("="*30)
            print("Monitoramento da rede")
            print("="*30)
            print("[1] Estatísticas de entrada e saída da rede")
            print("[2] Voltar")
            print("="*30)
            option = int(input("O que você quer monitorar?"))
            
            if(option == 1):
                os.system(clear)
                bytesSent = bytes_to_megas(psutil.net_io_counters().bytes_sent) 
                bytesRecv = bytes_to_megas(psutil.net_io_counters().bytes_recv)               

                print("="*30)
                print("Estatísticas de entrada e saída da rede: ")
                print("="*30)
                print("Megas enviados: ", bytesSent)
                print("Megas recebidos: ", bytesRecv)
                print("="*30)
                input("Aperte enter para voltar...")  
                os.system(clear) 
            elif(option == 2):
                isWorkingNetwork = False 
    elif(option == 4):
        os.system(clear)
        isWorkingSensors = True
        while(isWorkingSensors):
            print("="*30)
            print("Monitoramento de sensores")
            print("="*30)
            print("[1] Bateria")
            print("[2] Voltar")
            print("="*30)
            option = int(input("O que você quer monitorar?"))
            
            if(option == 1):
                os.system(clear)
                percent = psutil.sensors_battery().percent
                secsleft = seconds_to_hours(psutil.sensors_battery().secsleft)
                powerPlugged = psutil.sensors_battery().power_plugged   

                if(powerPlugged):
                    powerPlugged = 'Sim'
                else:
                    powerPlugged = 'Não'       

                print("="*30)
                print("Sensor da bateria: ")
                print("="*30)
                print("Bateria: ", round(percent), '%')
                print("Tempo restante: ", secsleft)
                print("Cabo de energia conectado: ", powerPlugged)
                print("="*30)
                input("Aperte enter para voltar...")  
                os.system(clear) 
            elif(option == 2):
                isWorkingSensors = False 
    elif(option == 5):
        os.system(clear)
        isWorkingOthers = True
        while(isWorkingOthers):
            print("="*30)
            print("Outras informações:")
            print("="*30)
            print("[1] Tempo de inicialização do sistema")
            print("[2] Usuários")
            print("[3] Voltar")

            print("="*30)
            option = int(input("O que você quer monitorar?"))
            
            if(option == 1):
                os.system(clear)        
                bootTime = psutil.boot_time() 
                dateTime = datetime.datetime.fromtimestamp(bootTime).strftime("%d-%m-%Y %H:%M:%S")

                print("="*30)
                print("Tempo de inicialização: ")
                print("="*30)
                print(dateTime)
                print("="*30)
                input("Aperte enter para voltar...")  
                os.system(clear) 
            elif(option == 2):
                os.system(clear)        
                started = psutil.users()[0].started
                dateTime = datetime.datetime.fromtimestamp(started).strftime("%d-%m-%Y %H:%M:%S")

                print("="*30)
                print("Dados dos usuários: ")
                print("="*30)
                print("Nome: ", psutil.users()[0].name)
                print("Host: ", psutil.users()[0].host)
                print("Ultima vez usado em: ", dateTime)
                    
                print("="*30)
                input("Aperte enter para voltar...")  
                os.system(clear) 
            elif(option == 3):
                isWorkingOthers = False 
    elif(option == 6):
        isWorking = False
        print("Saindo...")

