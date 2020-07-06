import split_into_sentences as splitter
import sys
import random
import os

def markov_chain(file_path: str):

    ### if file doesn't exist, exit immediately
    if not os.path.isfile(file_path):
        print("[ERROR] Invalid path.")
        sys.exit()

    chain = {}
    first_words = []

    with open(file_path, "r", encoding="utf8") as file:
        
        lines = file.readlines()

        for line in lines:
            
            ### removing '\n' character and splitting line into sentences
            line = line[:-1]
            sentences = splitter.split_input_into_sentences(line)
            
            ### splitting each sentence into words and building Markov Chain
            for sentence in sentences:
            
                words = sentence.split(" ")
                first_words.append(words[0])

                for i in range(0, len(words) - 1):
                    
                    if not words[i] in chain:

                        chain[words[i]] = []
                        
                    chain[words[i]].append(words[i+1])

    return chain, first_words


def generate_message(markov_chain: dict, first_words: list, sen_count: int) -> str:

    message = ""

    for i in range(0, sen_count):

        sentence = random.choice(first_words)
        last_word = sentence

        while last_word in markov_chain:

            last_word = random.choice(markov_chain[last_word])
            sentence += (" " + last_word)

        message += (sentence + " ")

    return message

def main():

    if len(sys.argv) < 3:

        print("usage: path - path to file with testset, n - number of sentences to generate")
        sys.exit()

    sentences_count = int(sys.argv[2])
    chain, first_words = markov_chain(sys.argv[1])

    message = generate_message(chain, first_words, sentences_count)

    print(message)

main()