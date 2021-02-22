import re
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get('https://www.2kratings.com/teams/boston-celtics')
soup = BeautifulSoup(page.content, 'html.parser')
players = soup.find('tbody')

names_raw = players.find_all(class_ = "entry-font")
names = [name.get_text() for name in names_raw]

# Find all attribute boxes
regex = re.compile('.*attribute-box.*')
ratings_raw = players.find_all("span", {"class" : regex})
ratings = [int(rating.get_text()) for rating in ratings_raw]

#print(ratings)
ratings_pp = np.array(ratings)
#print(type(ratings_pp))
ratings_matrix = ratings_pp.reshape(len(names), 3)
#print(ratings_matrix)
ovrs = [x[0] for x in ratings_matrix]
threePTs = [x[1] for x in ratings_matrix]
dnks = [x[2] for x in ratings_matrix]

# Create pandas dataframe
players_info = pd.DataFrame(
    {
        'Player': names,
        'OVR': ovrs,
        '3PT': threePTs,
        'DNK': dnks
    }
)

print(players_info)

players_info.to_csv("player_data.csv")