import json
import os

class ParseMessages:
    jsonPath = "./json/"
    targetPath = "./text/"



        
    @classmethod
    def parse(self):
        print("parse start")
        files = os.listdir(self.jsonPath)
        numFiles = len(files)
        processedCount = 0
        while processedCount < numFiles:
            file = files[processedCount]
            print(str(file))
            if not file.startswith('.'):
                self.parseFile(file)
            processedCount = processedCount+1

    @classmethod
    def parseFile(self, fileName):
        file = self.jsonPath + fileName
        messageText = ""
        senderDict = {}
        with open(file) as data_file:    
            data = json.load(data_file)
        for messages in data["messages"]:
            try:
                message = str(messages["content"]) +"\n"
                sender = str(messages["sender_name"])
                if sender in senderDict:
                    senderDict[sender] = senderDict[sender] + message
                else:
                    senderDict[sender] = message
            except:
                print("Whoooops")
        for name in senderDict:
            senderFileName = self.targetPath + name + ".txt"
            with open(senderFileName, "w") as newTxtFile:
                newTxtFile.write(senderDict[name])

def main():
        print("start")
        app = ParseMessages()
        app.parse()
        
if __name__ == "__main__": main()

            


        

