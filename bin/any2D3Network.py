import sys
import json
import codecs
from datetime import datetime



class any2D3Network:

    def parse_tcat_file(self,path):
        results = list()
        with codecs.open(path,'r','utf-8') as source_file:
            lines = source_file.readlines()
            for line in lines[1:]:
                line_parts = line.split(',')
                date_formatted = datetime.strptime(line_parts[2],'%Y-%m-%d %H:%M:%S').strftime('%Y%m%d%H%M%S')
                tweet = {"mts":[line_parts[13]],"replied":line_parts[14],"bio":line_parts[18],"in_reply_to":line_parts[14],"text":line_parts[5],"author":line_parts[3].lower(),"datetime":date_formatted,"id":line_parts[0]}
                results.append(tweet)
        return results

    def generate_D3Network(self,tweets):

        nodes = list()
        links = list()
        nodes_aux = dict()
        links_aux = dict()

        for tweet in tweets:
            print "tweet"
            print tweet['mts']
            author = tweet['author']
            if not author in nodes_aux.keys():
                nodes.append({"author":author,"bio":tweet['bio'],"datetime":tweet['datetime']})
                id = len(nodes_aux.keys())
                nodes_aux[author] = id


            for mt in tweet['mts']:
                if mt != "":
                    print "mt"
                    print tweet
                    link_str = "%s&&##&&%s" % (author,mt)
                    if not link_str in links_aux:
                        id = len(links_aux.keys())
                        links_aux[link_str] = id
                        links.append({"source":author,"target":mt,"weight":1,"type":"mt"})

                    else:
                        links[links_aux[link_str]]['weight'] += 1
                        links[links_aux[link_str]]['type'] = "mt"

        network = {"nodes":nodes,"links":links}
        return network





if __name__ == "__main__":

    obj = any2D3Network()

    tweets = []

    tweets += obj.parse_tcat_file(sys.argv[1])

    red = obj.generate_D3Network(tweets)

    json.dump(red,open("pruebaRedD3.json","w"),indent=4)
