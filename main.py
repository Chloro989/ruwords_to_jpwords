import random
import pandas as pd
from termcolor import colored
from gensim.models.word2vec import Word2Vec

model_path = r"C:\Users\ggZubrowka\Desktop\python\python_annki-card\latest-ja-word2vec-gensim-model\word2vec.gensim.model"
model = Word2Vec.load(model_path)

print(colored("\nTo finish the program, enter '0' \n","magenta"))


d = pd.read_csv('Russian_words to Japanese.csv', header=None, index_col=0, squeeze=True, encoding="shift-jis",skiprows=1).to_dict()



template = "*"*15 + "\nRussian word:{}\nTranslate it into Japanese:\n" + "*"*15

while True:
    #Show Russian words
    word = random.choice(list(d.keys()))
    print(colored(template.format(word), "red"))



    #Input Japanese words
    answer = input()

    #Show if the word you input matches the  Russian word
    
    if answer == "0":

      print("Exit")
      break
     
    elif answer == d[word]:
      print(colored("\nYou got the correct answer!\n" , "white"))
      removed_value = d.pop('{}'.format(word))
      
      if len(d) == 0 :
        print(colored("You have answered all the questions" , "cyan"))
        break
    
    elif answer != d[word]:
      try :
        print("The similarity was " + "{}".format(model.wv.similarity('answer', '{}'.format(d[word]))))

        if model.wv.similarity('answer','{}'.format(d[word])) >= 0.3 :
          print(colored("\nYou got the correct answer!\n" , "blue"))
        
          removed_value = d.pop('{}'.format(word))

          if len(d) == 0 :
           print(colored("You have answered all the questions" , "cyan"))
           break

        else:
          print(colored("\nWrong answer!" , "cyan"))
          print(colored(f"The correct answer was {d[word]}\n", "cyan"))     
        
      
      except KeyError as error:
        print(colored("\nWrong answer!" , "cyan"))
        print(colored(f"The correct answer was {d[word]}\n", "cyan"))

      """if model.wv.similarity('answer','{}'.format(d[word])) >= 0.3 :
          print(colored("\nYou got the correct answer!\n" , "blue"))
        
          removed_value = d.pop('{}'.format(word))

          if len(d) == 0 :
           print(colored("You have answered all the questions" , "cyan"))
           break

      else:
          print(colored("\nWrong answer!" , "cyan"))
          print(colored(f"The correct answer was {d[word]}\n", "cyan"))     """
        
    """else:
      print(colored("\nWrong answer!" , "cyan"))
      print("The similarity was" + "{}".format(model.wv.similarity('answer', '{}'.format(d[word]))))
      print(colored(f"The correct answer was {d[word]}\n", "cyan"))"""
    
