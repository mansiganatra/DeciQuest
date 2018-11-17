
# coding: utf-8

# In[1]:


import os
import sys


# In[17]:


data_directory_path = "D:/Sem1/INF551/Project/DeciQuest/data/projectmp3/"
if os.path.isdir(data_directory_path):
    count=1
    for foldername in os.listdir(data_directory_path):
        print(foldername)
        new_name =  str(count)
        os.rename(os.path.join(data_directory_path, foldername),os.path.join(data_directory_path, new_name))
        folderpath = os.path.abspath(os.path.join(data_directory_path, foldername))
#         for filename in os.listdir(folderpath):
#             print(filename)
#             if(".mp" in filename):
#                 os.rename(os.path.join(folderpath, filename),os.path.join(folderpath, new_name + '.mp3'))
#             elif(".pdf" in filename):
#                 os.rename(os.path.join(folderpath, filename),os.path.join(folderpath, new_name + '.pdf'))
        count+=1


# In[5]:


pwd

