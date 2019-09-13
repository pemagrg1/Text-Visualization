import nltk
from TextVisualization import TextVisualization

text = """The Russian military has indicated it will supply the Syrian government with a sophisticated air defence system, after condemning a missile attack launched by the US, Britain and France earlier in April. Col Gen Sergei Rudskoi said in a statement on Wednesday that Russia will supply Syria with new missile defence systems soon. Rudskoi did not specify the type of weapons, but his remarks follow reports in the Russian media that Moscow is considering selling its S-300 surface-to-air missile systems to Syria."""

text_viz = TextVisualization(text=text)
text_viz.word_cloud()
# text_viz.word_barplot()