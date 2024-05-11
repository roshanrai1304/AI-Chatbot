from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
import pinecone
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
import os

def load_docs(directory):
  loader = DirectoryLoader(directory)
  documents = loader.load()
  return documents


def split_docs(documents,chunk_size=500,chunk_overlap=20):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  docs = text_splitter.split_documents(documents)
  return docs

def get_similiar_docs(index, query,k=1,score=False):
  if score:
    similar_docs = index.similarity_search_with_score(query,k=k)
  else:
    similar_docs = index.similarity_search(query,k=k)
  return similar_docs



def upload_pinecone():
    directory = '../text file'
    documents = load_docs(directory)
    docs = split_docs(documents)
    print(len(docs))

    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    PINECONE_API_KEY = '' #@param {type:"string"}

    os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
    # find API key in console at app.pinecone.io


    index_name = 'chatbot-database'
    index = PineconeVectorStore.from_documents(docs, embeddings, index_name=index_name)

    query = "How is India economy"
    similar_docs = get_similiar_docs(index, query)
    similar_docs