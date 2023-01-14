# Import os module
import os

# Iterate loop to read and print all environment variables
# print("The keys and values of all environment variables:")
# for key in os.environ:
#     print(key, '=>', os.environ[key])

# print("The value of easyPasswordDjangoSecret is: ", os.environ['easyPasswordTestAmbient'])

try:
    os.environ['easyPasswordTestAmbient22']
    print('achou')
except:
    print('nao achou')