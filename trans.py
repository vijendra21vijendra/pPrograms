from googletrans import Translator
rawData = input("say something.. ")

translator = Translator()
done = translator.translate(rawData, src='en', dest='hi')
print(done.text)

# use jupyter for better output
