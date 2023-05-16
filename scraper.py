from bs4 import BeautifulSoup
import requests

def lunch(x:int):
    #경상국립대 주간식단 사이트 주소
    url = "https://www.gnu.ac.kr/main/ad/fm/foodmenu/selectFoodMenuView.do?mi=1341&restSeq=5"
    
    #주간식단 사이트 주소로 페이지 요청을 보내고 받은 페이지를 html.parser로 텍스트 형태 파일로 변환 
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    
    #bs라이브러리 메서드 중 요소선택 메서드를 이용하여 원하는 데이터 가져오기
    elements = soup.select('#detailForm div table tbody tr:nth-child(2) p')
    
    #원하는 데이터를 menu_list 안으로 넣기
    menu_list = []
    for i in range(len(elements)):
        menu_list.append(elements[i].get_text())
                       
    return menu_list[x]


