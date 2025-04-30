import asyncio
from agents.orchestrator import LixwiAgentOrchestrator
from semantic_kernel.agents import ChatHistoryAgentThread

async def main():
    orchestrator = LixwiAgentOrchestrator()
    agent = orchestrator.get_agent()
    thread: ChatHistoryAgentThread | None = None

    print("🧠 Lixwi Agent activo. Escribe 'exit' para salir.\n")
    while True:
        user_input = input("👤 Tú: ")
        if user_input.lower() in {"exit", "quit"}:
            break

        first_chunk = True
        async for response in agent.invoke_stream(messages=user_input, thread=thread):
            if first_chunk:
                print(f"🤖 {response.name}: ", end="", flush=True)
                first_chunk = False
            print(f"{response}", end="", flush=True)
            thread = response.thread
        print()

    if thread:
        await thread.delete()

if __name__ == "__main__":
    asyncio.run(main())
