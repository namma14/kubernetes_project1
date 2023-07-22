# writing a prog to crate and activet the virtal environment

# pre-reqisite to create and active virtual env. Install virtual environment module
# pip install virtualenv
# command to activate virtual environment in windows: .\myprojectenv\Scripts\activate.ps1\
# command to activate virtual environment in Linux/Mac : source myprojectenv/bin/activate (myprojectenv is the name of environment)

''' If virtual environment won't get activated on windows then follow below link and steps:
Link:https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows#:~:text=Restart%20you%20system%20and%20try,successfully%20then%20it's%20should%20work.&text=To%20install%20a%20virtual%20environment,pip%20install%20virtualenv
Steps:
Step1:Search PowerShell Right click on Windows PowerShell and Run as administrator.
Step2:Put below command and hit enter.
Step3:Set-ExecutionPolicy Unrestricted -Force
Step4:Restart you system and try to activate python virtual environment.
Step5:if your virtual environment was created successfully then it's should work.'''

# to exit virtual environment use deactivate command
# if we have to use virtualenv interpreter then ctrl+shift+p click onpython:selectinterpreter and select the virtual env interpreter
# To Delete a virtual environment delete the folder myprojectenv created in system
# To get the complete list of modules/packages installed in any environment use 'pip freezee' command. to get the stored modules directly in a file write 'pip freezee > requirement.txt'
# To install all modules available in a environment to a different environment use 'pip install -r .\requirements.txt'
print("Hello")