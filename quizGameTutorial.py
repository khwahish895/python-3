import tkinter as tk
from google import genai
import json
client = genai.Client(api_key="AIzaSyDSEPS3hIXFtFMYEA4nR8D0YZrOClPBOpQ")
summary = ""
questions = []
prompt = """Generate exactly 10 random quiz questions.

    Return ONLY valid JSON.
    add a string at the end that has a 10 to 15 word summary (one or 2 word per every question) labeled "summary"
    Schema:
    [
    {
        "question": "question",
        "options": ["A","B","C","D"],
        "answer": 0
    },
    {
    "summary": "summary"
    }
    ]

    Rules:
    - "options" must contain exactly 4 options
    - "answer" must be the index (0–3) of the correct option
    - "summary" must contain a 10 to 15 word summary of every question (one or 2 words per question)
    - No extra text outside JSON
    - No explanations
    - No trailing commas


    If format cannot be followed exactly, return: []"""
def load():
    global summary
    global prompt
    global questions
    if summary != "":
        prompt+= "\nExclude these topics: "+summary
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
    )
    responseText = response.text
    if(responseText.startswith("```json")):
        responseText="\n".join(responseText.splitlines[1:-1]).strip()
    questions = json.loads(responseText)
    summary = questions[-1]["summary"]
    print(questions)
load()

root = tk.Tk()
root.geometry("800x600")
bg = "#313131"
buttons = []
btnColors = ["#DA2525","#1381E9","#D308FC","#01FFC8"]
score = 0
currentQuestion = -1


def final():
    finalScoreLabel.config(text="Final Score: "+str(score))
    mainFrame.pack_forget()
    finalFrame.pack(fill=tk.BOTH,expand=True)
def repeat():
    global score
    global currentQuestion
    load()
    finalFrame.pack_forget()
    score= 0
    currentQuestion=-1
    nextQuestion()
    mainFrame.pack(fill=tk.BOTH,expand=True)

mainFrame = tk.Frame(root, bg=bg)
mainFrame.pack(fill=tk.BOTH,expand=True)
mainFrame.rowconfigure(0,weight=3)
mainFrame.rowconfigure((1,2),weight=2)
mainFrame.rowconfigure(3,weight=1)
mainFrame.columnconfigure((0,1),weight=1,minsize=400)
questionLabel = tk.Label(mainFrame, text="Question?", font=("Arial", 34), bg=bg, fg="white", wraplength=700)
questionLabel.grid(row=0,column=0,columnspan=2)
infoLabel = tk.Label(mainFrame, text="Score"+"\nQuestion",bg=bg,fg="white")
for i in range(4):
    buttons.append(tk.Button(mainFrame, text= "Option "+str(i),bg=btnColors[i],font=("Arial",18),fg="white"))
    buttons[i].grid(row=1+i//2,column=i%2,sticky="nswe",padx =20,pady=20)
infoLabel.grid(row=3,column=0,columnspan=2)
finalFrame = tk.Frame(root, bg=bg)
finalFrame.rowconfigure((0,1),weight=1)
finalFrame.columnconfigure(0,weight=1)
finalScoreLabel = tk.Label(finalFrame, text="Final Score",font=("Arial", 34), bg=bg, fg="white")
finalScoreLabel.grid(row=0,column=0)
repeatButton = tk.Button(finalFrame, text="Repeat",font=("Arial",24),bg="green",fg="white",command=repeat)
repeatButton.grid(row=1,column=0,sticky="n")

def checkAnswer(answer):
    global score
    if answer == questions[currentQuestion]["options"][questions[currentQuestion]["answer"]]:
        score+=1
    nextQuestion()

def nextQuestion():
    global currentQuestion
    if currentQuestion+1<10:
        currentQuestion+=1
        questionLabel.config(text=questions[currentQuestion]["question"])
        infoLabel.config(text="Score: "+str(score)+"\nQuestion "+str(1+currentQuestion)+"/10")
        for i in range(4):
            text = questions[currentQuestion]["options"][i]
            buttons[i].config(text = text,command=lambda t = text:checkAnswer(t))
    else:
        final()

nextQuestion()

root.mainloop()