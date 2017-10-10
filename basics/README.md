# README.md

Este directorio contiene ejemplos de programas de red escritos en Python. 
Los ejemplos se basan en los ejemplos del libro [Python Network Programming Cookbook - Second Edition](https://www.amazon.com/Python-Network-Programming-Cookbook-Second-ebook/dp/B073V2PDPF/ref=sr_1_1?ie=UTF8&qid=1507039527&sr=8-1&keywords=python+network+programming+cookbook+-+second+edition).

Descripción de los directorios en este repositorio.

* [01-socket-utils](01-socket-utils) contiene varios ejemplos básicos de programas de red en Python, e.g. abrir un socket, como redefinir la utilización de un socket, consultar por nombres de servicios, etc. 
Una descripción de las actividades a hacer en este directorio se describe [aquí](https://docs.google.com/a/correounivalle.edu.co/document/d/1b3p-bW66SLxTmQwygN38oc0u0MkzLFq4FwbD3bI0Kp4/edit?usp=sharing).

* [socket-http-client](socket-http-client) código en python para acceder a un cliente web. 
Usted debe completar dicho cliente de la siguiente manera. 
Revise el código y en cada comentario que encuentre la palabra `COMPLETE (n)` debe introducir el código en Python que le indica el numeral `(n)`. 
A continuación las pistas de lo que debe poner en el código:

 1. Instancie una variable llamada `s` que es de tipo socket y utiliza el protocolo TCP para la comunicación.
 2. Defina una variable llamada `port` y almacene en ella el valor entero `80`.
 3. Encuentre el IP del servidor que se encuentra en la variable `host` y guárdelo en una variable llamada `remote_ip`.
 4. Imprima un mensaje por pantalla que diga el siguiente mensaje `La dirección IP de www.google.com es 216.58.192.100`. El número IP `216.58.192.100` y `www.google.com` se deben tomar de las variables `remote_ip` y `host`, respectivamente.
 5. Defina una tupla llamada `endpoint` y que consta de los valores en las variables `remote_ip` y `port`.
 6. Utilice la variable `s` y su método `connect` con argumento la variable `endpoint` para llevar a cabo el proceso de conexión.
 7. Utilice un método de la variable `s` para enviar los datos al servidor.
 8. Utilice un método de la variable `s` para recibir los datos de respuesta del servidor y los almacena en una nueva variable llamada `reply`. 

* [another-simple-http-server](another-simple-http-server), similar al ejemplo del punto anterior, usted debe completar el código de acuerdo a lo descrito en los siguientes numerales:

 1. Instancie una variable llamada `ss` que es de tipo socket y utiliza el protocolo TCP para la comunicación.
 2. Defina una tupla llamada `endpoint` y que consta de los valores en las variables `''` y `args.port`.
 3. Utilice los métodos necesarios para asociar el socket a la tupla definia anteriormente e indíquele al sistema operativo el máximo número de conexiones que este debe atender en caso que el servidor web no lo pueda hacer inmediatamente. **HINT** Los métodos son `bind` y `listen`.
 4. Siga las instrucciones que se indican en el código fuente
