lixwi_ai_agent/
├── main.py                          # Punto de entrada, instancia SK + agentes
├── config/
│   └── sk_config.yaml               # Configuración de kernel, plugins, modelos
├── agents/
│   ├── orchestrator.py             # Agente central que enruta y coordina
│   └── intent_router.py            # Determina tipo de tarea (resolver, explicar)
├── plugins/
│   ├── solve_equation/             # Resolver problemas matemáticos
│   │   ├── skprompt.txt            # Prompt semántico
│   │   ├── function.py             # Llamado a SymPy o LLM
│   │   └── config.json             # Metadata del plugin
│   ├── explain_concept/            # Explicación teórica
│   ├── generate_quiz/              # (Opcional) evaluación personalizada
│   └── evaluate_answer/            # Validación de respuestas
├── tools/
│   ├── sympy_tools.py              # Funciones auxiliares para cálculos simbólicos
│   ├── vector_search.py            # Embeddings + búsqueda (opcional)
│   └── llm_client.py               # Cliente para modelo open-source
├── responsible_ai/
│   ├── logger.py                   # Registro de decisiones y acciones
│   ├── explainability.py           # Justificación de respuestas
│   └── bias_checker.py             # Control de sesgos o errores críticos
├── tests/
│   └── test_plugins.py             # Tests de unidad para plugins y lógica
├── requirements.txt
└── README.md
