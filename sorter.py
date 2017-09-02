'''
Created on Feb 16, 2015

@author: Ben
'''
import exifread
import os
import shutil
# Open image file for reading (binary mode)

dir_Name = 'D:\\Unsorted Pics\\100CANON'
dir_To = 'D:\Picture Backup'
months = ['-1','January','February','March','April','May','June','July','August','September','October','November','December']

filenames = next(os.walk(dir_Name))[2]

for pic in filenames:
    fullpath = dir_Name + '\\' + pic
    f = open(fullpath, 'rb') 
    
    try:
        tags = exifread.process_file(f)
        
        for tag in tags.keys():
            if tag in ('Image DateTime'):
                lastYear = ''
                lastMonth = ''
                count = 0
                dtcreated = str(tags[tag])
                year = dtcreated[:4]
                month = dtcreated[5:7]
                
                if not month and not year:
                    year = lastYear
                    month = lastMonth
                    
                else:
                    lastYear = year
                    lastMonth = month
                    
    #print fullpath + ': ' + year + ': ' + month
        year_Path = dir_To + '\\' + year
        to_Path = dir_To + '\\' + year + '\\' + month + ' ' + months[int(month)]
        #print to_Path  
              
        #find year and month directory   
        if not os.path.isdir(year_Path):
            #Create it
            os.mkdir(year_Path)
            
            print 'creating directory: ' + year_Path
            
        if not os.path.isdir(to_Path):
            os.mkdir(to_Path)
            
        shutil.copy2(fullpath, to_Path + '\\' + pic)            
    except:
        print 'failed to process: ' + fullpath 

                    
    
    #print 'Done'
            
            