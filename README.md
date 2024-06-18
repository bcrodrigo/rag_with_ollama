# rag_with_ollama

Repository to test out RAG using Ollama locally on my computer.

## Background and Motivation

Retrieval Augmented Generation (RAG) is a process to optimize the output of a Large Language Model (LLM) so that it references sources outside of its training data before generating a response [^1]. This is a less computationally expensive process, compared to fine-tuning, where selected weights of the model are actually updated in order to account for new items.

In this small project I want to setup my computer to interact with LLMs locally, on device, without using an API call. This will enable a workflow that I can use to read and query documents (mainly pdfs) without privacy concerns or limits to the number of tokens to be used by the LLM.

Additionally, these scripts will provide a building block for Natural Language Processing tasks, as there is a necessity to convert text into embeddings, and LLMs already do this by default.

## Installation Procedure

1. Install [Ollama](https://ollama.com/) and review main commands.
```bash
ollama pull <model_name>
ollama rm <model_name>
ollama list
ollama serve
```

2. Clone this repository
3. Install the requirements with
```bash
pip install -r requirements.txt
```



4. Setup Vector Database
I'll use an open source database, that I can run locally. I'll start with Chroma.

6. Setup embeddings function
I will use `OllamaEmbeddings()` with the selected LLM.


## Usage

### Preparation
- Review the available models at https://ollama.com/library. Note that it's recommended that:
	You should have at least 8 GB of RAM available to run the 7B models, 16 GB to run the 13B models, and 32 GB to run the 33B models. 
- Select LLM:  due to memory constrains I've selected `llama3` in all scripts
- Start a local Ollama server
```bash
ollama serve
```
### Adding documents to the database

- Move your pdf documents to the `data/` folder then run 
- Run  `create_or_add_to_database.py`
### Querying the database




## Challenges and Recommendations

- Choice of database:
I use ChromaDB, but there are other options

- Choice of embeddings
I use `OllamaEmbeddings()` with the required model, but there are other options

- Consistency and repeatability of responses
- Evaluation of 
- Deployment and the necessity of an API key

## References
https://github.com/ollama/ollama

[^1]: https://aws.amazon.com/what-is/retrieval-augmented-generation/
