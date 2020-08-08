import csv
from bs4 import BeautifulSoup
import news_data as nd
import send_email as se

def main():
    response1 = nd.get_response('https://news.ycombinator.com/')
    response2 = nd.get_response('https://news.ycombinator.com/news?p=2')

    html1 = BeautifulSoup(response1,'html.parser')
    html2 = BeautifulSoup(response2,'html.parser')

    # getting the title and link
    story1 = html1.findAll('a',class_ = 'storylink')
    story2 = html2.findAll('a',class_ = 'storylink')
    mega_story = story1 + story2

    # getting the votes data
    score1 = html1.select('.subtext')
    score2 = html2.select('.subtext')
    mega_score = score1 + score2

    news = nd.get_top_news(mega_story,mega_score)
    final_news = nd.sort_top10_news(news)
    print(final_news)
    email_body = nd.news_html(final_news)
    
    with open("emailList.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
           # print(row)
           se.send_email(row,email_body)


if __name__ == '__main__':
    main()