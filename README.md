# rag_with_ollama

Repository to test out RAG using Ollama locally on my computer.

## Motivation
To setup my computer to interact with LLMs without using an API call, locally, and on device.
This will enable a workflow that I can use to read an query extensive documents (pdfs mainly) without privacy concerns or limits to the number of tokens to be used.

## Procedure

1. Install [Ollama](https://ollama.com/) and review main commands
```bash
ollama pull <model_name>
ollama rm <model_name>
ollama list
ollama serve
```
2. Review the available models at https://ollama.com/library. Note that it's recommended that:
	
	You should have at least 8 GB of RAM available to run the 7B models, 16 GB to run the 13B models, and 32 GB to run the 33B models. 

3. Select LLM
Due to memory constrains I will start with `llama3` and go from there.

4. Setup Vector Database
I'll use an open source database, that I can run locally. I'll start with Chroma.

6. Setup embeddings function
I will use `OllamaEmbeddings()` with the selected LLM.

7. Setup directory structure as follows
```bash
.
├── data/  --> contains your pdf files
├── database/  --> initally empty will contain the vector database
├── src/ --> contains all python scripts

```

8. Move pdf documents to `data/` folder

9. Generate embeddings for document

## References
https://github.com/ollama/ollama
