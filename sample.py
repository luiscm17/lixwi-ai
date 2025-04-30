import os 
from typing import Annotated
from openai import AsyncOpenAI
from dotenv import load_dotenv
from semantic_kernel.agents import ChatCompletionAgent, ChatHistoryAgentThread
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.functions import kernel_function
import random
import asyncio  # Añadido para manejar async/await

class DestinationsPlugin:
    """A List of Random Destinations for a vacation."""

    def __init__(self):
        # List of vacation destinations
        self.destinations = [
            "Barcelona, Spain",
            "Paris, France",
            "Berlin, Germany",
            "Tokyo, Japan",
            "Sydney, Australia",
            "New York, USA",
            "Cairo, Egypt",
            "Cape Town, South Africa",
            "Rio de Janeiro, Brazil",
            "Bali, Indonesia"
        ]
        # Track last destination to avoid repeats
        self.last_destination = None

    @kernel_function(description="Provides a random vacation destination.")
    def get_random_destination(self) -> Annotated[str, "Returns a random vacation destination."]:
        # Get available destinations (excluding last one if possible)
        available_destinations = self.destinations.copy()
        if self.last_destination and len(available_destinations) > 1:
            available_destinations.remove(self.last_destination)

        # Select a random destination
        destination = random.choice(available_destinations)

        # Update the last destination
        self.last_destination = destination

        return destination

# Cargar variables de entorno al inicio
load_dotenv()

# Configurar el cliente de OpenAI con variables de entorno
client = AsyncOpenAI(
    api_key=os.getenv("GITHUB_TOKEN"),  # Usar getenv en lugar de environ.get
    base_url=os.getenv("GITHUB_ENDPOINT"),  # Corregido para usar variable de entorno
)

# Crear el servicio de chat completion
chat_completion_service = OpenAIChatCompletion(
    ai_model_id=os.getenv("GITHUB_MODEL"),  # Usar variable de entorno
    async_client=client,
)

# Crear el agente
agent = ChatCompletionAgent(
    service=chat_completion_service, 
    plugins=[DestinationsPlugin()],
    name="TravelAgent",
    instructions="You are a helpful AI Agent that can help plan vacations for customers at random destinations",
)

async def main():
    # Create a new thread for the agent
    # If no thread is provided, a new thread will be
    # created and returned with the initial response
    thread: ChatHistoryAgentThread | None = None

    user_inputs = [
        "Plan me a day trip.",
    ]

    for user_input in user_inputs:
        print(f"# User: {user_input}\n")
        first_chunk = True
        async for response in agent.invoke_stream(
            messages=user_input, thread=thread,
        ):
            # 5. Print the response
            if first_chunk:
                print(f"# {response.name}: ", end="", flush=True)
                first_chunk = False
            print(f"{response}", end="", flush=True)
            thread = response.thread
        print()

    if thread:
        await thread.delete()

# Ejecutar el programa principal
if __name__ == "__main__":
    asyncio.run(main())
