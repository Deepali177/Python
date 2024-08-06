def Files():
    import os
    from subprocess import getstatusoutput
    os.system("tput setaf 10")
    print("*************************************************************************")

    os.system("tput setaf 10")
    name = "\" \t\t\t\t      BOD Checkout\""
    os.system("echo {0} | figlet -f wideterm -d ./fonts/".format(name))
    os.system("tput setaf 10")
    print("*************************************************************************")
  
