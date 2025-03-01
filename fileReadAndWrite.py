import main
class ReadAndWritetoTxt:
    
    def __init__(self,filePath):
        self.filePath = filePath
    
    def readFromTxt(self):
        try:
            with open(self.filePath,"r") as file:
                line = file.readline()
                while line !="":
                    print(line)
                    line = file.readline()
                    
            
        except FileNotFoundError as e:
            print(f"An error occured: {e}")

txt_reader = ReadAndWritetoTxt("görevListesi.txt")
txt_reader.readFromTxt()
main.main()