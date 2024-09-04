# anthropic-chat

🎭 Obras de William Shakespeare con API de Anthropic 🎭

Esta es una aplicación web desarrollada con Streamlit que permite a los usuarios ingresar el título de su obra preferida de William Shakespeare y obtener un resumen interpretado de la misma. La aplicación utiliza la API de Anthropic para generar resúmenes precisos y amigables, con la opción de continuar explorando otras obras.

## Funcionalidades

- **Interfaz amigable**: El script app.py configura una interfaz intuitiva y sencilla donde los usuarios pueden ingresar su obra favorita.
- **Resúmenes automatizados**: Genera automáticamente un resumen de la obra ingresada.
- **Interacción adicional**: La aplicación interactúa con el usuario preguntando si desea explorar más sobre la obra o consultar otras.

Para comenzar a utilizar esta aplicación interactiva de Shakespeare utilizando la API de Anthropic, sigue los siguientes pasos:

   Clave de API de Anthropic: Asegúrate de tener una 
   clave de API de Anthropic y configúrala en tus 
   variables de entorno como ANTHROPIC_API_KEY.

## Requisitos

- Python 3.x
- Streamlit
- Anthropic SDK

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/CRISHFAS/anthropic-chat.git
```
2. Instala las dependencias necesarias:

```bash
pip install streamlit anthropic
```

3. Ejecuta el script app.py para iniciar la aplicación en Streamlit

```bash
streamlit run app.py
```

## Uso

Ingresa el título de la obra de Shakespeare que deseas interpretar en el cuadro de texto.
Haz clic en el botón "Leer".
La aplicación mostrará un resumen interpretado de la obra ingresada.

### Definiciones de funciones

Interfaz amigable: La aplicación presenta una interfaz limpia con un diseño en gradiente que destaca el título.
Generación de resúmenes: Mediante la función call_claude, se envía la consulta del usuario a la API de Anthropic y se transmite la respuesta a la interfaz de Streamlit.
Interacción continua: La aplicación no solo ofrece resúmenes, sino que también pregunta al usuario si desea explorar más obras, fomentando la interacción continua

### Puedes probar la aplicación en el siguiente enlace:
Aquí puedes ver un video que muestra el funcionamiento de la aplicación: [Ver Video de Demostración](./media/demo.mp4)

Si deseas, puedes agregar nuevas características o mejorar el código, por favor abre un pull request.

# Las contribuciones son bienvenidas !!.


<img class="giphy-gif-img giphy-img-loaded" src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzN0bG93ZG1qemN0YTI0M3gybWF5MDhsM2hnY3UydWVpcXI5emRjcyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Tm6sAHdRmdgzK/giphy.gif" width="100%" height="100%" alt="El mejor GIF de abrazo de tinta de Oxygen" style="background: rgba(0, 0, 0, 0);">