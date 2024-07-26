# Chain Of Responsibility Pattern & Null Object Pattern for Logger..

# Classes Used - 
    # LogHandler Class : Abstract Class for declaring Handler function to handle chains of different Log levels.
    # NoneHandler Class : class for Handling None Case. It helps to reduce huge number of None checks in Code.
    # InfoLogHandler Class : class for handling log level - INFO
    # DebugLogHandler Class : class for handling log level - DEBUG
    # WarnLogHandler Class : class for handling log level - WARN
    # ErrorLogHandler Class : class for handling log level - ERROR
    # CriticalLogHandler Class : class for handling log level - CRITICAL
    # FatalLogHandler Class : class for handling log level - FATAL
    # Logger Class : Base Class to instantiate different log levels in a chain.

from abc import ABC, abstractmethod


class LogHandler:
    @abstractmethod
    def handler(self,level,message):
        pass
    
    
class NoneHandler(LogHandler):
    def handler(self,level,message):
        print(f"Log Level '{level}' is not Valid!")
    
    
class FatalLogHandler(LogHandler):
    def __init__(self,next):
        self.next = next
        
    def handler(self, level, message):
        if level.upper() == "FATAL":
            print(f"{level} : {message}")
        else:
            self.next.handler(level,message)
        
        

class CriticalLogHandler(LogHandler):
    def __init__(self,next):
        self.next = next
        
    def handler(self, level, message):
        if level.upper() == "CRITICAL":
            print(f"{level} : {message}")
        else:
            self.next.handler(level,message)
        
    
class ErrorLogHandler(LogHandler):
    def __init__(self,next):
        self.next = next
        
    def handler(self, level, message):
        if level.upper() == "ERROR":
            print(f"{level} : {message}")
        else:
            self.next.handler(level,message)
        

class WarnLogHandler(LogHandler):
    def __init__(self,next):
        self.next = next
        
    def handler(self, level, message):
        if level.upper() == "WARNING" or level.upper() == "WARN":
            print(f"{level} : {message}")
        else:
            self.next.handler(level,message)
        
        
class DebugLogHandler(LogHandler):
    def __init__(self,next):
        self.next = next
        
    def handler(self, level, message):
        if level.upper() == "DEBUG":
            print(f"{level} : {message}")
        else:
            self.next.handler(level,message)
        
        
class InfoLogHandler(LogHandler):
    def __init__(self,next):
        self.next = next
        
    def handler(self, level, message):
        if level.upper() == "INFO":
            print(f"{level} : {message}")
        else:
            self.next.handler(level,message)
            
            
class Logger:
    def __init__(self):
        fatalloghandler = FatalLogHandler(NoneHandler())
        criticalloghandler = CriticalLogHandler(fatalloghandler)
        errorloghandler = ErrorLogHandler(criticalloghandler)
        warnloghandler = WarnLogHandler(errorloghandler)
        debugloghandler = DebugLogHandler(warnloghandler)
        infologhandler = InfoLogHandler(debugloghandler)
        self.handle = infologhandler
        
    def log(self,level,message):
        self.handle.handler(level,message)
        
if __name__ == "__main__":
    logger = Logger()
    logger.log(level="ERROR",message="This is Error log message")
    logger.log(level="INFO",message="This is Info log message")
    logger.log(level="FATAL",message="This is Fatal log message")
    logger.log(level="DEBUG",message="This is Debug log message")
    logger.log(level="ANY",message="This is ANY log message")
        
        
