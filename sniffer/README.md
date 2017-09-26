# Práctica con Wireshark

En este directorio encontrará varios recursos que le permitirán repetir las prácticas llevadas a cabo durante la clase alrededor del uso de los sniffers.

Para llevar a cabo estas prácticas se optó por usar herramientas que estaban instaladas en [contenedores](https://en.wikipedia.org/wiki/Docker_(software)) (a.k.a. máquinas virtuales livianas), con el propósito de evitar la instalación de dichas herramientas de forma permanente en el computador de quien lleva a cabo estas prácticas.

**Lo primero y mas importante** es instalar [Docker](https://docs.docker.com/engine/installation/) en su computador.

Una vez instalado Docker, usted deberá descargar algunos contenedores para llevar a cabo exitosamente la práctica.

1. El contenedor con el sniffer [Wireshark](https://hub.docker.com/r/manell/wireshark/)

```bash
docker pull manell/wireshark
```

2. El contenedor con el servidor web [Nginx](https://hub.docker.com/_/nginx/)

```bash
docker pull nginx
```

En este [video](https://youtu.be/3ucnHOPQmFk) usted podrá encontrar más detalles relacionados a la forma como se accede a estos contenedores.

---
# Prácticas

## Práctica web

Una primera práctica que debe llevar a cabo el estudiante es validar que se pueden observar los paquetes que se transfieren entre un servidor web y un cliente web (a.k.a. *web browser*). 
1. Se debe ejecutar el contenedor que tiene Wireshark.
2. Se ejecuta el contenedor que tiene el servidor web.
3. En la interfaz de Wireshark, dentro de las opciones de tarjetas de red disponibles para monitorear se selecciona la que tiene la etiqueta `any`.
4. Al abrirse una "nueva" ventana, en el campo de texto que tiene la palabra `filtro` o `filter` colocar la expresión `tcp.port == 80`.
5. Vaya a un *web browser* y acceda al URL `http://localhost:8080`.
6. Analizar los paquetes que se ven en la interacción.

--- 

## Práctica Telnet

Una segunda práctica que se propone es la que tiene que ver con el servicio de red [telnet](https://en.wikipedia.org/wiki/Telnet). 
Para ello lleve a cabo los siguientes pasos: 

1. Descargar los archivos `Dockerfile` y `telnet` que están en la carpeta [telnet](https://github.com/josanabr/computernetworks/tree/master/sniffer/telnet) a una carpeta nueva.

2. Estando en dicha carpeta ejecute lo siguiente

```bash
docker build -t jstelnet .
```

3. Una vez termine la ejecución del comando anterior, ejecute el siguiente comando

```bash
docker run --rm -it -p 2323:23 jstelnet
```

4. Vaya al programa `Wireshark` y cambie en el campo filtro `tcp.port == 80` por el identificador de puerto del servicio `telnet`.

Evidencie lo débil que es el servicio `telnet` y la razón por la cual hoy no es tan popular.
Para ello, limpie todos los paquetes analizados hasta el momento por el Wireshark y desde una terminal ejecute el comando `telnet localhost 2323`. 
Cuando se le pregunte por el **login** digite `usuario` y por el password digite `usuario`.

Observe que el servicio `telnet` envía un dato o caracter a la vez.

---

**Sin embargo** el comando `telnet` nos permite validar la disponibilidad de servicios como el de un servidor web.

Entendiendo que usted tiene corriendo el servidor `nginx` ejecute los siguientes comandos

```bash
telnet localhost 8080
GET /index.html HTTP/1.1
host: localhost

```

**Recuerde** que para indicar la terminación de una petición HTTP es necesario ejecutar **dos veces** la tecla **ENTER** después de digitar `host: localhost`.

El comando `telnet` nos permite acceder a servicios de red sin necesidad de utilizar las herramientas naturales que se usan para acceder a dichos servicios. 

---

## Práctica SSH

De forma similar usted ahora debe evidenciar porque un servicio como el `ssh` es mas seguro que el `telnet`.

Para ello vamos a crear un contenedor con el servicio de SSH. 
Para ello ejecute los siguientes pasos: 

1. Descargue el archivo `Dockerfile` que esta en esta en [dirección](https://github.com/josanabr/computernetworks/tree/master/sniffer/ssh) en una carpeta nueva. 
2. Ejecute el siguiente comando estando en la carpeta donde descargó el archivo `Dockerfile`

```bash
docker build -t jsssh .
```

3. Una vez termine la ejecución del comando, ejecute el contenedor de la siguiente manera

```bash
docker run --rm -d -p 3333:22 jsssh
```

Pasos que usted debe seguir para monitorear el tráfico `ssh` entre su computador y el contenedor:

1. Modificar el campo `filtro` dentro de Wireshark para que se escuche por el puerto del servicio que estamos corriendo para este ejemplo, en este caso `3333`.

2. Desde una terminal ejecutar el siguiente comando `ssh -p 3333 localhost`.

¿Cómo se da cuenta que efectivamente los datos que se envían por `ssh` no se pueden entender?

---

# Tarea servicio de red FTP

Usted deberá describir una práctica de acceso al servicio de red FTP similar a la forma como se hizo en esta guía para los servicios web, telnet y ssh (en archivo de Google Drive la descripción). 

Usted deberá además presentar un video no mayor a 5 minutos donde se evidencie como el protocolo de red FTP tampoco es seguro.

Ideas de como llevar a cabo esta práctica

1. Descargar un contenedor con el servicio de red FTP.
2. Ejecutar dicho contenedor.
3. Probar que desde una terminal usted puede acceder al servicio de FTP, [enlace 1](https://kb.globalscape.com/KnowledgebaseArticle10224.aspx) [enlace 2](http://www.tburke.net/info/misc/cmdline-ftp.htm).
4. Analizar el tráfico de red usando Wireshark. 
Algo clave es que FTP usa dos puertos a la hora de interactuar con un cliente, un puerto de comandos y otro puerto para transferir datos. Esto lo debes tener en cuenta para poder tener éxito en la tarea.
