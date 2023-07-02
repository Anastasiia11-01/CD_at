[![Test and Deploy](https://github.com/Anastasiia11-01/CD_at/actions/workflows/deplo.yml/badge.svg)](https://github.com/Anastasiia11-01/CD_at/actions/workflows/deplo.yml)

# CD Assignment

## Components:

  - Creating Main.py and Test.py files in local terminal and connecting this to github repository, which later on were connected to ubuntu from github.
  - Creating .yml files for github actions
  - Creating secrets for github actions

## Problems:

  - To understand the linux folder system, how to access folder and to store files in there: practicing helped me to get familiar with this.
  - To create a working test file for github: I found out that the test file should not be simply named as test.py, but 'test' word should be only a part of the file's name,
    which is why the file has been named as maindeploy_test.py.
  - To understand what are actually the secrets for the yml file, where to store them and what should be their content: I searched the web and managed to find out that there are 
    different type of secrets (for actions, for enviroment, for account in general).It helped to really good memorize where to store private key(in repository actions) and 
    public key (in authorized_keys on local machine). Also I learned that for connecting github with ubuntu there should be one more SSH key generated and stored in 
    the main settings of github account.
  - To understand the structure of .yml files, which became easier after reviewing other .yml files of other users. Also it took me a while to understand from where to take the
     'uses: actions/checkout@v3' part and it became clearer after checking with toutors.

#### [Some thoughts to share:]

> This was a very difficult assignment.
> I felt like I've been left in a cold deep water without knowing how to swim. 
> It was very helpul to have constant chat possibilities and it clarified a lot of issues I have faced.
> But the most helpfull was the call session.
> I understood you have reasons for not giving more exact explanations or code examples.
> But maybe a good idea would be to arrnage some group video call,
> where you would explain the basics of yml file structure and it's content.
> Thanks a lot for so much time spent with me on this assignment! I really learned it.
    
