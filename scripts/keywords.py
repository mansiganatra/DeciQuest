
# coding: utf-8

# In[141]:


import sys
import requests
import json

firebase_keywords_url = "https://deciquest.firebaseio.com/keywords.json"
keywordsJsonFilePath = "D:/Sem1/INF551/Project/DeciQuest/data/finalmp3/index/metadata_keywords.json"
metadataJsonFilePath = "D:/Sem1/INF551/Project/DeciQuest/data/finalmp3/index/metadata_transcript.json"
stopwordsFilePath = "D:/Sem1/INF551/Project/DeciQuest/data/finalmp3/index/stopwords.txt"


# In[142]:


deciquest_data = {}
stopwords = []
if metadataJsonFilePath:
    with open(metadataJsonFilePath, 'r') as jf:
        deciquest_data = json.load(jf)
        jf.close()


# In[143]:


def reverse_metadata_string_index(original_dictionary):
    reverse_dictionary = {}
    for key, values in original_dictionary.items():
        for v in values:
            reverse_dictionary[v] = reverse_dictionary.get(v, [])
            reverse_dictionary[v].append(key)

    return reverse_dictionary


# In[144]:


def generate_stopwords_list(stopwordsFilePath):
    with open(stopwordsFilePath, 'r') as f1:
        stopwords = f1.read().splitlines()
    return stopwords
    f1.close()


# In[145]:


def remove_all_unpermitted_special_characters(keywords_list):
    new_keywords_list =[]
    for keyword in keywords_list:
        permitted_keyword = ''.join(literal for literal in keyword if literal.isalnum())
        if permitted_keyword:
            new_keywords_list.append(permitted_keyword)
    return new_keywords_list


# In[146]:


def remove_stopwords(all_metadata_string_list):
#     print(all_metadata_string)
    
    final_all_metadata_string_list = [keyword for keyword in all_metadata_string_list if keyword not in stopwords]
    final_all_metadata_string_list = remove_all_unpermitted_special_characters(final_all_metadata_string_list)
#     final_all_metadata_string = ' '.join(final_all_metadata_string_list)
    
#     print(final_all_metadata_string)
    return final_all_metadata_string_list;


# In[147]:


def generate_metadata_string_index(original_metadata_dict):
    string_metadata_dict = {}
    for key, values in original_metadata_dict.items():
#         print(json.dumps(values, indent =4))
        all_metadata_string = ""
#         print(json.dumps(values))
#         if("content" in values):
#             all_metadata_string += values["content"]
        if("metadata" in values and values["metadata"] is not None):
#             print(json.dumps(values, indent = 4))
            metadata  = values["metadata"]
#             print(type(metadata))
            if("Author" in metadata):
                all_metadata_string += metadata["Author"]
            if("dc:creator" in metadata):
                all_metadata_string += metadata["dc:creator"]
            if("dc:title" in metadata):
                all_metadata_string += metadata["dc:title"]
            if("xmpDM:releaseDate" in metadata):
                all_metadata_string += metadata["xmpDM:releaseDate"]
            if("meta:author" in metadata):
                all_metadata_string += metadata["meta:author"]
        
        all_metadata_string = all_metadata_string.lower()
        all_metadata_string_list = remove_stopwords(all_metadata_string.split(' '))
        string_metadata_dict[key] = all_metadata_string_list
#     print(json.dumps(string_metadata_dict, indent = 4))
    
    return string_metadata_dict
    


# In[148]:


stopwords = generate_stopwords_list(stopwordsFilePath)


# In[151]:


string_metadata_index = generate_metadata_string_index(deciquest_data["data"])
# print(json.dumps(string_metadata_index, indent = 4))


# In[153]:


keywords_index = reverse_metadata_string_index(string_metadata_index)
print(json.dumps(keywords_index, indent = 4))


# In[155]:


dataUploadResponse = requests.put(firebase_keywords_url, data = json.dumps(keywords_index)) 
print("Completed uploading deciquest data to firebase.")

