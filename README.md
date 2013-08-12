# yuiCompleteRollup - the complete YUI library in one file 

A Python script to combine all YUI files into one large file. 
Do not use this in production code. It is useful in a test environment where you don't have access to the internet and don't want to host YUI on your own.

## run

switch into working dir

    cd yuiCompleteRollup/

make the script executable

    chmod +x createRollup.py

run the script    

    ./createRollup.py


## config
Some modules are excluded because they are not compatible like "yui-nodejs-min.js".
You can change this by edit the blackList array in the script.

    blackList = ["yui-nodejs-min.js"]
    
Or tell the script where the library files are located.

    pathToYui = "../yui3.10.3/"
