#TODO:Make into an exe, maybe find a better reg expr for URLs

import webbrowser, sys, os, re

text_path = os.getcwd() + "/websites.txt"
links = []
regex_link = re.compile('(?:http[s]?://)?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\)]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

f = open(text_path,'r')
lines = f.readlines()

for line in lines:
    line_links = regex_link.findall(line)
    links.extend(line_links)

for link in links:
    if "https://" not in link:
        link = "https://" + link
    webbrowser.open_new_tab(link)

print(links) 
