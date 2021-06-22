import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import urllib
import matplotlib.pyplot as plt
import argparse

# --- parse argumants --- #
parser = argparse.ArgumentParser(description='Script to count number of workd for the given web page')
parser.add_argument('--weblink', type=str, nargs='+', help='a URL link to web page')
parser.add_argument('--wordcount', type=int, nargs='+', help='minimum number of word count to display')              
args = parser.parse_args()

if __name__ == '__main__':
    # ---- Read a web page - (html code) ---- #
    page =  urllib.request.urlopen(args.weblink[0])
    html_plain = page.read()

    # --- data cleaning (remove html code) --- #
    soup = BeautifulSoup(html_plain,'html.parser')
    soup_text = soup.get_text(strip = True)
    ready_text = soup_text.lower()

    # --- tokenization (make list of all words) --- #
    tokens = [t for t in ready_text.split()]

    # ---- remove stop words --- #
    stop_words = stopwords.words('english')
    clean_tokens = tokens[:]
    for token in tokens:
        if token in stop_words:
            clean_tokens.remove(token)

    # ---- Compute frequency of reach word --- #
    freq = nltk.FreqDist(clean_tokens)
    freq = dict(sorted(freq.items(), key=lambda item: item[1])) 

    # ---- Extract n frequently used words ---- # 
    nwords = min(args.wordcount[0], len(freq))
    x, y =[], []
    for key, val in list(freq.items())[-nwords:]:
        x.append(key)
        y.append(val)

    # ---- plot ---- #
    plt.bar(x, y) 
    plt.xticks(rotation=45)  
    plt.show()

