import os
#import format data
from formats import (all_formats, image_files_extensions,
                     office_files_extensions, video_files_extensions)
#import file paths
from paths import (folder_destination, folders_collection, image_files_folder,
                   office_files_folder, video_files_folder)


def check_files(file_extension, target_path):
  #check if folder
  if os.path.isdir(target_path):
    print(str(target_path),'IS A DIR')
    return check_folders(target_path)
  else:
    if file_extension not in all_formats:
      return folder_destination
    #check if file extension is an image extension
    if file_extension in image_files_extensions:
      return  image_files_folder
    #check if file extension is a video extension
    if file_extension in video_files_extensions:
      return video_files_folder
    #if none of the above let the destination be the same
    #check if the file is an office extension
    for types in office_files_extensions:
      if file_extension in office_files_extensions[types]:
        return office_files_folder
  print(all_formats)

def check_folders(target_path):
  print("CHECKING FOLDER")
  video = 0
  folder = 0
  other = 0
  image = 0
  office = 0
  destinations = [video_files_folder,folders_collection,folder_destination,image_files_folder,office_files_folder]
  for files in os.listdir(target_path):
    FileName, FileExtension = os.path.splitext(str(files))
    path = target_path + '/' + str(FileName) + str(FileExtension)
    if os.path.isdir(path):
      folder += 1
    else:
      print("IS NOT A DIR")
      for types in office_files_extensions:
        if FileExtension in office_files_extensions[types]:
          print('FOUND AN OFFICE FILE')
          office += 1
      if FileExtension in image_files_extensions:
        print("FOUND AN IMAGE")
        image += 1
      if FileExtension in video_files_extensions:
        print("FOUND A VIDEO")
        video += 1
      if FileExtension not in all_formats:
        print("UNKNOWN FORMAT")
        other += 1
  lists = [video, folder, other, image, office]
  for i in range(len(lists)):
    for values in range(i + 1, len(lists)):
      if lists[i] == lists[values]:
        lists[values] = 0
  lists_copy = lists.copy()
  lists_copy.sort()
  print(lists)
  print(lists_copy)
  for i in range(len(lists)):
    if lists_copy[-1] == lists[i]:
      return destinations[i]
      print(destinations[i])

