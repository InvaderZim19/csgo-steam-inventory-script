You need to install Python 2.7 first.
Here are directions.

1. Go to https://www.python.org/downloads/

2. Click download python 2.7.11.

3. Go through installation, installing python in your C:\Python27 folder.

4. After it finishes, you need to add python into your path. On windows 10, get to the advanced
System Settings. The window should say system properties. 

5. Within that window, in the Advanced tab, click Environment Variables.

6. Under system variables, find the PATH variable.

7. Edit it, don't delete anything. Add on, "C:\Python27" and "C:\Python27\Scripts\" no quotes. Hit okay.

8. You're done installing python.

Next you need to get to the correct directory within command prompt. 

1. Open your command prompt. (search for cmd or command prompt)

2. You should be in your C:\Users\*yourname* . You want to be on your Desktop, just put the stuff there inside 
a folder. Lets say there's a folder on our desktop called "script".

3. From here, the command "cd" moves us around directories (folders). So from where we are now, the command
"cd Desktop" will take us there.

4. From "C:\Users\*yourname*\Desktop" we want to get to the "script" folder. So we "cd script", and we are 
there.

5. We are in the folder of the script. To run a python script, type in python then the name of the file. Let's 
say our script is called "inventory.py". To run it, "python inventory.py".

End