#yuiCompleteRollup - the complete YUI library in one file 

A Python script to combine all YUI files into one large file. 
Do not use this in production code. It is useful in a test environment where you don't have access to the internet and don't want to host YUI on your own.

##run

####download the yui build to the project folder

- visit http://yuilibrary.com/
- download the zip
- extract it to yuiCompleteRollup project dir

####switch into working dir

    cd yuiCompleteRollup/

####make the script executable

    chmod +x createRollup.py
    
####adapt the yui bild folder name in the script

createRollup.py 

    pathToYui = "yui/"

####run the script    

    ./createRollup.py
    
Now a file named [yuiCompleteRollup.js] was created and you are ready to use it.


##config
Some files are excluded because they are not compatible like "yui-nodejs-min.js".
You can change this by editing the blackList in the createRollup.py

    blackList = ["yui-nodejs-min.js"]

