from get_question import *
from extract_data import *

def extract_boolean_question(text_data):
    boolean_question=[]
    for x in text_data:
        b_q=generate_question(x)
        boolean_question.extend(b_q["Boolean Questions"])
    print("Boolean Question")
    for x in range(1,len(boolean_question)):
        print(str(x)+").",boolean_question[x])
  
  
with open("test_data.txt",encoding="utf8") as text_data:
    text_data=text_data.read()
n=1024 
text_data=[text_data[i:i+n] for i in range(0,len(text_data),n)]
print(extract_boolean_question(text_data))      
    