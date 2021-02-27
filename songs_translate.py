import requests
from lxml import etree
import lxml.html
import csv


'''
parce songs from https://www.amalgama-lab.com/ with translations
'''

def parce(url):
    try:
        api = requests.get(url)
    except:
        return
    tree = lxml.html.document_fromstring(api.text)
    text_original = tree.xpath('//*[@id="click_area"]/div//*[@class="original"]/text()')
    text_translate = tree.xpath('//*[@id="click_area"]/div//*[@class="translate"]/text()')
    with open("text.csv", "w", newline = '') as csv_file:
        write = csv.writer(csv_file)
        for i in range(len(text_original)):
            print(text_original[i], text_translate[i])
            write.writerow(text_original[i])
            write.writerow(text_translate[i])
def main(url):
    parce(url)

if __name__ == "__main__":
    main("https://www.amalgama-lab.com/songs/r/robbie_williams/feel.html")
