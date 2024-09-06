import http.client
import urllib.request, urllib.error
import os
import sys
import re



# set some default variables
remove_characters = ['**', '\\n']

# text that tends to be at the end of the url that we need truncate everything past them
end_characters = [')',",","'",'`',"\"",'</a>','</div>',"\\",">","]"]

big_regex = re.compile('|'.join(map(re.escape, remove_characters)))

# if there are any URLs to ignore add here
link_ignore_list = []
link_ignore_list_env = os.getenv("LINK_IGNORE_LIST")
if link_ignore_list_env and len(link_ignore_list_env) > 0:
    link_ignore_list = link_ignore_list_env.split(',')

# Add any repo specific ignores
link_ignore_list_env_2 = os.getenv("inputs.repo_link_ignore_list")
if link_ignore_list_env_2 and len(link_ignore_list_env_2) > 0:
    link_ignore_list.extend(link_ignore_list_env.split(','))

print_valid = os.getenv("print_valid_links") is not None

# If we are given a directory then use it, otherwise assume path is current directory
path = "."
if len(sys.argv) >1  and os.path.exists(sys.argv[1]):
    path = sys.argv[1]

# directory environment overrides the system arguments and default.
directory_env = os.getenv("inputs.directory")
if directory_env and len(directory_env) > 0:
    path = directory_env

pat_env = os.getenv("INPUT_PAT")
if directory_env and len(directory_env) > 0:
    path = directory_env

# list which stores all links to check
links_to_check = []
link_file_map = {}
# Get the response code of the url to see if it exists
def getResponseCode(url):
    content = None
    try:
        req = urllib.request.Request(url,
                                     headers={'User-Agent': 'Mozilla/5.0'})
        conn = urllib.request.urlopen(req)
        # Only get HTML if we have a potential anchor link
        if "#" in url and "pdf" not in url:
            content = conn.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        return [e.code, content]
    except urllib.error.URLError as e:
        return [404, content]
    except http.client.InvalidURL:
        return [200, content]
    return [conn.getcode(), content]

def clean_link(link):
    if link.endswith("."):
        link = link[:link.rfind(".")]
    if link.endswith("'"):
        link = link[:link.rfind("'")]
    if link.endswith("\""):
        link = link[:link.rfind("\"")]
    link_stripped = big_regex.sub("", link.strip())
    for end_c in end_characters:
        end_index = link_stripped.find(end_c)
        if end_index != -1:
            link_stripped = link_stripped[:end_index]
    return link_stripped

def add_link(loc,link):
    # this is a command being ran so difficult to validate in this script, skip it
    if '$(uname' in link:
        return False

    # get just from the http portion if there was more in from of the string we grabbed
    link = link[link.find("http"):]

    # if there is a period at the end, truncate to that period. Other periods may be valid
    # strip various characters that may be in the string
    link_stripped = clean_link(link)
    while link_stripped != link:
        link = link_stripped
        link_stripped = clean_link(link)

    # add link to be checked
    links_to_check.append(link_stripped)

    # store where the link is so we can fix it
    link_file_map[link_stripped] = loc
def check_link(link):
    # try and get the url, if its 404 or 500 then its invalid, let us know and trigger the error flag
    code = getResponseCode(link)
    loc =link_file_map[link]
    if code[0] in [404, 403, 500]:

        # If the link failed, but we are ignoring it then just mention that
        for ignored_link in link_ignore_list:
            if ignored_link in link:
                print(
                    loc + ", " + link + ", Ignored")
                return False

        # print(file+" Code:"+str(code[0])+" Line "+str(line_num)+"("+str(char)+"):"+item_stripped)
        print(
            loc + ", " + link + ", Failed")
        return True

    # check for missing anchors
    elif "#" in link and \
        code[1] is not None \
        and 'href=\"' + link[link.find("#"):] + '\"' not in \
        code[1]:
        print(
            loc + ", " + link + ", Failed - Anchor")
    # print(file + " Missing Anchor Line " + str(
    #     line_num) + "(" + str(
    #     char) + "):" + item_stripped)
    elif print_valid:
        print(
            loc + ", " + link + ", Valid")
    return True


if __name__ == "__main__":
    err = 0
    print("Directory is "+path)
    # Loop through all files in path
    for root, dirs, files in os.walk(path):
        for file in files:
            #  only read file that match template ( txt, md or python notebook)
            if file.endswith(".md") or file.endswith(".txt") or file.endswith(
                ".ipynb"):

                # get content and separate into lines and then separate by spaces
                raw_content = open(os.path.join(root, file), "r").read()
                content = raw_content.split("\n")
                content = [x.split(" ") for x in content]
                loc = os.path.join(root, file)
                # have an incrementer for line number later export
                for line in content:
                    for item in line:

                        if "https://" in item or "http://" in item:
                            if "](" in item:
                                add_link(loc,item[item.find("]"):])
                                # if we get any error  then add it
                                if item[item.find("("):] == item[item.find("]"):]:
                                    continue
                                add_link(loc,item[item.find("("):])
                            else:
                                add_link(loc,item)

    for link in set(links_to_check):
        # if we get any error  then add to err variable
        err = check_link(link) + err
    # if the error is > 1 then set it to 1 to error as 1
    if err > 1:
        err = 1
    exit(err)
