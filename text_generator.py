import openai
import os
from playsound import playsound
from gtts import gTTS

openai.api_key = "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"

def main():

    while True:
        ask = input("\nIntroduce tu pregunta: ")

        if ask == "exit":
            break


        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=ask,
            n=1,
            max_tokens=2048
        )

        print("--------\n",response.choices[0].text,"\n------------")
        try:
            text = response.choices[0].text
            speech = gTTS(text=text,lang="es",slow=False)
            speech.save("..\TextGenerate\data\\texto.mp3")
            playsound("..\TextGenerate\data\\texto.mp3")
        except Exception as e:
            print(e)

        input()
        os.system("cls" if os.name == "nt" else "clear")



if __name__ == "__main__":
    main()