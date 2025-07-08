# PDF Read: Warning 'Ignoring wrong pointing object 18 0 (offset 0)':

 If the code returns __Warnings__ from the PDF parse being used by `PyPDFLoader` as : __Ignoring wrong pointing object 18 0 (offset 0)__


The `warnings` may occur due to structural issues or irregularities in the PDF files, as they may contain malformed or non-standard references; typically from documents created in `Word` or `scanned`.

## How to fix this issue:

### Option 1: (Use a different loader):

        from langchain_community.document_loaders import PDFMinerLoader
        loader = PDFMinerLoader(path)
        docs = loader.load()

### Option 2: (Clean or re-export the PDF):
- Online Tools: __[ILovePDF](https://www.ilovepdf.com/repair-pdf)__ or __[PDF24](https://tools.pdf24.org/en/repair-pdf)__ Tools to `"repair"` or clean PDFs.
- Microsoft Word: Save as PDF → __Ensure "Best for electronic distribution and accessibility"__ is selected.
