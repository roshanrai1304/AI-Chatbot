# AI-Chatbot

The project is an AI chatbot which takes files from google drive as a knowledge base and gives the response according to that

The project is divided into three part's:
  1. The files are downloaded from google drive
  2. They are separated into chunks and stored it into pinecone
  3. Then the chatbot implementation which reads files from pinecone and gives the response


For the setup of the project install the required library in the requirements.txt file gives the api_key for OpenAI and Pinecone wherever required and run the command streamlit run app.py