import webbrowser

ISRL_url = "https://hastie.su.domains/ISLR2/ISLRv2_website.pdf" # Replace with the URL of the webpage you want to open
ISRL_PDF_PAGE = 38
webbrowser.open(ISRL_url)
print(f"ISRL current PDF page: {ISRL_PDF_PAGE} read till {ISRL_PDF_PAGE + 5}")

DL_url = "https://www.deeplearningbook.org/" # Replace with the URL of the webpage you want to open
DL_PAGE = 29
current_C_and_S = "Linear Algebra"
print(f"DL current PDF page: {DL_PAGE} read till {DL_PAGE+5}, Currently reading: {current_C_and_S}")
webbrowser.open_new(DL_url)

learn_pytorch = "https://www.learnpytorch.io/00_pytorch_fundamentals/"
webbrowser.open_new(learn_pytorch)
pytorch = "Pytorch fundamentals"
print(f"current section: {pytorch}")
