
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
from elasticsearch import Elasticsearch, RequestsHttpConnection
import requests
#Enter your twitterAPI keys here 
consumer_key = 'MZ8fXiLq1KhxO11UwAbjW99cm'
consumer_secret = 'Dn50Md2gWlbVxybHAKgI1Knob71ugiF7Q7gIJClN33M1GYySCj'
access_token = '52647948-xnlwpbETyFNX0JmEcdrsB7FLI42fTimAbyXK1xgOM'
access_secret = 'xiYL3QEpPmNmbR0AhqphvS2s2Tyf0V0FOOcpKRb92d4kL'


class StdOutListener(StreamListener):

    def on_data(self, data):
        data_json = json.loads(data)
        try:
            coordinates = data_json['place']['bounding_box']['coordinates']
            tweet = data_json['text']
            place = data_json['place']

            if place is not None:
                if coordinates[0] is not None and len(coordinates[0]) > 0:
                    avg_x = 0
                    avg_y = 0
                    for c in coordinates[0]:
                        avg_x = (avg_x + c[0])
                        avg_y = (avg_y + c[1])
                    avg_x /= len(coordinates[0])
                    avg_y /= len(coordinates[0])
                    coordinates = [avg_x, avg_y]
                print coordinates
                e_data = {
                    "tweet": tweet,
                    "coordinates": coordinates

                }
                rrr = requests.post('https://search-twittermap-inuckwupgoy3q4rf7vxtv65y5y.us-west-1.es.amazonaws.com/twittermap/abc',json=e_data)
                #rrr = requests.get('https://search-twittermap-inuckwupgoy3q4rf7vxtv65y5y.us-west-1.es.amazonaws.com/')
                print rrr
        except (KeyError, TypeError):
            pass
        return True

    def on_error(self, status):
        print (status)

if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, StdOutListener())
    stream.filter(track=['trump','messi','ronaldo','bush','thursday','josh brown','#indvsnz',
                         'location','amazon','dollar','lenovo','hugh','pizza','snapchat','money',
                         'election','https','lol','instagram','twitter','fb','facebook','nba','birthday',
                         'technology', 'hillary', 'food', 'travel','vote','nintendo', 'fashion', 'soccer',
                         'sports','modi','debate','america','india','obama','song','punjab','new york','bernie',
                         'news','logan','usa','london','health','Dangal'])


