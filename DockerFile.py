#!/usr/bin/env python
# coding: utf-8

# In[1]:



#    ----------------------------------------------------------------------------------------------------------------     #


import os
def check_if_string_in_file(file_name, string_to_search):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return True
    return False

# Searching keywords to start dockercontainer
if check_if_string_in_file('Main.html', '<html>'):
    os.system('echo "Yes, string found in file" ')
    os.system('sudo docker -divt /root/Project-MLOps:/usr/local/apache2/htdocs/ --name Docker_OS httpd')
    

else:
    os.system('echo "Yes, string found in file" ')
    os.system('sudo docker -divt /root/Project-MLOps:/root/ --name Docker_OS docker1')
    
    
#    -----------------------------------------------------------------------------------------------------------------     #


# In[ ]:




