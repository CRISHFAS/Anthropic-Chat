import streamlit as st 
import anthropic

st.markdown(
    """
    <style>
    .title-gradient {
        background: linear-gradient(90deg, #ff7e5f, #feb47b);  /* Gradiente de color */
        -webkit-background-clip: text;
        color: transparent;
        font-size: 2.5em;
        font-weight: bold;
        text-align: center;
    }
    </style>
    <h1 class="title-gradient">Obras de William Shakespeare</h1>
    """,
    unsafe_allow_html=True
)

api_key="Your_api_key"

poema_input = st.text_area("Ingresa tu obra preferida", height=100)

if st.button("Leer"):
    if poema_input:
        client = anthropic.Anthropic(
            api_key=api_key)
        
        message = client.messages.create(
            model = "claude-3-5-sonnet-20240620",
            max_tokens= 3500,
            temperature= 1,
            system= """Eres un asistente de IA con un profundo conocimiento sobre las obras de William Shakespeare.
            Tu tarea es proporcionar a los usuarios un breve resumen de sus obras y sobre qué trata cada una de ellas,tambien debes ser amigable preguntando al lector si le interesa saber más o leer alguna otra obra.""",
            messages= [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": poema_input
                        }
                    ]
                }
            ]
        )
        
        st.subheader("Obra interpretada:")
        interpretation_text = message.content[0].text if message.content else "No se encuentra la obra requerida."
        st.write(interpretation_text)
    else:
        st.warning("Ingresa tu obra para poder interpretarlo.")
        