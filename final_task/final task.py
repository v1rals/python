#!/usr/bin/env python3
import sys


try:    # check input values
    path = sys.argv[1]
    tag = sys.argv[2]
except Exception:
    print("please check input values")
    print("first arg is link:   https://habr.com/ru/post/280238/")
    print("second is tag:   span")
    exit(0)
try:
    log = sys.argv[3]
except IndexError:
    log = None
try:
    upload = sys.argv[4]
except IndexError:
    upload = None


class CountTags:

    def __init__(self, path, tag, log, upload):
        self.path = path
        self.tag = tag
        self.tags = []
        self.list = []
        self.log = log
        self.upload = upload
        self.result = None

    def run(self):

        from html.parser import HTMLParser
        from time import gmtime, strftime

        class MyHTMLParser(HTMLParser):

            def handle_starttag(self, tag, attrs):
                count.append(tag)

            def handle_endtag(self, tag):
                count.append(tag)

        parser = MyHTMLParser()

        from urllib.request import urlopen
        from bs4 import BeautifulSoup
        from urllib.error import URLError
        try:    # check is url valid
            html = urlopen(self.path)
            page_content = html.read()
        except URLError:
            print("cant reach destination page")
            exit(0)

        with open('pagelog.html', 'wb') as fid:             #save page content
            fid.write(page_content)
        doc = open("pagelog.html", "r", encoding="utf8")
        soup = BeautifulSoup(doc, 'html.parser')
        # parse saved page
        count = []
        parser.feed(soup.prettify())
        self.tags.append(count)

        from collections import Counter     # count tags
        for i, item in enumerate(self.tags):
            self.list = Counter(self.tags[i])

        if self.tag == "all":   # check user wishes
            print(self.list)
            print("All:", sum(self.list.values()))
            self.result = "all:", sum(self.list.values()), self.list
        else:
            for key in self.list:
                if key == self.tag:
                    print(self.tag, self.list[key])
                    self.result = (self.tag, self.list[key])

        def logging(path, result):  # logging, obliviosly
            with open('log.txt', 'a+') as log:
                time = strftime("%Y/%m/%d %H:%M", gmtime())
                logstring = time + " " + path + " " + str(result)
                log.write(logstring + "\n")
        if self.log == "L":
            logging(self.path, self.result)

        def s3upload():     # upload to s3
            import boto3
            file_name = 'log.txt'
            bucket_name = input("input source bucket name" + "\n")  # name of the bucket
            s3_client = boto3.client('s3')
            s3_client.upload_file(file_name, bucket_name, file_name)
        if self.upload == "u":
            s3upload()


if __name__ == "__main__":
    CountTags(path, tag, log, upload).run()


