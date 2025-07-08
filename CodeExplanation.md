# CODE 1: DataIngestion

Loads a PDF file and split its text into overlapping chunks using the `langchain_community` and `langchain_text_splitter` rexpectively.

> Loads the PDF file from the repository. 
> Splits the PDF files into "Chunks" using `__RecursiveCharacterTextSplitter__` where the chunk_size is `500` & chunk_overlap size is `50`.
> Chunks are stores as list of "Document object" which can be retrieved manually by simple indexing technique.