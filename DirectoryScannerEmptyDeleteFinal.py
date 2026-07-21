##################################################################
# Importing required Libararies
###################################################################

import sys
import os
import time
import schedule

####################################################################
#
#   Function Name: DirectoryScanner
#   Input        : Name of Directory
#   Description  : Deletes all empty files periodically
#   Date         : 19/07/2026
#   Author       : Vishal      
# ##################################################################   

def DirectoryScanner(DirectoryPath):
    Border = "-"*40

    timestamp = time.ctime()
    LogFileName = "Marvellous%s.log"%(timestamp)
    LogFileName = LogFileName.replace(" ", "_")
    LogFileName = LogFileName.replace(":", "_")

    Ret = False

    Ret = os.path.exists(DirectoryPath)
    if (Ret == False):
        print ("Marvellous Automation error: There is no such Directory with name", DirectoryPath)
        return

    Ret = os.path.isdir(DirectoryPath)
    if (Ret == False):
        print ("Marvellous Automation error: It is not a Direcotry with name", DirectoryPath)
        return

    
    print ("Log File gets created with name:", LogFileName)

    fobj = open (LogFileName, "w")
    fobj.write(Border+"\n")
    fobj.write ("Marvellous automation script\n")
    fobj.write(Border+"\n\n")

    fobj.write ("Files from the directory are:\n\n")
    fobj.write(Border+"\n")

    TotalFiles = 0
    EmptyFile  = 0

    for FolderName, SubFolder, Filename in os.walk(DirectoryPath):
        for fname in Filename:
            TotalFiles = TotalFiles +1

            fname = os.path.join(FolderName,fname)
            fobj.write(f"{fname}: {os.path.getsize(fname)} bytes\n")

            if (os.path.getsize(fname) == 0):
                EmptyFile = EmptyFile + 1
                os.remove(fname)

            fobj.write(f"{fname}")
            fobj.write(fname+"\n")

    fobj.write(Border+"\n")
    fobj.write(f"Total Files scanned: {TotalFiles}\n")
    fobj.write(f"Total empty Files found and deleted: {EmptyFile}\n")
            
    fobj.write(Border+"\n")
    fobj.write("Log files get created at: " +timestamp)
    fobj.write("\n"+Border+"\n")
        
    fobj.close()

#############################################################################################
# # Function Name:    main
# Input        :    Command Line Arguments
# Description  :    It controls the script
# Date         :    19/07/2026
# Author       :    Vishal 
# ##################################################################################################
  
def main():
    Border = "-"*40

    print (Border)
    print ("Marvellous autoamation script")
    print (Border)

    if (len(sys.argv)==2):

        if (sys.argv[1]=="__h" or sys.argv[1]=="__H" ):
            print ("This automation script is used to traverse in directory")
            print ("For better usage please check __u flag")

        elif (sys.argv[1]=="__u" or sys.argv[1]=="__U"):
            print ("Please execute the script as")
            print ("Python Filename.py Directoryname")
            print ("Directory name should be absolute path")

        else:
                       
            schedule.every(1).minute.do(DirectoryScanner, sys.argv[1])
            
            while True:
                schedule.run_pending()
                time.sleep(1)

    else:

        print ("Invalid number of argument")
        print ("please use __h or __u for more info")

    print (Border)
    print ("Thank you for using Marvellous script")
    print (Border)

    
##################################################################
# Starter of Automation Script
###################################################################

if __name__ == "__main__":
    main()
