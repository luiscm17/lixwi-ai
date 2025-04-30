lixwi_ai_agent/
├── App.py                          # Chainlit app
├── main.py                          
├── config/
│   ├── sk_config.py                # Python > YAML (type hints + autocompletado)
│   └── settings.py                 # Secrets, API keys (con dotenv)
├── agents/
│   ├── orchestrator.py             
│   ├── task_classifier.py          # Renombrar "intent_router" (clasifica ejercicios)
│   └── session_state.py            # Nueva clase para manejar estado del usuario
├── plugins/
│   ├── math/                       # Agrupar por materia (escalable a física/química)
│   │   ├── equation_solver/        # Plugin específico
│   │   │   ├── native_function.py  # Lógica SymPy
│   │   │   ├── semantic_function/  # Prompt engineering + LLM
│   │   │   │   ├── skprompt.txt    
│   │   │   │   └── config.json     
│   │   │   └── tests/              # Tests por plugin
│   │   └── theory_explainer/       # Explicaciones con RAG
│   └── core/                       # Funciones transversales
│       ├── feedback_handler/       # Evaluaciones de estudiantes
│       └── error_reporter/         # Reporte de errores en respuestas
├── services/                       # Renombrar "tools/"
│   ├── llm/
│   │   ├── openai_client.py        # GPT-4
│   │   └── local_llm.py            # Mistral/Llama (opcional)
│   ├── vector_db.py                # ChromaDB/Pinecone
│   └── symbolic_math.py            # SymPy/Wolfram
├── responsible_ai/
│   ├── audit_logger.py             # Registro detallado (más que solo logger.py)
│   ├── fairness_checker.py         # Análisis de sesgos con Fairlearn
│   └── explanation_generator.py    # Explicaciones tipo XAI
├── tests/
│   ├── unit/                       # Tests unitarios
│   └── integration/                # Tests de flujos completos
├── docker/                         # Configuración Docker
│   ├── Dockerfile
│   └── docker-compose.yml
├── docs/                           # Documentación técnica y pedagógica
├── Makefile                        # Automatización de tareas
└── README.md