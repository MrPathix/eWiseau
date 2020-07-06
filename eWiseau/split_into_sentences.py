import sys

def split_input_into_sentences(inputstr: str):
    
    #inputstr.replace("\n", "")

    exclamations = []
    sentences = []

    ### splitting input on question marks
    questions = inputstr.split("? ")

    for i in range(0, len(questions) - 1):
        questions[i] += "?"

    ### further splitting on exclamation marks
    for question in questions:
        exclamationsplits = question.split("! ")

        for i in range(0, len(exclamationsplits) - 1):
            exclamationsplits[i] += "!"

        for exclamation in exclamationsplits:
            exclamations.append(exclamation)

    ### further splitting on periods
    for exclamation in exclamations:
        declaratives = exclamation.split(". ")

        for i in range(0, len(declaratives) - 1):
            declaratives[i] += "."

        for declarative in declaratives:
            sentences.append(declarative)

    return sentences
