# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 12:40:30 2019

@author: rohit
"""
import glob
import json

path = 'D:/Rohith/Code/freshworks/'
def merger(path,file_prefix,merge,max_size_bytes):
    files = []
    count=0
    for f in glob.glob("*"):
        if file_prefix in f:
            files.append(f)
    print(files)
    sorted(files)
    a = open(path+"\\"+files[0])
    pre_data = a.read()
    pre_data = json.loads(pre_data)
    a.close()
    
    merged = pre_data
    
    for ele in files[1:]:
        f = open(path+"\\"+ele,'r')
        data = f.read()
        #print(data)
        post_data = json.loads(data)
        for key in post_data.keys():
            if(key in merged.keys()):
                for i in (post_data[key]):
                    merged[key].append(i)
        f.close()
    print(merged)
    merged_str = json.dumps(merged)
    
    #print(merged_str)    
    #merged_json = json.loads(merged_str)
    
    count += 1
    file = open(path+"\\"+merge+str(count)+".json",'w')
    if(len(merged_str) <= max_size_bytes):
        file.write(merged_str)
    file.close()
    
merger(path,"data","merge",1000000)