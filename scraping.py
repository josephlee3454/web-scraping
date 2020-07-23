import requests # requests library
# print(requests)
from bs4 import BeautifulSoup as b_soup
# print(b_soup)

URL = 'https://en.wikipedia.org/wiki/Washington_(state)'
response = requests.get(URL)
# print(response)
content = response.content # bringing in unparsed data
# print(content)
soup = b_soup(content, 'html.parser') # parsed data but still kinda krazy with a k  
# print(soup.prettify())

# div id = "bodyContent" class = "mw-body-content"
# citation_content = soup.find_all(class_="noprint Inline-Template Template-Fact")
# print(citation_content)
new_list = []
def get_citations_needed_count():
  citation_content = soup.find_all(class_="noprint Inline-Template Template-Fact")
  new_list.append(citation_content)
  number_of_occurences = len(citation_content)
  # print(citation_content)

def get_citations_needed_report():
  citation_content_1 = new_list[0][0]
  print("first cite" + citation_content_1.text.strip())
  citation_content_2 = new_list[0][1]
  print("second cite" + citation_content_2.text.strip())
  citation_content_3 = new_list[0][2]
  print("third cite" + citation_content_3.text.strip())
  citation_content_4 = new_list[0][3]
  print("fourth cite" + citation_content_4.text.strip())
  citation_content_5 = new_list[0][4]
  print("fith cite" + citation_content_5.text.strip())
  citation_content_6 = new_list[0][5]
  print("sixth cite" + citation_content_6.text.strip())
  citation_content_7 = new_list[0][6]
  print("seventh cite" + citation_content_7.text.strip())
  


if __name__ == "__main__":
  get_citations_needed_count()
  get_citations_needed_report()


