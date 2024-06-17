'''
Here I'm assuming there is the following directory structure

.
├── data/  --> contains your pdf files
├── database/  --> initally empty will contain the vector database
├── src/ --> contains all python scripts

'''
import argparse
import os
import shutil

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document

# External import for embedding function
from cust_embedding_function import cust_embedding_function

# To import Chroma database
from langchain_community.vectorstores import Chroma

PATH_TO_DATABASE = "../database/"
PATH_TO_DATA = "../data"
MODEL_NAME = 'llama2'

def main():

    # Check if the database should be cleared (using the --clear flag).
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--reset", 
        action="store_true", 
        help="Reset the database.")
    
    args = parser.parse_args()
    if args.reset:
        print("Clearing Database")
        clear_database()

    # Create (or update) the database
    documents_list = load_documents()
    chunks = split_documents(documents_list)
    add_to_database(chunks)

# reference
#  https://python.langchain.com/v0.1/docs/modules/data_connection/document_loaders/
def load_documents():
    print('Loading Documents')
    document_loader = PyPDFDirectoryLoader(PATH_TO_DATA)
    return document_loader.load()


def split_documents(documents_list: list[Document]):
    print('Splitting Documents')
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800, # 800 characters for each chunk
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents_list)


def add_to_database(chunks: list[Document]):
    
    # Load the existing database.
    db = Chroma(
        persist_directory=PATH_TO_DATABASE, 
        embedding_function=cust_embedding_function(MODEL_NAME)
    )

    # Calculate Page IDs.
    chunks_with_ids = calculate_chunk_ids(chunks)

    # Add or Update the documents.
    existing_items = db.get(include=[])  # IDs are always included by default
    existing_ids = set(existing_items["ids"])

    print(f"Number of existing documents in DB: {len(existing_ids)}")

    # Only add documents that don't exist in the DB.
    new_chunks = []
    for chunk in chunks_with_ids:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)

    if len(new_chunks):

        print(f"Adding new documents to database: {len(new_chunks)}")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids=new_chunk_ids)
    else:
        print("No new documents to add")


def calculate_chunk_ids(chunks: list[Document]):

    # This will create IDs like "data/document_name.pdf:6:2"
    # Page Source : Page Number : Chunk Index

    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        # If the page ID is the same as the last one, increment the index.
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        # Calculate the chunk ID.
        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id

        # Add it to the page meta-data.
        chunk.metadata["id"] = chunk_id

    return chunks


def clear_database():
    if os.path.exists(PATH_TO_DATABASE):
        shutil.rmtree(PATH_TO_DATABASE)


if __name__ == "__main__":
    main()
