# Gonna be Selenium project
import polib
from translator_selenium import SeleniumTranslator

if __name__ == "__main__":
    poIn = input("Enter dir of po file: ")
    poOut = input("Enter dir of po output:")

    translator = SeleniumTranslator()
    translator.setLang("tr","en")

    poFile = polib.pofile(poIn)

    for i in range(0,len(poFile)):
        poFile[i].msgstr = translator.translate(poFile[i].msgid)
        progress = (i/len(poFile))*100
        print(f"ilerleme: {progress}%")

    poFile.save(poOut)
    translator.exit()