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

