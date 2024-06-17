from langchain_community.embeddings.ollama import OllamaEmbeddings

def cust_embedding_function(model_name: str):
    '''
    returns OllamaEmbedings function, with the specified model_name, to populate and query a vector database
    '''
    embeddings = OllamaEmbeddings(model = model_name)
    return embeddings