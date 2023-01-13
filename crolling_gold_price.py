import requests
from bs4 import BeautifulSoup
import pickle

#매개변수 'kind' 따라 맞는 값 크롤링
def crolling_information(kind):
    request = requests.get(f"https://www.goodgold.co.kr/goldprice/gold_price.php?gold={kind}&pageNum=1")
    request.raise_for_status()
    res = BeautifulSoup(request.text, "html.parser")


    table = res.find("div", {"class":"content"}).find("table")
    tables = table.find_all("tr")[:2]

    if (kind == "순금"):
        name = "24k"
    else:
        name = tables[0].find_all("th")[0].text
    
    date = tables[1].find_all("td")[0].text
    price = tables[1].find_all("td")[2]
    price.find('span').decompose()
    price = price.text.replace(",", "").strip()
    
    infos = [name, date, int(price)]
    print(infos)
    return infos

#값 정리하는 함수
def arrange_data():
    datas = {
    "info_24k" : crolling_information("순금"),
    "info_18k" : crolling_information("18K"),
    "info_14k" : crolling_information("14K")
    }
    return datas

def save_data():
    datas = arrange_data()
    with open("./gold_calc_pyhton/gold_data.pickle","wb") as fw:
        pickle.dump(datas, fw)

def load_data():
    with open("./gold_calc_pyhton/gold_data.pickle","rb") as fr:
        data = pickle.load(fr)
    return data