# Utilidades de la clase `socket` en Python

Cada aplicación se puede correr de la siguiente manera:

```
python <python file.py>
```

Donde `<python file.py>` es el nombre de un archivo de este directorio.

A continuación se describen los siguientes códigos:

1. `01-local_machine_info.py` da la información del nombre de la máquina y su IP.
2. `02-remote_machine_info.py` da el número dado un nombre de máquina. Cambie `www.python.org` por `www.python.mx`.
3. `04-finding_service_name.py` se revela información de los protocolos existentes dado un número de puerto.
4. `10-reuse_socket_address.py` se presenta la instrucción que permite que un puerto de red sea reutilizado.
5. `11-print_machine_time.py` ¿Qué es el servicio de NTP? 
6. `13a-echo_server.py` y `13b-echo-client.py` muestran la forma como se intercambian datos un cliente y un servidor usando el protocolo TCP. Revise los datos que viajan usando wireshark.
7. `14a-echo_server_udp.py` y `14b_echo_client_udp.py` muestra la forma como se intercambian datos un cliente y un servidor usando el protocolo UDP. Revise los datos que viajan usando wireshark.

## Preguntas

1. En el punto 6, el cliente recibía del servidor bloques de 16 bytes. ¿Por qué no se pueden recibir múltiples bloques de 16 bytes en una conexión UDP?
2. ¿Qué pasa si se ejecutan dos veces el servidor de TCP sobre un mismo puerto, e.g. 8888?
3. ¿Qué pasa si se ejecutan dos veces el servidor de UDP sobre un mismo puerto, e.g. 8888?
4. ¿Qué pasa si se ejecuta una instancia del servidor TCP y otra instancia del servidor UDP sobre el mismo identificador de puerto, e.g. 8888?
