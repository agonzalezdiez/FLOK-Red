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
                tweet = {"replied":line_parts[14],"bio":line_parts[18],"in_reply_to":line_parts[14],"text":line_parts[5],"author":line_parts[3].lower(),"datetime":date_formatted,"id":line_parts[0]}
                results.append(tweet)
        return results




if __name__ == "__main__":

    obj = any2D3Network()

    tweets = []

    tweets += obj.parse_tcat_file(sys.argv[1])

    print tweets
