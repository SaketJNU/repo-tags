import string
import json
import re

class TagfromReadme():

    def __init__(self):
        pass

    def read_file(self):
        readme_file = []
        for line in open("README.md"):
            for text in line.split():
                ftext = re.sub('[^a-zA-Z0-9-_.]', ' ', line)
                for word in ftext.split():
                    readme_file.append(word)
                    #print word
        return readme_file


    def read_tag_list(self):
        tag_list = []
        with open('aggregated_topic_list.json') as f:
            tags = json.load(f)
            for tag in tags:
                tag_list.append(tag)
            #print tag_list
        return tag_list

    def read_stop_words(self):
        stop_words = []
        for line in open("unique_stop_word_list.txt"):
            if line.strip()[0:1] != "#":
                for word in line.split():  # in case more than one per line
                    stop_words.append(word)
        return stop_words

    def remove_stopwords(self, readme, stop_words):
        keywords = []
        for word in readme:
            if word not in stop_words:
                keywords.append(word)
        return keywords

    def assign_tags(self, keywords, tag_list):
        assigned_tags = []

        for key in keywords:
            if key in tag_list:
                if key not in assigned_tags:
                    assigned_tags.append(key)
        return assigned_tags

    def fetch_tags(self):
        tag_list = self.read_tag_list()
        stop_words = self.read_stop_words()
        readme_file = self.read_file()
        keywords = self.remove_stopwords(readme_file, stop_words)
        assigned_tags = self.assign_tags(keywords, tag_list)

        #print "Length of readme file:", len(readme_file)
        #print "Length of stop-words:", len(stop_words)
        #print "Length of tags:", len(tag_list)
        print "Length of assigned tags", len(assigned_tags)
        print "Tags assigned to the package:", assigned_tags


if __name__ == "__main__":
    t = TagfromReadme()
    t.fetch_tags()