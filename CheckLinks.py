import http.client
import urllib.request,urllib.error
import os
import sys
import re

# Get the response code of the url to see if it exists
def getResponseCode(url):
    content = None
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        conn = urllib.request.urlopen(req)
        # Only get HTML if we have a potential anchor link
        if "#" in url and "pdf" not in url:
            content = conn.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        return [e.code,content]
    except urllib.error.URLError as e:
        return [404,content]
    except http.client.InvalidURL:
        return [200,content]
    return [conn.getcode(),content]


path = os.path.dirname(os.path.realpath(__file__))
remove_characters = ['**', '\\n']
# text that tends to be at the end of the url that we need truncate everything past them
end_characters = [')',",","'",'`',"\"",'</a>','</div>',"\\",">"]
big_regex = re.compile('|'.join(map(re.escape, remove_characters)))
if len(sys.argv) >1  and os.path.exists(sys.argv[1]):
    path = sys.argv[1]

err = 0
# Loop through all files in path
for root, dirs, files in os.walk(path):
    for file in files:
        #  only read file that match template ( txt, md or python notebook)
        if file.endswith(".md") or file.endswith(".txt") or file.endswith(".ipynb"):

            # get content and separate into lines and then separate by spaces
            raw_content = open(os.path.join(root, file), "r").read()
            content = raw_content.split("\n")
            content = [x.split(" ") for x in content]

            # have an incrementer for line number later export
            line_num=0
            for line in content:
                char=0
                for item in line:

                    if "https://" in item or "http://" in item:

                        # this is a command being ran so difficult to validate in this script, skip it
                        if '$(uname' in item:
                            continue

                        # get just from the http portion if there was more in from of the string we grabbed
                        item = item[item.find("http"):]

                        # if there is a period at the end, truncate to that period. Other periods may be valid
                        if item.endswith("."):
                            item = item[:item.rfind(".")]
                        if item.endswith("'"):
                            item = item[:item.rfind("'")]
                        if item.endswith("\""):
                            item = item[:item.rfind("\"")]
                        # strip various characters that may be in the string
                        item_stripped = big_regex.sub("",item.strip())
                        for end_c in end_characters:
                            end_index = item_stripped.find(end_c)
                            if end_index != -1:
                                item_stripped = item_stripped[:end_index]

                        # try and get the url, if its 404 or 500 then its invalid, let us know and trigger the error flag
                        code = getResponseCode(item_stripped)
                        if code[0] in [404,403,500]:
                            err = 1
                            print(file+" Code:"+str(code[0])+" Line "+str(line_num)+"("+str(char)+"):"+item_stripped)

                        # check for missing anchors
                        elif "#" in item_stripped and \
                            code[1] is not None \
                            and 'href=\"'+item_stripped[item_stripped.find("#"):]+'\"' not in code[1]:
                            print(file + " Missing Anchor Line " + str(line_num) + "(" + str(
                                char) + "):" + item_stripped)
                    char+=len(item)
                line_num+=1
exit(err)