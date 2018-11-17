
# coding: utf-8

# In[1]:


from tika import parser
import json
import os


# In[2]:


mp3_metadata_dict = {}
amazon_s3_basepath = "http://deciquest.s3.us-east-2.amazonaws.com/data/"


# In[3]:


def parse_metadata_for_mp3(absolute_file_path, key):
    parsedMp3 = parser.from_file(absolute_file_path)
    mp3_metadata = parsedMp3.get('metadata')
    mp3_metadata_dict[key].update(metadata=mp3_metadata)
   

    #print('After adding metadata:' +json.dumps(mp3_metadata_dict[key]))
    #print("Added metadata: " + json.dumps(mp3_metadata))
    #mp3_metadata_list.append(mp3_metadata)


# In[4]:


def parse_data_from_pdf(absolute_file_path, key):
    parsedPdf = parser.from_file(absolute_file_path)
    content_value = parsedPdf.get('content').replace('\n','').replace('\t','').encode("ascii", "ignore")
    mp3_metadata_dict[key].update(content=content_value)
   
    #print('After adding content:' +json.dumps(mp3_metadata_dict[key]))
    #print json.dumps(content, indent =4, sort_keys = True)
    


# In[8]:


data_directory_path = "/home/ec2-user/project/DeciQuest/data/projectmp3"
output_path = "/home/ec2-user/project/DeciQuest/data/projectmp3/index"
if os.path.isdir(data_directory_path):
    for foldername in os.listdir(data_directory_path):
        key = foldername.split('.')[0]
        if(key not in mp3_metadata_dict.keys()):
            mp3_metadata_dict[key] = {}
        #print("Startin value: " +  json.dumps(mp3_metadata_dict))
        #print(key)
        folderpath = os.path.abspath(os.path.join(data_directory_path, foldername))
        for filename in os.listdir(folderpath):
            filepath = os.path.abspath(os.path.join(folderpath, filename))
            if(".mp" in filename):
                parse_metadata_for_mp3(filepath, key)
                mp3_storage_path = os.path.join(amazon_s3_basepath, key, filename)
                print(mp3_storage_path)
                mp3_metadata_dict[key].update({"storage-path-mp3": mp3_storage_path})
            elif(".pdf" in filename):
                parse_data_from_pdf(filepath, key)
                pdf_storage_path = os.path.join(amazon_s3_basepath, key, filename)
		print(pdf_storage_path)
                mp3_metadata_dict[key].update({"storage-path-pdf": pdf_storage_path})
    #print json.dumps(mp3_metadata_list, indent =4, sort_keys = True)
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    with open(os.path.join(output_path, "metadata_transcript.json"), 'w+') as f:
        json.dump(mp3_metadata_dict, f)
        

