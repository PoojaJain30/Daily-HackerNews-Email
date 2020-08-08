import requests
from requests.exceptions import HTTPError

#function to check the response 
def is_good_response(res):
    content_type = res.headers['Content-Type'].lower()
    return (res.status_code == 200 and content_type is not None and content_type.find('html') > -1)

#function to get the response from given url
def get_response(url):
    try:
        response = requests.get(url)
        if is_good_response(response):
            return response.content
        else:
            return None
    except HTTPError as err:
        print(f'Http error occured: {err}')
        return None
    except Exception as otherErr:
        print(f'Other error occured: "{otherErr}')
        return None

#function to get news details with more than 100 points   
def get_top_news(story,score):
    news = []
    for idx,val in enumerate(story):
        title = story[idx].getText()
        link = story[idx].get('href') 
        votes = score[idx].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points',''))
            if points >= 100:    
                news.append({'Title': title , 'Link': link , 'Votes': points})
    return news

#function to get top 10 news
def sort_top10_news(data):
    return sorted(data,key = lambda item : item['Votes'] , reverse = True)[0:10]

#function to consturct email body html structure 
def news_html(data):
    links = ""
    for i in range(len(data)):
        links += '<li style="font-size:14px;"><a href="'+data[i]["Link"]+'">'+data[i]["Title"]+'</a></li>'
    msg = """<h1 style='color:#40E0D0;'> Good Morning!!</h1><h2> Top 10 news:</h2><ul>""" + links + """  </ul><h3> See you Tomorrow </h3>"""
    return msg