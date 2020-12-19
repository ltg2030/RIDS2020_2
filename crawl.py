import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileReader, PdfFileWriter

start = 1
idx = 0
with open("dict.txt","r") as fd:
    dictionary = fd.read().split('\n')

    for msg in dictionary:
        try:
            keyword = msg.split('. ')[1].split(':')[0]
            url = f"https://www.google.com/search?q=filetype%3Apdf+{keyword}&start={start}"
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')

            links = soup.select('a')
            links = list(filter(lambda s:s.get('href').find('.pdf')!=-1, links))

            for link in links:
                idx = idx + 1
                s = link.get('href')
                s = s[s.find('http'):s.find('.pdf')+4]
                
                print(f"save {s} -> {idx}.pdf")

                r = requests.get(s)
                with open(f'{idx}.pdf', 'wb') as f:
                    f.write(r.content)

                with open(f'{idx}.pdf', 'rb') as f:
                    try:
                        inputpdf = PdfFileReader(f)
                        for i in range(inputpdf.numPages):
                            output = PdfFileWriter()
                            output.addPage(inputpdf.getPage(i))
                            with open(f"{idx}_%s.pdf" % i, "wb") as outputStream:
                                output.write(outputStream)
                    except:
                        pass
        except:
            pass

        

"""
            """