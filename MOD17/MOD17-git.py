# COMANDOS DO GIT EM PYTHON
  
 # nome de usuário

import os

from getpass import getpass


username = 'freirefellipe'

os.environ['GITHUB_USER'] = username

#!git config --global user.name '${GITHUB_USER}'

 # endereço de email



#usermail = getpass() # variável usermail recebe a função getpass() do pacote getpass
usermail = 'freirefellipe@gmail.com'
os.environ['GITHUB_MAIL'] = usermail

#!git config --global user.mail '${GITHUB_MAIL}'

 # token

usertoken = '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'
os.environ['GITHUB_TOKEN'] = usertoken


# PROJETO



