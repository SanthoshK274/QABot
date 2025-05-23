QABot

This is a RAG-based bot that answers any questions from a particular uploaded document. The approach used to achieve this is:

-> Uploaded the document using PyPDF2
-> Extracted the raw text form the document
-> Initialized Google GenAI embeddings and further split the raw text into manageable chunks
-> Used FAISS Vector Store for storing the embeddings of the chunks.
-> Used RetrievalQA that simplifies the implementation of a RAG pipeline
-> Used Gemini-2.0-Flash using the API key, and retrieved the most relevant chunks after converting the given input query to an embedding.
-> Used the "stuff" chain type to send all chunks as a whole to the LLM, and make a meaningful content out of it.

