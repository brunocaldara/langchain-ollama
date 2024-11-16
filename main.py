from langchain_ollama.chat_models import ChatOllama

llm = ChatOllama(
    model='llama3.1:latest',
    temperature=0,
)

response = llm.invoke('Conte uma piada')
print(response)
