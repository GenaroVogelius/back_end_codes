# The objetive was to implement a function called parse that expects a str of HTML as input, extracts any YouTube URL that’s the value of a src attribute of an iframe element therein, and returns its shorter, shareable youtu.be equivalent as a str. Expect that any such URL will be in one of the formats below. Assume that the value of src will be surrounded by double quotes. And assume that the input will contain no more than one such URL. If the input does not contain any such URL at all, return None.
# You may not import any other libraries besides re.

# Formats of inputs:
# http://youtube.com/embed/xvFZjo5PgG0
# https://youtube.com/embed/xvFZjo5PgG0
# https://www.youtube.com/embed/xvFZjo5PgG0
# """<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0" ></iframe>"""
# """<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"""

import re

def main():
    print(parse(input("HTML: ")))



def parse(url):
    try:
        matches = re.fullmatch(r".+((?:http|https).+G0).+", url)
        youtube = matches.group(1)
        new_youtube = re.sub(r"be.com/embed/",".be/", youtube)
        print (new_youtube)
        new_youtube = re.sub(r"(http://www.)","https://", new_youtube)
        print (new_youtube)
        new_youtube = re.sub(r"(http|https)?://www.","https://", new_youtube)
        return new_youtube
    except AttributeError:
        return None


if __name__ == "__main__":
    main()
        
#OTRA FORMA DE HACERLO  
# def parse(s):
#     if re.search (r"<iframe(.)*><\/iframe> ", s):
#         url_pattern = re.search(r" (http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s)
#         if url_pattern:
#             split_url = url_pattern.groups()
#             return "https://youtu.be/" + split_url[3]  

# https://regex101.com/ aca podes ir testeando la regular expresion