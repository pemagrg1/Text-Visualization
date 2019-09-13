import nltk
from nltk.corpus import stopwords
import numpy as np
import collections
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image

set(stopwords.words('english'))

class TextVisualization:
    def __init__(self,text=None,image_path=None,top_n=10):
        self.text = text
        self.top_n = top_n
        self.stopwords = set(stopwords.words('english'))
        self.image_path = image_path
        self.word_list = nltk.word_tokenize(self.text)
        self.freq = collections.Counter(self.word_list)
        self.freq_dict = dict(self.freq)


    def word_cloud(self):
        text = " ".join([(k + " ") * v for k, v in self.freq_dict.items()])
        wordcloud = WordCloud(background_color="white").generate(text)
        fig = plt.figure()
        fig.suptitle('Word Cloud', fontsize=20)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

    def word_barplot(self):
        top_10 = self.freq.most_common(self.top_n)
        freq_dict = dict(top_10)
        fig = plt.figure()
        fig.suptitle('Bar Plot of top 10 words', fontsize=20)
        plt.bar(range(len(freq_dict)), list(freq_dict.values()), align='center')
        plt.xticks(range(len(freq_dict)), list(freq_dict.keys()))
        plt.show()

    def word_mask(self):
        pass

    def word_color_pattern(self):
        image_mask = np.array(Image.open(self.image_path ))

        wordcloud = WordCloud(background_color="white", mask=image_mask,
                              )
        wordcloud.generate(self.text)

        image_colors = ImageColorGenerator(image_mask)
        plt.imshow(image_mask, cmap=plt.cm.gray, interpolation="None")
        plt.imshow(wordcloud.recolor(color_func=image_colors), alpha=.8,
                   interpolation='None')
        plt.axis("off")
        plt.show()







