from time import time

def log(filename):                
    def _decorate(func): 
        with open(filename, "w") as logfile:
            pass  
        def _inner(*args):      
            with open(filename,"a") as logfile:          
                logfile.write(f"{time():.7f}: {func.__name__}{args}\n")
                func(*args)          
        return _inner
    return _decorate


@log("log.out")                
def original(message):          
    print(f"original: {message}")
    
if __name__ == '__main__':
    for i in range(5):
        original(str(i))
