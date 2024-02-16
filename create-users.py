#!/usr/bin/python3
import os
import re
import sys

def main():
    for line in sys.stdin:
        match = re.match(r'^\s*#',line) #this line will create a pattern that matches the number of whitespace characters ('\s*') followed by the '#'. It also checks whether the line starts with a '#' or not. 
        if match:
            continue
        match = re.match(" ",line)
        fields = line.strip().split(':') #strip any whitespae and split into an array
        if match or len(fields) != 5: #this checks if the line starts with a '#' or if the number of fields in 'fields' list is not equal to 5. It checks for '#' so it can skip them and move onto lines with actual commands. 
            continue #the continue here is for the FOR loop. We skip the line if it starts with a # or does not have five fields because it makes the scripts only process valid data and reduces the total number of errors. 
        username = fields[0]
        password = fields[1]

        gecos = "%s %s,,," % (fields[3],fields[2])

        groups = fields[4].split(',') #this line gets the fifth element in the 'fields' list and splits the string itno a list of substrings using ,
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        #print cmd
        os.system(cmd) #os.system allows for user to execute shell commands using Python and cmd is a variable containing the command user wants to execute
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        #print cmd
        os.system(cmd)
        for group in groups: #this FOR loop searches for each element in the obkect "groups" and will iterate over each elements
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()
