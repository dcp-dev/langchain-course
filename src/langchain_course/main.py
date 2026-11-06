from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="http://127.0.0.1:8080/v1",
    api_key="local-only",      # ignorée par le serveur, mais obligatoire côté client
    model="mirai-s-27b",
    temperature=1.0,           # valeurs par défaut du serveur : temp 1.0, top_p 0.95
)

print(llm.invoke("Dis bonjour en une phrase.").content)