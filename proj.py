import PyPDF2
import re



text = ""
with open("icsfin.pdf" , "rb") as pdfFile:
    reader = PyPDF2.PdfFileReader(pdfFile)
    pages = reader.numPages
    for i in range(1 , pages-2):
        
        page = reader.getPage(i)
        data = page.extract_text()
        text = text + data



#some unwanted data follow the same pattern as the wanted data. This is a way of solving it
#--------------------------------------------------
text = text.replace("(a)" , "(a )")
text = text.replace("(e)" , "(e )")

text = text.replace("A." , "a)")
text = text.replace("E." , "e)")
text = text.replace("ime)" , "imE)")


text = text.replace("fragment:" , "fragment?")
text = text.replace("\n6\n))" , "6))")

text = text.replace("C." , "c)")
text = text.replace("B." , "b)")
text = text.replace("D." , "c)")
text = text.replace("int a) { a = 5 ;" , "int A) { A = 5 ;")
#("3\n7\n)

for i in range(4 , 10):
    text =text.replace("3\n"+str(i)+"\n)" , "3"+str(i)+"\n)")
#-----------------------------------------------------------------------------

def findMatches(compile):
    pattern = re.compile(compile)
    matches = pattern.finditer(text)
    return matches 

firstChoice = ""

for match in findMatches("a\)"):
    
    span = list(match.span())
    firstChoice = firstChoice  +str(span[0]) + " " 
firstChoice = firstChoice.split()
firstChoice = list(firstChoice)




lastChoice = ""
for match in findMatches("e\)"):
    #print(matches)
    span = list(match.span())
    lastChoice = lastChoice + str(span[0])  + " "
lastChoice = lastChoice.split()
lastChoice = list(lastChoice)

Ques= ""

for match in findMatches(r"\b([0-9]|[1-9][0-9])\b[\n][)]"):
    span = list(match.span())
    Ques = Ques + str(span[0])  + " "
    #print(matches)
    
Ques = Ques.split()
Ques = list(Ques)
matchesark = ""
 
newLine = ""

for i in range(len(lastChoice)):
    for j in range(int(lastChoice[i]) , len(text)):
        if text[j] == "\n":
            newLine = newLine + str(j) + " "
            break
   
newLine = newLine.split()
newLine = list(newLine)

#----------------------------------------------------------------------------------------------------
#imatchport requests
#imatport json

#for i in range(len(AS)):
    
    #url = "https://api.telegramat.org/bot5473698118:AAGL58lGyofzpwL2sOEHq9PFLvYla44matchrfs/sendPoll"

    #paramatcheters = {

            #"chat_id" : "1760611121",
            #"question": text[int(Q[0]): int(first[0])] , 
            #"options" : json.dumatchps([text[int(first[i]): int(third[i])]]),
            #"is_anonymatchous" : False , 
           # "type"    : "regular",
        #}
    #response = requests.get(url , data = paramatcheters )
#------------------------------------------------------------------------------
# i was planing on asking the questions in a telegramatch bot , but because the lingth of the question is not enough i could not :(

answer = " "
for i in range(len(firstChoice)-1):
    if answer!= "":
        
        print(text[int(Ques[i]): int(firstChoice[i])].replace("\n" , ""))
        print(text[int(firstChoice[i]): int(lastChoice[i])].replace("\n" , ""))
        answer = input("Enter ur answer (press enter to leave)")
        
       # answer = input("Enter ur answer(press enter to finsh)")