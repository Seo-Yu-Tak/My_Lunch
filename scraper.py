from bs4 import BeautifulSoup
import requests


url = "https://www.gnu.ac.kr/main/ad/fm/foodmenu/selectFoodMenuView.do?mi=1341&restSeq=5"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

elements = soup.select('#detailForm div table tbody tr:nth-child(2) p')


menu_list = []
for i in range(len(elements)):
    menu_list.append(elements[i].get_text())
    print(elements[i])
    
print(menu_list[0])
