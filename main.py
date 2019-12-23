from pprint import pprint
import requests
from bs4 import BeautifulSoup

URL = 'https://blah.com'  # enter url to be searched
page = requests.get(URL)  # pulls url from net
# pprint(page)

soup = BeautifulSoup(page.content, 'html.parser')  # converts incoming data to j.script
results = soup.find(id='ResultsContainer')  # decodes j.script to html from specified id eg. <div id="ResultsContainer">
# print(results.prettify())  # clean the html to readable format and prints
# print("brb.....")
# """Beautiful Soup object called 'results' and select only the job postings.
# # These are, after all, the parts of the HTML that you’re interested in! You can do this in one line of code
# # eg. Every job posting is wrapped in a <section> element with the class_='card-content'   """
#
# element = results.find_all('section', class_='class name')
#  # ".find_all()" on a Beautiful Soup object
# # It returns an iterable containing all the HTML for the thing being searched eg jobs listin
# for every in element:
#      # for job_elem in element:
#      #     print(job_elem, end='\n' * 2) """displays all code under the html code <sectoin> & class = card content"""
#      # """for a more precise neat search create var for what you're looking for"""
#     var1 = every.find('html attribute', class_='class name')  # this var finds every class named 'title'
#     var2 = every.find('html attribute2', class_='class name')  # this var finds every class named 'company'
#     var3 = every.find('html attribute3', class_='class name')  # this var finds every class named 'location'
#     print(var1, var2, var3)
#     print()
#     """ But still there's a lot of html lets scale it down"""
#     var1 = every.find('html attribute', class_='class name')
#     var2 = every.find('html attribute2', class_='class name')
#     var3 = every.find('html attribute3', class_='class name')
#     if None in (var1, var2, var3):
#         continue
#     print(var1.text.strip())
#     print(var2.text.strip())
#     print(var3.text.strip())
#     print()
#     #  add .text() to a BeautifulSoup object to convert HTML elements to text
#     # add .strip() to remove the over spacing
#     """ for this error: AttributeError: 'NoneType' object has no attribute 'text'  # Due to web advertisements
#     Use:     if None in (var1, var2, var3):
#                     continue"""
main_query = results.find_all('html attribute', string=lambda text: 'search item' in text.lower())

for ans in main_query:
    link = ans.find('a')['href']
    print(ans.text.strip())
    print(f" Number Of Results: {len(main_query)}")
    print(f" Answer: {link}\n")




