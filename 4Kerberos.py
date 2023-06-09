import subprocess
import re

def ejecutar_comando(comando):
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    if resultado.returncode == 0:
        print("Salida:")
       # print(resultado.stdout)
    else:
        print("Error:")
       # print(resultado.stderr)

comando = 'sudo nmap -p- -open -sS -vvv --min-rate 5000 -n -Pn ip -oG allPorts'
ejecutar_comando(comando)

def cat_allPorts(comando):
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    if resultado.returncode == 0:
        print("Contenido del archivo allPorts:")
    #    print(resultado.stdout)
    else:
        print("Error:")
    #   print(resultado.stderr)

comandoCat = 'cat allPorts'
cat_allPorts(comandoCat)


def extractPorts(filename):
    with open(filename, 'r') as file:
        content = file.read()

    ports = re.findall(r'\d{1,5}/open', content)
    ports = [port.split('/')[0] for port in ports]
    ports = ','.join(ports)

    ip_address = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', content)
    ip_address = sorted(set(ip_address))[0]

    output = f"[*] Extracting information...\n\n"
    output += f"\t[*] IP Address: {ip_address}\n"
    output += f"\t[*] Open ports: {ports}\n\n"
    
   if '88' in output:
    print("Se ha encontrado Kerberos")
   else:
    print("No se ha encontrado Kerberos")
    
    with open("extractPorts.tmp", "w") as tmp_file:
        tmp_file.write(output)

    subprocess.run(["batcat", "extractPorts.tmp"])
    subprocess.run(["rm", "extractPorts.tmp"])

# Ejemplo de uso
extractPorts("allPorts")
