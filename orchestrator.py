import os
import importlib
from dotenv import load_dotenv
from openai import AsyncOpenAI
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.agents import ChatCompletionAgent

class LixwiAgentOrchestrator:
    def __init__(self):
        load_dotenv()
        self.plugins = self._load_plugins()

        # Crear cliente LLM
        self.client = AsyncOpenAI(
            api_key=os.getenv("GITHUB_TOKEN"),
            base_url=os.getenv("GITHUB_ENDPOINT")
        )

        # Servicio compatible con OpenAI API
        self.chat_completion_service = OpenAIChatCompletion(
            ai_model_id=os.getenv("GITHUB_MODEL"),
            async_client=self.client
        )

        # Crear agente con todos los plugins cargados
        self.agent = ChatCompletionAgent(
            service=self.chat_completion_service,
            plugins=self.plugins,
            name="LixwiMathTutor",
            instructions="Eres un agente educativo experto en matemáticas avanzadas. Ayuda al usuario con explicaciones o resolución simbólica."
        )

    def _load_plugins(self):
        plugins_dir = os.path.join(os.path.dirname(__file__), "plugins")
        plugin_instances = []

        for filename in os.listdir(plugins_dir):
            if filename.endswith("_plugin.py"):
                module_name = f"plugins.{filename[:-3]}"
                module = importlib.import_module(module_name)
                # Convención: el plugin debe tener una clase con el mismo nombre en CamelCase
                class_name = ''.join(part.capitalize() for part in filename.replace("_plugin.py", "").split('_')) + "Plugin"
                plugin_class = getattr(module, class_name)
                plugin_instances.append(plugin_class())

        return plugin_instances

    def get_agent(self):
        return self.agent
