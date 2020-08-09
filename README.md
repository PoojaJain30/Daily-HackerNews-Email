# Daily-HackerNews-Email

Daily-HackerNews-Email is a Python project.
In this project I am scrapping top 10 news with more than 100 votes from hackernews and then sending that as a html email to the mailing list.

## Instalation and Inbuild modules
BeautifulSoup 
smtplib
email.message
csv

## Stucture 

The project is divided into three .py files and one .csv file.

1.main.py : Main script run
2.send_email.py: Functionality for email sending
3.news_data.py: Functionality for scrapping data 

## Future Enhancement
Using AWS cloud to send email every morining at particular time.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)