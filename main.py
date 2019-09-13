import nltk
from TextVisualization import TextVisualization

text = """he pickle module implements binary protocols for serializing and de-serializing a Python object structure.“Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy. Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” or “flattening”; however, to avoid confusion, the terms used here are “pickling” and “unpickling”."""
img_path = "/media/ekbana/ekbana500/MY GITHUB/Text-Visualization/img/female.jpg"

text_viz = TextVisualization(text=text,image_path=img_path,save_img=True)
# text_viz.word_cloud()
# text_viz.word_barplot()
# text_viz.word_color_pattern()
text_viz.word_mask()