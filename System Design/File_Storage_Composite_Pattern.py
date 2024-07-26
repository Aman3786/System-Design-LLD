# Composite Design Pattern for Creating FileStorage like System which is present in windows,linux...

# FileManager Class: Abstract Class for declaring add(), remove(), ls() function to create FileStorage system.
# File Class: Class for creating & showing File in FileStorage System
# Directory Class: Class for creating, deleting and showing Directory & File in FileStorage System


from abc import ABC, abstractmethod

class FileManager(ABC):
    def add(self,*args):
        pass
    
    def remove(self,*args):
        pass
    
    @abstractmethod
    def ls(self):
        pass
    
    
class File(FileManager):
    def __init__(self, name, filetype, size):
        self.name = name
        self.filetype = filetype
        self.size = size
        
    def ls(self):
        print(f"FileName: {self.name}, Type: {self.filetype}, Size: {self.size}")
        
        
class Directory(FileManager):
    def __init__(self,name):
        self.directory_name = name
        self.filesystem = []
        
    def add(self,directory):
        self.filesystem.append(directory)
        
    def remove(self, directory):
        self.filesystem.remove(directory)
        
    def ls(self):
        print(f"{self.directory_name}/")
        for directory in self.filesystem:
            directory.ls()
            
            
if __name__ == "__main__":
    lld = Directory("System Design")
    
    lld_1 = Directory("Singleton")
    lld1_file1 = File(name="Singleton_Pattern.txt",filetype="TXT",size="10 KB")
    lld_1.add(lld1_file1)
    
    lld_2 = Directory("Observer")
    lld_21 = Directory("Observer_Sub")
    lld21_file1 = File(name="Observer_Sub_Pattern.js",filetype="JS",size="15 KB")
    lld_21.add(lld21_file1)
    lld_2.add(lld_21)
    
    lld.add(lld_1)
    lld.add(lld_2)
    
    lld.ls()
    
    