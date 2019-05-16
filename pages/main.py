from query import *
from database import *
from django.shortcuts import render

#import sys
#sys.path.insert(0, '../parser')
#from parser import sentence_parse

#from nltk import stanford
#from nltk.parse.stanford import StanfordDependencyParser
import syn_calc
import sentence_parse





userInput = ""

if __name__ == "__main__":
    print("Program begin")
    db = Database()
    db.import_data("data.csv")
    #print(db.students[1])
    #print(db.numstudents)

    # create UI here, get first input
    #userInput = ui.get_input()
    #userInput = "What is the class average?"
    def query(request):
        if request.method == "post":
            #userInput = request.post['myValue']
            userInput = "What is the class average?"
    while userInput not in ["exit", "Exit", "quit", "Quit"]:
        print(userInput)

        originalQuestion = userInput
        print(originalQuestion)
        processedQuestion = syn_calc.pre_process_question(originalQuestion)
        print(processedQuestion)

        splitSentences = sentence_parse.is_complex(processedQuestion)
        print(splitSentences)
        break
        #extract info here
        calc = syn_calc.extract_calc(processedQuestion)
        print(calc)
        break
        q = Query()
        result = db.process_query(q)
        print(result)
        if len(result) == 0:
            pass
            #ui.output_result("No student matches selection criteria")
            def home(request):
                from pages.namer import output
                return render(request, "home.html", {"output": output})
        else:
            pass
            #ui.output_result(result)
            def home(request):
                return render(request, "home.html", {"output": result})

        #get new input
        #userInput = ui.get_input()
        userInput = "exit"

    print("\n\nProgram exit")
