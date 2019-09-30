# WorkingTitle
### Product Mission - A tool for game studios to fix release day bugs by collecting criticism from Twitter accounts of players on the day of a new game release. <br/>

![ARCHITECTURE](https://drive.google.com/uc?export=view&id=1w5MyFNhYvziyGwpdxZAr38DhqtP4EL3s)

### Target Users - <br/>
#### The support team at a large game development studio. <br/><br/><br/>

### MVP - <br/>
#### Current scripts which generate a list of twitter users who have tweeted about a given #hashtag. Get and analyze their tweets for sentiment, and store negative sentiment tweets for further analysis. <br/><br/><br/>

### System Design - <br/>
#### There are two pyhton scripts in this project, tweepy.py and gml.py. The first script gets a list of users who have posted a tweet with a particular #hashtag, such as the name of a newly released game, and stores their user names along with top tweets in two separate text files. We can specify the hashtag and the number of users to parse within the script.<br/>The second script parses the text file with the tweets to generate a sentiment score for each tweets in a third text file. This can then be analyzed further for negative tweets and mentions of bugs, which can be passed along to the QA team for patching.<br/><br/><br/>

### Steps to run this project - <br/>

### Dependencies - pip, python, tweepy

#### Install [Python](www.python.org), [Pip](https://pypi.org/project/pip/), [Tweepy](https://www.tweepy.org/) following the instructions for your platform (Linux, Windows or MacOS).

### Steps to run the project - <br/>
#### 1. In your terminal type ```python tweepy.py``` and hit enter. The script will get the top 20 users and generate text files containing their usernames and tweets in the same directory.<br/>
#### 2. Next type ```python gnl.py``` and hit enter. The script will generate the sentiment scores for the tweets in a text file.<br/>
#### Edit the tweepy.py file with your preferred values for the hashtag to search for and the number of users to get.<br/><br/><br/>

### Testing - <br/>
#### Used the scripts for default tests with the hashtag #Borderlands3 and number of users as 20. Got the text files for usernames, tweets and sentiment scores. (ADD SCREENSHOTS)<br/><br/><br/>

### Project Outcomes - <br/>
### Lessons - <br/>
#### 1. Building software is not easy. We ran into errors. We learnt to be patient.<br/>
#### 2. Consistency is important. Doing work in regular and small increments is much easier than holding 5 hour code sprints before the deadline.<br/>
#### 3.Documentation of the code is as important as the code itself. Poorly formatted, messy code without any accompanying documentation is a nightmare to work with. Proper documentation makes it easy for future developers to work on your code.<br/>
<br/>
### Personal Outcomes - <br/>
#### 1. What I liked doing?<br/>
#### Nihar: I liked the team aspect of the project. Working alone might not have given me a new insight into the problems that arose. A new perspective helped me attack the problem from another angle, and ultimately helped me solve the problem.<br/>
#### Wei: New partners and challenges give me impulse. This is my first API programming project. Together with Nihar, I learned a lot of skills.

#### 2. What you could have done better?
#### Nihar: I should have held more meetings, which could have led to greater product polish. We finished the project, after all in 3 meetings, and mainly worked alone on our own parts of the project.
#### Wei: We should have more communications and discussions with partners. And A clearer working plan.

#### 3. What you will avoid in the future?
#### Nihar: I will avoid jumping straight into coding without first having a plan, and without finalizing any architecture in place.<br/>
#### Wei:I will go online to search for more information and know more about APIs.

