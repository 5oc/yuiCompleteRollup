#yuiCompleteRollup - the complete YUI library in one file 

A Python script to combine all YUI files into one large file. 
Do not use this in production code. It is useful in a test environment where you don't have access to the internet and don't want to host YUI on your own.

##run

####ownload the yui build to the project folder

- visit http://yuilibrary.com/
- download the zip
- extract it to yuiCompleteRollup project dir

####switch into working dir

    cd yuiCompleteRollup/

####make the script executable

    chmod +x createRollup.py
    
####adapt the yui bild folder name in the script

- createRollup.py 
    ...
    pathToYui = "../yui?.?.?/"
    ...

####run the script    

    ./createRollup.py


##config
Some modules are excluded because they are not compatible like "yui-nodejs-min.js".
You can change this by edit the blackList array in the script.

    blackList = ["yui-nodejs-min.js"]
    
Or tell the script where the library files are located.

    pathToYui = "../yui3.10.3/"
