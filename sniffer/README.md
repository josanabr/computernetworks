# Práctica con Wireshark

En este directorio encontrará varios recursos que le permitirán repetir las prácticas llevadas a cabo durante la clase alrededor del uso de los sniffers.

Para llevar a cabo estas prácticas se optó por usar herramientas que estaban instaladas en contenedores (a.k.a. máquinas virtuales livianas), con el propósito de evitar la instalación de dichas herramientas de forma permanente en el computador de quien lleva a cabo estas prácticas.

**Lo primero y mas importante** es instalar [Docker](https://docs.docker.com/engine/installation/) en su computador.

Una vez instalado Docker, usted deberá descargar algunos [contenedores](https://en.wikipedia.org/wiki/Docker_(software)) para llevar a cabo exitosamente la práctica.

1. El contenedor con el sniffer [Wireshark](https://hub.docker.com/r/manell/wireshark/)

```bash
docker pull manell/wireshark
```

2. El contenedor con el servidor web [Nginx](https://hub.docker.com/_/nginx/)

```bash
docker pull nginx
```

En este [video](https://youtu.be/3ucnHOPQmFk) usted podrá encontrar más detalles relacionados a la forma como se usan estos contenedores.

---

Una primera práctica que debe llevar a cabo el estudiante es validar que se pueden observar los paquetes que se transfieren entre un servidor web y un cliente web (a.k.a. web browser). 
1. Se debe ejecutar el contenedor que tiene Wireshark.
2. Se ejecuta el contenedor que tiene el servidor web.
3. Dentro de las opciones de tarjetas de red disponibles para monitorear se selecciona la etiqueta `any`.
4. En el campo de texto que tiene la palabra `filtro` o `filter` colocar la expresión `tcp.port == 80`.
5. Analizar los paquetes que se ven en la interacción.

--- 

Una segunda práctica que se propone es la que tiene que ver con el servicio de red `telnet`. 
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

**Sin embargo** el comando `telnet` nos permite validar la disponibilidad de servicios como el de un servidor web.

Entendiendo que usted tiene corriendo el servidor `nginx` ejecute los siguientes comandos

```bash
telnet localhost 8080
GET /index.html HTTP/1.1
host: localhost

```

**Recuerde** que para indicar la terminación de una petición HTTP es necesario ejecutar **dos veces** la tecla **ENTER** después de digitar `host: localhost`.
