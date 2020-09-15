This scraper can scrap all Questions-Answers related to any topic e.g. mathematics-and-physics,coronavirus etc from Quora.

If what you need to crawl is the answers to all the questions under a topic, then you firstly need to use 'QuestionLink.py' to get the list of questions, and the list will be saved in 'QuoraLink.csv'.

​		python QuestionLink.py 

If you need to get all the replies under a specific question, then you only need to write the question into 'QuoraLink.csv'.

Then run 'QuoraAnswer.py' to get the response, which would be stored in 'QuoraAnswer.csv'

​		python QuoraLink.csv

