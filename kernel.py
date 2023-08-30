from dictionary import *
import subprocess


def runcommand(command0=[], command1=[], timeout="5"):
    proc0 = subprocess.Popen(command0, bufsize=0, stdout=subprocess.PIPE)
    std_out0, std_err0 = proc0.communicate()
    std_out0 = std_out0.strip()
    proc0.kill()
    proc1 = subprocess.Popen(command1, bufsize=0, stdin=subprocess.PIPE, stdout=subprocess.PIPE)    
    std_out1, std_err1 = proc1.communicate(input=b''+std_out0)
    proc1.kill()
    return std_out1, std_err1
        
def main():
    alphabet = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    i = 0
    while True:
        i += 1
        for password in generateur_recurrent_d_espace(alphabet, "", i):
            print(password)
            std_out, std_err = runcommand(["echo", password], ["python3", "password.py"], 5)
            if std_out == b'0\n':
                print("The password is : " + password)
                exit(0)
        
if __name__ == '__main__':
	main()