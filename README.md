# python-nba2k-ratings-crawler
 Python NBA 2K ratings crawler with BeautifulSoup

### How to Run
 Change request url to the link of nba team in "2kratings.com"
 
### Example
 ```python
page = requests.get('https://www.2kratings.com/teams/boston-celtics')
```
 This link will generate a table as fellow
 |     |Player          |OVR|3PT|DNK|
|------|----------------|---|---|---|
|0     |Jayson Tatum    |90 |84 |88 |
|1     |Jaylen Brown    |89 |85 |89 |
|2     |Kemba Walker    |85 |79 |30 |
|3     |Marcus Smart    |79 |72 |50 |
|4     |Daniel Theis    |78 |78 |78 |
|5     |Robert Williams |77 |25 |75 |
|6     |Tristan Thompson|77 |62 |75 |
|7     |Payton Pritchard|76 |86 |35 |
|8     |Jeff Teague     |75 |82 |70 |
|9     |Semi Ojeleye    |73 |81 |75 |
|10    |Javonte Green   |72 |66 |85 |
|11    |Aaron Nesmith   |71 |75 |55 |
|12    |Grant Williams  |71 |81 |60 |
|13    |Romeo Langford  |70 |65 |65 |
|14    |Tacko Fall      |70 |30 |65 |
|15    |Carsen Edwards  |70 |76 |65 |
|16    |Tremont Waters  |69 |75 |30 |
