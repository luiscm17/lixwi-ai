import os
import chainlit as cl
from dotenv import load_dotenv
from orchestrator import LixwiAgentOrchestrator
from semantic_kernel.agents import ChatHistoryAgentThread

# Cargar variables de entorno
load_dotenv()

# Inicializar el orquestador y obtener el agente
orchestrator = LixwiAgentOrchestrator()
agent = orchestrator.get_agent()

# Crear un hilo de conversación
thread: ChatHistoryAgentThread | None = None

@cl.on_message
async def handle_message(message: cl.Message):
    global thread
    user_input = message.content

    response_text = ""
    async for response in agent.invoke_stream(messages=user_input, thread=thread):
        response_text += str(response)
        thread = response.thread

    await cl.Message(content=response_text.strip(), author="LixwiAgent").send()
