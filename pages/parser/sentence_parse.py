import nltk
from nltk.tree import Tree as Tree
from nltk import word_tokenize, pos_tag
from stanfordcorenlp import StanfordCoreNLP
from Stanford_Parse import Parse
from sentence_detector import Sentence_Detector
import logging
import json
import re 

nlp = Parse()

# detect the structure of sentence. if it is a complex sentence that contains two clause it will return a list of clauses
# they are [p_wh_cluase and wh_clause] p_cluase is an ajunct which means it offers additonal information to the main clause
# according to our task the information about student will be translated to "condition"  and the other would be cauculation
# thus in the next step, the two clauses are processed seperately to extract informaton for conditon and caculation

class is_complex():

    def is_complex(self,tree,tags):
        wh_list = ["what","which","who","how"]
        in_list = ["for","in","at","on","among","to","above","below","between","after","before"]
        b = [t for t in tree.subtrees(filter = detect_s)]
        a = [t for t in tree.subtrees(filter = detect_p)]
        n = len(a)
        a1 = a[0].leaves()
        b1 = b[0].leaves()

        if a and b:
            if n==2:
                if ',' in b1:
                    ss = sentence.split(',')
                    return ss
                else:
                    if b1[0] in wh_list:
                        b2 = [t.leaves() for t in b[0].subtrees(filter = detect_p)][-1]
                        i = -len(b2)
                        return [' '.join(e1[0:i]),' '.join(b2)]
                    if b1[0] in in_list:
                        b2 = [t.leaves() for t in b[0].subtrees(filter = extract_sbar)][-1]
                        i = -len(b2)
                        return [' '.join(b2),' '.join(b1[0:i-1])]
        
            if n==1 and b1[0] in in_list:
                b2 = [t.leaves() for t in b[0].subtrees(filter = extract_sbar)][0]
                i = -len(b2)
                return [' '.join(b2),' '.join(b1[0:i-1])]
            if n==1 and b1[0]in wh_list:
                b2 = [t.leaves() for t in b[0].subtrees(filter = detect_p)][0]
                i = -len(b2)
                return [' '.join(b1[0:i]),' '.join(b2)]
            
        if b and not a:
            #print("only b")
            if ',' in e1:
                ss = sentence.split(',')
                return ss
            else:
                e = [t.leaves() for t in b[0].subtrees(filter = detect_p)]
                s = split_s(sentence)
                return [s,' '.join(e[0])]  
    
        if a and not b:
            if n==2:
                if ',' in a1:
                    ss = sentence.split(',')
                    return ss
                else:
                    if a1[0] in wh_list:
                        e = [t.leaves() for t in a[0].subtrees(filter = extract_sbar)]
                        p = split_pp(sentence)
                        return [' '.join(e[1]),p]
                    if a1[0] in in_list:
                        e = [t.leaves() for t in a[0].subtrees(filter = detect_p)]
                        s = split_s(sentence)
                        return [s,' '.join(e[-1])]
                
            if n==1 :
                try:
                    e = [t.leaves() for t in tree.subtrees(filter = extract_sbar)]
                    p = split_pp(sentence)
                    return [' '.join(e[-1]),p]
            
                except:
                    return [sentence,"simple"]                
        else:
            return [sentence,'simple']

 


#test sentence:
#sentence = "what is john's average"
#sentence = 'between John Marry Joe what is the average score of them in exam2?'
#sentence = 'of thoes who got hihger than 80  what is the average score ?'
#sentence = 'what is the average score of thoes who got higher than 80?'
#sentence = 'for who got higher than 80 what is the average score?'
#sentence = 'For who got higher than 80 in the exams what is the average score of them in exam2?'
#sentence = 'What is their average score in exam2 of thoes who got higher than 80 in exam1'
#sentence = 'what is the average of exam2 for thoes who got higer than 80 in the exams'
#sentence = 'in exam1, who is the higheset?'
#sentence = 'for those who pass the exams who is the best?'
#sentence = "who is the best for thoes who passed the exams"
#sentence = 'On assignment1 assignment2 assignment3 which has the higheset average score'
#sentence = 'among assignment1 assigment2 assighment3 which has the highest score'
#sentence = 'among all of the assignments which has the highest score'
#sentence = 'for those who pass the exams what is the average of thoes who are higher than 80'
#print (tree)
#print(is_complex(tree))

def main(self, sentence):
    tree = Tree.fromstring(str(nlp.parse(sentence)))
    tags = nlp.pos_tag(sentence)
    a = self.is_complex(tree,tags)
        if False:
        print "*********************", sentence
        print "It is a simple sentence."
 
