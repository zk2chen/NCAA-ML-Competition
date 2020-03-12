from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import pandas as pd



def get_draft_data(year):
    page = requests.get('https://www.nbadraft.net/ranking/bigboard/?year-ranking='
                        + str(year))
    soup = BeautifulSoup(page.content, 'html.parser')
    
    soup.findAll('tr', limit = 2)
    headers = [th.getText() for th in soup.findAll('tr', limit = 2)[0].findAll('th')]
    headers.append('Season')
    headers = headers[2:]
    
    rows = soup.findAll('tr')[1:]
    draft_info = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]
    
    df_draft = []
    for i in range(len(draft_info)):
        player_info = draft_info[i][2:]
        player_info.append(year)
        df_draft.append(player_info)
    
    draft_data = pd.DataFrame(df_draft, columns = headers)
    return draft_data