import nltk
from nltk.tree import Tree as Tree
from nltk import word_tokenize, pos_tag
from stanfordcorenlp import StanfordCoreNLP
from Stanford_Parse import Parse
import logging
import json
import re 

#nlp = StanfordCoreNLP(r'C:\Users\wangtao\Documents\NLP_project\stanford-corenlp-full-2018-10-05')
#tree = Tree.fromstring(str(nlp.parse(sentence)))
#tags = nlp.pos_tag(sentence)


class Sentence_Detector:

    def detect_p (tree):
        child_nodes = [child.label() for child in tree.subtrees() if isinstance(child, nltk.Tree)]
    #if (tree.label() == 'SBARQ') and ('WHPP' in child_nodes):
        return (tree.label()=='PP') and ('SBAR' in child_nodes)
    # detect the sturcture 

    def detect_s(tree):
        child_nodes = [child.label() for child in tree.subtrees() if isinstance(child, nltk.Tree)]
        return (tree.label()=='SBARQ') and ('SBAR' in child_nodes)

# extract the subsentence
    def extract_sbar(tree):
        child_nodes = [child.label() for child in tree.subtrees() if isinstance(child, nltk.Tree)]
    #if (tree.label() == 'SBARQ') and ('WHPP' in child_nodes):
        return (tree.label()=='SBAR') and ('S'in child_nodes)

    def split_pp(tags):
        grammar = r"""P_CLAUSE:{<IN><DT>?<NN.*|PRP>?<W.*|NN.*><VB.*><JJ.*>?<IN|TO>?<NN.*|PRP|CD>?<IN|TO>?<NN.*|PRP|CD>?}
                  PP:{<IN|TO><NN.*|PRP|CD>}
                  CLAUSE:{<W.*><VB.*><DT|PRP$>?<JJ.*>?<NN.*|PRP|CD>+<PP>?}"""
        cp = nltk.RegexpParser(grammar)
        p = cp.parse(tags)
        chunks = []
        for subtree in p.subtrees(filter=lambda t: t.label() == 'P_CLAUSE'):
             chunk = ""
             for leave in subtree.leaves():
                 chunk += leave[0] + ' '
                 chunks.append(chunk.strip())
        return chunks[-1]


    def split_s(tags):
        grammar = r"""P_CLAUSE:{<IN><DT>?<NN.*|PRP>?<W.*|NN.*><VB.*><JJ.*>?<IN|TO><NN.*|PRP|CD><IN|TO>?<NN.*|PRP|CD>?}
                PP:{<IN|TO><NN.*|PRP|CD>}
                CLAUSE:{<W.*><VB.*><DT>?<JJ.*>?<NN.*|PRP|CD>+<PP>+}"""
        cp = nltk.RegexpParser(grammar)
        p = cp.parse(tags)
        chunks = []
    for subtree in p.subtrees(filter=lambda t: t.label() == 'CLAUSE'):
        chunk = ""
        for leave in subtree.leaves():
            chunk += leave[0] + ' '
            chunks.append(chunk.strip())
    return chunks[-1]











