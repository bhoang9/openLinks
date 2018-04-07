#TODO: make it so that script works properly even when no browser window
#      is initially open

import webbrowser, sys, os, re

text_path = os.getcwd() + "/websites.txt"
links = []
regex_link = re.compile('(?:http[s]?://)?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\)]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

f = open(text_path,'r')
lines = f.readlines()

for line in lines:
    line_links = regex_link.findall(line)
    links.extend(line_links)

#if("https://" not in links[0]):
#    links[0] = "https://" + links[0]
#    webbrowser.open_new(links[0])
#else:
#    webbrowser.open_new(links[0])

for link in links:
    if "https://" not in link:
        link = "https://" + link
    webbrowser.open_new_tab(link)

print(links) 
