import nltk
from nltk.corpus import stopwords
import numpy as np
import collections
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image

set(stopwords.words('english'))
saved_img_path = "/media/ekbana/ekbana500/MY GITHUB/Text-Visualization/saved_img/"
class TextVisualization:
    def __init__(self,text=None,image_path=None,top_n=10,save_img=False):
        self.text = text
        self.top_n = top_n
        self.save_img = save_img
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
        if self.save_img:
            plt.savefig(saved_img_path+"word_cloud.jpg")
        plt.show()

    def word_barplot(self):
        top_10 = self.freq.most_common(self.top_n)
        freq_dict = dict(top_10)
        fig = plt.figure()
        fig.suptitle('Bar Plot of top 10 words', fontsize=20)
        plt.bar(range(len(freq_dict)), list(freq_dict.values()), align='center')
        plt.xticks(range(len(freq_dict)), list(freq_dict.keys()))
        if self.save_img:
            plt.savefig(saved_img_path + "word_barplot.jpg")
        plt.show()

    def word_pieplot(self):
        top_10 = self.freq.most_common(self.top_n)
        freq_dict = dict(top_10)
        fig = plt.figure()
        fig.suptitle('Pie Plot of top 10 words', fontsize=20)
        plt.pie((freq_dict.values()),labels=freq_dict.keys(),autopct='%1.2f',startangle=90)
        plt.axis('equal')
        if self.save_img:
            plt.savefig(saved_img_path + "word_pie_plot.jpg")
        plt.show()

    def word_mask(self):
        image_mask = np.array(Image.open(self.image_path))
        wordcloud = WordCloud(background_color="white", max_words=2000,
                       mask=image_mask,
                       contour_width=0.5,
                       contour_color='steelblue')
        wordcloud.generate(self.text)

        if self.save_img:
            file_name = self.image_path.split("/")[-1]
            wordcloud.to_file(saved_img_path + "word_mask_"+file_name)

        # show
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()


    def word_color_pattern(self):
        image_mask = np.array(Image.open(self.image_path ))

        wordcloud = WordCloud(background_color="white", mask=image_mask,
                              )
        wordcloud.generate(self.text)

        image_colors = ImageColorGenerator(image_mask)
        plt.imshow(image_mask, cmap=plt.cm.gray, interpolation="None")
        plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation='None')
        if self.save_img:
            file_name = self.image_path.split("/")[-1]
            wordcloud.to_file(saved_img_path+ "word_color_pattern_"+file_name)
        plt.axis("off")
        plt.show()








