from nltk.text import Text

content = """
Hey there! NLP is like teaching computers to understand and talk like people do. Just like we talk to our friends,
NLP helps computers understand and talk to us. It's like magic words that make the computer understand stories, questions, and even jokes!
So, NLP helps computers become super smart and friendly, just like having a robot friend.
Happy learning on NLP!!!!!
computers are good to learn
"""

text = Text(content)

# Find and display instances of the word 'oil' in the text
text.concordance('computers')
