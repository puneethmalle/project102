import os
import shutil

from_dir = "/Users/sujathakamasani/Desktop"
to_dir = "/Users/sujathakamasani/Desktop/project102/Document_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

#Move All the files from downloads folder to Another Folder

for file_name in list_of_files:

    name, extension =os.path.splitext(file_name)

    if extension == "":
        continue
    if extension in['.txt', '.pdf','.doc','.docx']:
         

         path1 = from_dir + '/' + file_name
         path2 = from_dir + '/' + "Documents_Files"
         path3 = to_dir + '/' + "Documents_Files" + '/' + file_name



        #shutil.move(from_dir,path2)
    #else:
       # os.mkdir(path2)
        #shutil.move(path,path2)
       # print(path2)
         if os.path.exists(path2): 
          print("Moving"+ file_name + ".....")        

#Move from path1 ---> path3
          shutil.move(path1,path3)
         else:
            os.makedirs(path2)
            print("moving"+file_name+"....")
            shutil.move(path1,path3)