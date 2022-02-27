from extract_data import *
from Questgen import main
qe= main.BoolQGen()
qg=main.QGen()
from pprint import pprint
import nltk
nltk.download('stopwords')

        



def generate_question(text_data):
    boolean_question=[]
    mcq_question=[]
    payload={"input_text":text_data,"max_questions":5}
    
    b_q=qe.predict_boolq(payload)
    
    '''output=qg.predict_mcq(payload)
    print(output)
    mcq_q=[]
    
    try:
        for x in output["questions"]:
            ques={
                "question":x["question_statemet"],
                "options":x["options"],
                "answer":x["answer"]
            }
            mcq_q.append(ques)
    except:
        pass
    output=qg.predict_shortq(payload)
    short_qu=[]
    try:
        for x in output["questions"]:
            ques={"question":x["Question"],
                  "answer":x["answer"]}
            short_qu.append(ques)
            
    except:
        pass'''
    return b_q#,mcq_q,short_qu

def generate_one_word(text_data):
    payload={"input_text":text_data}
    output=qg.predict_mcq(payload)
    #print(output)
    mcq_q=[]
    
    try:
        for x in output["questions"]:
            ques={
                "question":x["question_statement"],
                #"options":x["options"],
                "answer":x["answer"]
            }
            mcq_q.append(ques)
    except:
        pass
    return mcq_q






