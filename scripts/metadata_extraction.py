
# coding: utf-8

# In[22]:


from tika import parser
import json
import os


# In[23]:


mp3_metadata_list =[]


# In[24]:


def parse_metadata_for_mp3(absolute_file_path):
    mp3_metadata = parser.from_file(absolute_file_path)["metadata"]
    mp3_metadata["storage:path"] = absolute_file_path
    mp3_metadata_list.append(mp3_metadata)


# In[25]:


data_directory_path = "D:/Sem1/INF551/Project/Data"
output_path = "D:/Sem1/INF551/Project/index"
if os.path.isdir(data_directory_path):
    for filename in os.listdir(data_directory_path):
        parse_metadata_for_mp3(os.path.abspath(os.path.join(data_directory_path, filename)))
    #print json.dumps(mp3_metadata_list, indent =4, sort_keys = True)
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    with open(os.path.join(output_path, "mp3_metadata.json"), 'w+') as f:
        json.dump(mp3_metadata_list, f)
        


# In[26]:


parsedPdf = parser.from_file("D:\Sem1\INF551\Project\Data\John F. Kennedy - Inaugural Address.pdf")
content = parsedPdf["content"].replace('\n','').replace('\t','').encode("ascii", "ignore")
print json.dumps(content, indent =4, sort_keys = True)

