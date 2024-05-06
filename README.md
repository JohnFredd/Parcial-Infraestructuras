# Parcial-Infraestructuras

## Integrantes
- John Freddy Belalcázar Rojas - john.freddy.belalcazar@correounivalle.edu.co - 2182464
- Laura Murillas Andrade - laura.murillas@correounivalle.edu.co - 1944153

## Descripción de requerimientos
- Instalar la librería yt-dlp: pip install yt-dlp
- Instalar la librería ffmpeg: pip install ffmpeg-python
- Instalar ffmpeg de la pagina oficial y ubicarlo en el directorio raíz del proyecto

## Forma de uso o ejecución
Para ejecutar el programa se debe:
- Encontrar el archivo /static/channels.json
- Modificar el archivo channels.json con las url de los canales de los cuales se desea descargar los videos
- Abrir el archivo correspondiente a la versión que se desea ejecutar: main.py(Secuencial), mainMultithreading.py, mainMultiprocessing.py
- En caso de no ser el archivo secuencial, localizar la variable maxThreads, maxProcesses y modificarla con el numero de hilos/procesos que se desea ejecutar el programa
- Ejecutar el script
- Se creará una carpeta audio donde se organizarán los audios resultantes.

## Descripción logica del aplicativo
El aplicativo sigue la siguiente lógica de funcionamiento:
- Se instancia la clase Reader y se le pide leer el JSON que contiene los enlaces de los canales
- La clase Reader abre el archivo
- La clase Reader genera un diccionario que contiene una clave, valor por cada url en el archivo
- Para obtener la clave y el valor que se deben registrar se llama a la función extractChannelInformation() la cual dada una url de un canal de yt mediante la librería yt-dlp consulta la informacion del canal y retorna como clave el titulo del canal y como valor un arreglo que contiene 5 arreglos correspondientes a los últimos 5 videos de ese canal, donde se guarda en la posicion 0 la url del video y en la posicion 1 el nombre del video el cual fue previamente purgado de caracteres especiales por la función cleanFileName()
- Se registra en el archivo de registro el inicio de la ejecucion del programa
- Se itera sobre el diccionario que devolvio la clase Reader
- En cada iteracion se instancia un objeto de la clase Downloader al cual se le pasan como atributos el nombre del canal, el titulo del video que ya fue purgado y la ruta al archivo de registro
- Se le pide a la clase Downloader que descargue el archivo, esta función retorna la ruta local donde el video fue descargado, esta ruta se le pasa como atributo a la función convert() de la clase Converter que se encarga de convertir el video ya instalado a formato mp3
- Para la descarga del video la clase Downloader extrae la informacion del video y lo descarga en la ruta personalizada que se define al instanciar la clase mediante los atributos del nombre del canal y el nombre del video
- Despues recopila la información necesaria y la agrega al archivo de registro
- Por último retorna la ruta donde se descargo el video
- La función convert() de la clase Converter convierte el video a audio mediante la libreria ffmpeg
- Por último se borra el video Original
- Se calcula el tiempo de ejecución del programa
