# Gonna be Selenium project
import polib
import sys
from translator_selenium import SeleniumTranslator

if __name__ == "__main__":
	if len(sys.argv) > 1:
		poIn = sys.argv[1]
		poOut = sys.argv[2]
	else:
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