import nltk
from nltk.tree import Tree as Tree
from nltk import word_tokenize, pos_tag
from stanfordcorenlp import StanfordCoreNLP

# the file that run the stanfordcoreNLP 
from Stanford_Parse import Parse
import re 

#nlp = StanfordCoreNLP(r'C:\Users\wangtao\Documents\NLP_project\stanford-corenlp-full-2018-10-05')
#tree = Tree.fromstring(str(nlp.parse(sentence)))
#tags = nlp.pos_tag(sentence)


class Sentence_Detector:
    
    def detect_p (tree): #detect if it contains p_clause
    
        child_nodes = [child.label() for child in tree.subtrees() if isinstance(child, nltk.Tree)]
        return (tree.label()=='PP') and ('SBAR' in child_nodes)
     
    def detect_s(tree): # detect the sentence sturcture
        child_nodes = [child.label() for child in tree.subtrees() if isinstance(child, nltk.Tree)]
        return (tree.label()=='SBARQ') and ('SBAR' in child_nodes)
        
    def detect_conj(tree): #detect the conjunction
        child_nodes = [child.label() for child in tree.subtrees() if isinstance(child, nltk.Tree)]
        return (tree.label()=='SBARQ') and ('CC' in child_nodes)
# extract the subsentence
    def extract_sbar(tree):# extract the subsentence 
        child_nodes = [child.label() for child in tree.subtrees() if isinstance(child, nltk.Tree)]
    #if (tree.label() == 'SBARQ') and ('WHPP' in child_nodes):
        return (tree.label()=='SBAR') and ('S'in child_nodes)

# # split sentence using nltk.chunker the RegexParser

    def split_pp(tags):   # ertract the matix PP 
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


    def split_s(tags): # extract the matix clause
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











