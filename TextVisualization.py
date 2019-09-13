import nltk
import collections
from wordcloud import WordCloud
import matplotlib.pyplot as plt

class TextVisualization:
    def __init__(self,text):
        self.text = text
        self.word_list = nltk.word_tokenize(self.text)
        self.freq = collections.Counter(self.word_list)
        self.freq_dict = dict(self.freq)
        print (self.freq_dict)

    def word_cloud(self):
        text = " ".join([(k + " ") * v for k, v in self.freq_dict.items()])
        wordcloud = WordCloud(background_color="white").generate(text)
        fig = plt.figure()
        fig.suptitle('Word Cloud', fontsize=20)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

    def word_barplot(self):
        top_10 = self.freq.most_common(10)
        freq_dict = dict(top_10)
        fig = plt.figure()
        fig.suptitle('Bar Plot of top 10 words', fontsize=20)
        plt.bar(range(len(freq_dict)), list(freq_dict.values()), align='center')
        plt.xticks(range(len(freq_dict)), list(freq_dict.keys()))
        plt.show()
