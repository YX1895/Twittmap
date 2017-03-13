# Twittmap

Humans are curious creatures. They are interested in what people say in different regions. So we developed TwitterMap, a map displaying the location where a certain word is tweeted by someone.  
<br>
There are two way of using TwitterMap. First, we can select the sample word from the dropdown menu to see their location. We can also type in any words we are interested in to find the location where a twitter user has posted a tweet. When a user clicks the marker, he or she could see the content of this tweet.  
<br>
We designed its UI by bootstrap and using Django as its backend. First, we acquired tons of tweets (including geolocation etc.)by Twitter streaming API and store them through AWS ElasticSearch. When a user queried a keyword, ElasticSearch could help to get queried results. Google maps API then translate the geo-information to the markers on the map. And we deployed our application on AWS Elastic Beanstalk in an auto-scaling environment.  
![GitHub](https://github.com/YX1895/Twittmap/blob/master/UI.jpeg)

We can also view the content and position of this tweet by clicking the marker.

![GitHub](https://github.com/YX1895/Twittmap/blob/master/tweetcontent.jpeg)

Stack
----
* Elasticsearch (tweet storage and search)
* Django (backend)
* Bootstrap (frontend)

Usage
----
####Install Dependencies####
```java
// install dependencies with:
$ pip install -r requirements.txt
```
####Start Server####
```java
$ python manage.py runserver
```
 
