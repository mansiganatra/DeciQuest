
# coding: utf-8

# In[13]:


import sys
import requests
import json

firebase_root_url = "https://deciquest.firebaseio.com/.json"
jsonFilePath = "D:/Sem1/INF551/Project/DeciQuest/data/finalmp3/index/metadata_transcript.json"


# In[14]:


if jsonFilePath:
    with open(jsonFilePath, 'r') as jf:
        deciquest_data = json.load(jf)
        jf.close()


# In[15]:


dataUploadResponse =  requests.put(firebase_root_url, data = json.dumps(deciquest_data))
print "Completed uploading deciquest data to firebase."

