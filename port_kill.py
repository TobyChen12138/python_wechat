import os
import sys 
kill_cmd = "kill -9 $(lsof -i:%s|awk '{print $2}'|tail -n 2)"

def kill_port(port):
    conv_kill_cmd = kill_cmd % port
    print os.system(conv_kill_cmd)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "error", sys.argv
        exit()
    kill_port(sys.argv[1])
