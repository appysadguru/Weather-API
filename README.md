The REST-API code is present in 'hw2' folder.
The front-end code is present in 'hw3' folder.

    Sign in to AWS Account
    Launch and connect to the instance:
    Under Configure Security Group:
    Set 1) Type: SSH   Source: My IP
        2) Add Rule -> Type: HTTP  PortRange: 80 Source: Anywhere
    https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html

    Connect to WinSCP:
    username: ubuntu
    https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/

    Connect to Putty:
    For Ubuntu:-
    username: ubuntu
    https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html

    INSTALLATION:

    Change to root user:
        sudo -i
    Set up Language and Encoding standards:
        apt-get install language-pack-en
        locale-gen en_GB.UTF-8
    Update apt package:
        apt update
    Install python:
        apt install -y  python3-dev python3-setuptools python3-pip
    Install django:
        pip3 install Django
    Install django REST framework:
        pip3 install djangorestframework
    Create a folder:
        sudo mkdir /var/ccpro1
    To transfer files:
        sudo chown -R ubuntu:ubuntu /var/ccpro1
    Or pull from github
    After transferring the files, start the server:
        nohup python3 manage.py runserver 0.0.0.0:80 &

    HOW TO USE:
        DATA will be delivered in JSON format.
    
    GET List of dates for which weather is available:
        <IPaddress of the instance>/historical/
        Output: list of date records
                DATE as a string
        
    GET Weather information for a particular date:
        <IPaddress of the instance>/historical/YYYYMMDD/
        Input: date(YYYYMMDD) should be or after 20130101
        Output: date record
            DATE as a string
            TMAX as float number
            TMIN as float number
        
    DELETE Weather information for a particular date:
        change the method to: DELETE
        Input: date(YYYYMMDD) should be or after 20130101
        <IPaddress of the instance>/historical/YYYYMMDD/
        
    POST Weather information for a particular date:
        change method to: POST
        <IPaddress of the instance>/historical/
        Input:
        Enter the DATE(number) in the order: YYYYMMDD
        Enter TMAX(float)
        Enter TMIN(float)
    Output:
        Entered DATE as a string
        Entered TMAX as float
        Entered TMIN as float
        
    URL for front-end: <IPaddress of the instance>/hw3/
