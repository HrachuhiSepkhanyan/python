import feedparser

urls = ["https://rss.nytimes.com/services/xml/rss/nyt/World.xml", 
"https://rss.nytimes.com/services/xml/rss/nyt/Business.xml",
"https://rss.nytimes.com/services/xml/rss/nyt/Sports.xml"]

files = ['world.csv', 'business.csv', 'sport.csv']


index = 0   
for url in urls:
    feed = feedparser.parse(url)['entries']
    item_feed = [item for item in feed]
    lst = [{'title':i['title'], 'link': i['link']} for i in feed]
    try:
        with open (files[index], 'w', encoding='utf-8') as input_file:
            for item in lst:
                input_file.write(str(item['title']+'\n'))
                input_file.write(str(item['link']+'\n'))
                input_file.write('\n')
    except FileNotFoundError:
        print('File not exist')
    index +=1