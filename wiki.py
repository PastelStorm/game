#!/usr/bin/env python

import requests
import re
import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("secret")
    args = parser.parse_args()
    return args

def call(url):
    headers = {"Content-type": "application/json"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        sys.exit('Status:', response.status_code, 'There was a problem with the request')
    return response.json()

def get_text():
    secret = parse_args().secret
    url = "http://en.wikipedia.org/w/api.php?action=parse&page=%s&format=json&prop=text&section=0" % secret
    response = call(url)
    # get only text from article
    response = response["parse"]["text"]["*"]
    # get article first paragraph
    match = re.search(r'<p>(.+)</p>', response)
    # check if article exists
    if match:
        question = re.sub(r'<[^>]*>', '', match.group(0))
    else:
        sys.exit('The article for %s not found. Try another word.' % secret)

    # replace the secret word with ???
    question = re.sub(r'(?i)%s[A-Za-z]{0,3}[\s\"\.,:;!?\']' % secret[:-1], '???' + ' ', question)
    # remove text in square brackets, i.e. links numbers
    question = re.sub(r'\[[A-Za-z0-9 ]*\]', '', question)
    # remove text in parentheses, i.e. pronunciation or latin names for subjects
    question = re.sub(r'\s\(([^\)]+)[\)]+', '', question)
    #question = re.sub(r'\s+', ' ', question)
    return question.encode('utf-8')

def get_images():
    secret = parse_args().secret
    url = "http://en.wikipedia.org/w/api.php?action=query&titles=%s&prop=images&format=json" % secret
    response = call(url)
    #get images names
    image_titles = []
    images = response["query"]["pages"].values()[0]["images"]
    for image in images:
        #if secret.lower() in image["title"].lower():
        image_titles.append(image["title"])

    image_urls = []
    for title in image_titles:
        title = title.replace('&', '%26')
        url = "http://en.wikipedia.org/w/api.php?action=query&titles=%s&prop=imageinfo&iiprop=url&format=json" % title
        image_url = call(url)["query"]["pages"].values()[0]["imageinfo"][0]["url"]
        image_urls.append(image_url)

    return image_urls

if __name__ == "__main__":
    with open("wiki.html", "w") as f:
        f.write("<p>")
        f.write(get_text())
        f.write("</p>")
        for i in get_images():
            f.write('<img src="%s" width="320">' % i)
