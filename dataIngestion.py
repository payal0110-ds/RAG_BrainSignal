# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# def PDF_Loader(path):
#     loader=PyPDFLoader(path)
#     docs=loader.load()
#     text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

#     text=text_splitter.split_documents(docs)
#     return text

# result=PDF_Loader('Data/Research Study_Brain Signals.pdf')
# print(result[1])

'''
The WARNING are ocurred due to structural issue in PDF file, henec we are using a
differnt loader 'PDFMinerLoader' to fix this issue. 
'''

from langchain_community.document_loaders import PDFMinerLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def PDF_Loader(path):
    loader=PDFMinerLoader(path)
    docs=loader.load()
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    text=text_splitter.split_documents(docs)
    return text

# result=PDF_Loader('Data/Research Study_Brain Signals.pdf')
# print(result[1])