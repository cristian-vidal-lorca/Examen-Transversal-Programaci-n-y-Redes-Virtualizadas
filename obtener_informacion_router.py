import netmiko
from netmiko import ConnectHandler

# Información del router
cisco1 = {
    "ip": "192.168.56.101",
    "device_type": "cisco_ios",
    "username": "cisco",
    "password": "cisco123!",
}

# Conectar al router y ejecutar comandos
with ConnectHandler(**cisco1) as net_connect:
    # Obtener información de IP y estado de las interfaces
    command1 = "show ip interface brief"
    output1 = net_connect.send_command(command1)
    print("\nInformación de IP y estado de las interfaces:")
    print(output1)

    # Obtener el running-config
    command2 = "show running-config"
    output2 = net_connect.send_command(command2)
    print("\nRunning-config:")
    print(output2)

    # Obtener el show version
    command3 = "show version"
    output3 = net_connect.send_command(command3)
    print("\nShow version:")
    print(output3)
