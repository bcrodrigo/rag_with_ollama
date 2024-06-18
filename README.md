# rag_with_ollama

Repository to test RAG using Ollama locally on my computer.

## Background and Motivation

Retrieval Augmented Generation (RAG) is a process to optimize the output of a Large Language Model (LLM) so that it references sources outside of its training data before generating a response [^1]. This is a less computationally expensive process, compared to fine-tuning, where selected weights of the model are actually updated in order to account for new items.

In this small project I want to setup my computer to interact with LLMs locally, on device, without using an API call. This will enable a workflow that I can use to read and query documents (mainly pdfs) without privacy concerns or limits to the number of tokens to be used by the LLM. 

Additionally, these scripts will provide a building block for Natural Language Processing tasks, as there is a necessity to convert text into embeddings, and LLMs already do this by default.

## Installation Procedure

1. Install [Ollama](https://ollama.com/) and review main commands [^2].
```bash
ollama pull <model_name>
ollama rm <model_name>
ollama list
ollama serve
```

2. Clone this repository.
3. Install the requirements with
```bash
pip install -r requirements.txt
```
4. Make two new directories so that the structure is as follows:
```bash
.
├── data/  --> contains your pdf files
├── database/  --> initally empty will contain the vector database
├── src/ --> contains all python scripts

```

## Usage

### Preparation
- Review the available models at the [Ollama model library](https://ollama.com/library). Note that it's recommended that:

	"You should have at least 8 GB of RAM available to run the 7B models, 16 GB to run the 13B models, and 32 GB to run the 33B models."

- Select an LLM, and download it with
```bash
ollama pull <model_name>
```
Note that I've selected `llama3` for all the scripts.

- Start a local Ollama server
```bash
ollama serve
```
### Adding Documents to the Database

- Move your pdf documents to the `data/` folder then run 
```bash
python create_or_add_to_database.py
```

### Querying the Database
```bash
python query_database.py "your_query_for_LLM"
```

## Challenges and Recommendations

**Choice of database:** I use ChromaDB, but there are other options, that could provide higher speed.

**Choice of embeddings:** I use `OllamaEmbeddings()` with the chosen model, but there are other options.

**Consistency and repeatability of responses:** This is related to the embeddings, chunk sizes, and the metadata available in the database. 
- [ ] Need to look into hierarchies and knowledge graphs (see [^3] for details)

**Evaluation of results:** This will be related to the contents of the documents we add to the database. 
- [ ] Need to have a dedicated test suit to try perform consistent evaluation of the LLM.

**Deployment:** This necessitates an API key, and it's outside of the scope of this project.

## References

[^1]: https://aws.amazon.com/what-is/retrieval-augmented-generation/
[^2]: https://github.com/ollama/ollama
[^3]: https://medium.com/enterprise-rag/a-first-intro-to-complex-rag-retrieval-augmented-generation-a8624d70090f