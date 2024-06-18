import argparse

from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

from cust_embedding_function import cust_embedding_function


PATH_TO_DATABASE = "../database/"
PATH_TO_DATA = "../data"
MODEL_NAME = 'llama3'


PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="query text for prompt")
    args = parser.parse_args()
    query_text = args.query_text
    query_rag(query_text)


def query_rag(query_text: str):
    # Prepare the datbase
    embedding_function = cust_embedding_function(MODEL_NAME)
    db = Chroma(
        persist_directory=PATH_TO_DATABASE, 
        embedding_function=embedding_function
        )

    # Search the database
    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = Ollama(model=MODEL_NAME)
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\n\nSources:\n"
    print(formatted_response)

    for source in sources:
        print(source) 
    
    return response_text


if __name__ == "__main__":
    main()
