## making wordclouds

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def create_wordcloud(txt, title):

    wc = WordCloud().generate(txt)
    plt.figure(figsize=(18, 14))
    plt.imshow(wc)
    plt.savefig("{}.png".format(title))

if __name__ == "__main__":
    create_wordcloud("Test text met woorden")
