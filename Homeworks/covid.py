import pandas as pd
from pyarrow.dataset import dataset
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

header = []
for zi in range(20, 27):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(f'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{zi}-ianuarie-ora-13-00/')

    table = browser.find_element(by=By.CLASS_NAME, value="entry-content")
    table_text = table.text
    lista = table_text.split('\n')
    lista_index_start = [i for i, j in enumerate(lista) if 'Nr. crt.' in j]
    lista_index_final = [i for i, j in enumerate(lista) if '43.' in j]
    lista = lista[lista_index_start[0]:lista_index_final[0]:1]
    header_len = browser.find_element(by=By.XPATH, value=)

    for
    dictionar = {i: [] for i in header}
    for j in range(0, len(header)):
        for i in range(len(header) + int(j), len(lista), len(header)):
            dictionar[header[int(j)]].append(lista[i])
        df = pd.DataFrame(dictionar)


df = pd.DataFrame(dataset, columns=header)
df.to_csv('covid.csv', header=header)
print(df)
