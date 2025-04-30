# 🤖 Lixwi AI Math Agent

## 📝 Descripción
Lixwi AI Math Agent es un asistente matemático inteligente construido con Semantic Kernel y OpenAI. El agente puede resolver problemas matemáticos, explicar conceptos y proporcionar asistencia paso a paso en la resolución de ecuaciones.

## ✨ Características
- 🧮 Resolución de ecuaciones matemáticas
- 📚 Explicación detallada paso a paso
- 🔄 Procesamiento simbólico con SymPy
- 💻 Interfaz web con Chainlit
- 🤝 Integración con Semantic Kernel

## 🛠️ Tecnologías
- Python 3.8+
- Semantic Kernel
- OpenAI API
- SymPy
- Chainlit

## 📋 Requisitos Previos
- Python 3.8 o superior
- Cuenta de OpenAI con API key
- Variables de entorno configuradas

## ⚙️ Configuración
1. Clona el repositorio
```bash
git clone https://github.com/yourusername/ai-agent.git
cd ai-agent
```

2. Instala las dependencias
```bash
pip install -r requirements.txt
```

3. Configura las variables de entorno
```bash
GITHUB_TOKEN=tu_openai_api_key
GITHUB_ENDPOINT=tu_endpoint
GITHUB_MODEL=tu_modelo
```

## 🚀 Uso
### Interfaz Web (Chainlit)
```bash
chainlit run App.py -w
```

## 📁 Estructura del Proyecto

lixwi_ai_agent/
├── main.py                 # Punto de entrada consola
├── App.py                  # Interfaz web Chainlit
├── agents/
│   └── orchestrator.py     # Orquestador principal
├── plugins/                # Plugins semánticos
├── tools/                  # Herramientas auxiliares
└── tests/                  # Tests unitarios

## 🤝 Contribuir
Las contribuciones son bienvenidas. Por favor, abre un issue para discutir los cambios propuestos.

## 📄 Licencia
Este proyecto está bajo la Licencia MIT.

## ✨ Agradecimientos
- Semantic Kernel
- OpenAI
- Chainlit
- SymPy