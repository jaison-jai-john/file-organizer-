office_files_extensions = {
  'word': ['.doc', '.docm', '.docx', '.dot', '.dotm', '.dotx', '.odt', '.pdf', '.rtf', '.wps', '.xml', '.xps'],
  'excel': ['.csv', '.dbf', '.dif', '.ods', '.prn', '.slk', '.xla', '.xlam', 'xls', '.xlsb', '.xlsm', '.xlsx', '.xlt', '.xltm', '.xltx', '.xlw', '.xml', '.xps'],
  'powerpoint': ['.pot', '.potm', '.potx', '.ppa', '.ppam', '.pps', '.ppsm', '.ppsx', '.ppt', '.pptm', '.pptx', '.thmx'],
}
for types in office_files_extensions:
  for formats in range(len(office_files_extensions[types])):
    office_files_extensions[types][formats] = office_files_extensions[types][formats].lower()



image_files_extensions = ['.PSD', '.XCF', '.AI', '.CDR', '.tif', '.tiff', '.bmp', '.jpg', '.jpeg', '.gif', '.png', '.eps', '.raw', '.cr2', '.nef', '.orf', '.sr2', '.WEBP', '.heif', '.heic', '.ind', '.indd', '.indt', '.SVG', '.EPS', '.jpe', '.jif', '.jfif', '.jfi', '.gif', '.dib', '.jp2', '.j2k', '.jpf', '.jpx', '.jpm', '.mj2', '.svgz', '.afphoto',]
for formats in range(len(image_files_extensions)):
  image_files_extensions[formats] = image_files_extensions[formats].lower()


video_files_extensions = ['.WEBM', '.MPG', '.MP2', '.MPEG', '.MPE', '.MPV', '.OGG', '.MP4', '.mp4', '.M4P', '.M4V', '.AVI', '.WMV', '.MOV', '.QT', '.FLV', '.SWF', '.AVCHD', '.mkv', '.MKV', '.Mkv',]
for formats in range(len(video_files_extensions)):
  video_files_extensions[formats] = video_files_extensions[formats].lower()


all_formats = ['.doc', '.docm', '.docx', '.dot', '.dotm', '.dotx', '.odt', '.pdf', '.rtf', '.wps', '.xml', '.xps', '.csv', '.dbf', '.dif', '.ods', '.prn', '.slk', '.xla', '.xlam', 'xls', '.xlsb', '.xlsm', '.xlsx', '.xlt', '.xltm', '.xltx', '.xlw', '.xml', '.xps', '.pot', '.potm', '.potx', '.ppa', '.ppam', '.pps', '.ppsm', '.ppsx', '.ppt', '.pptm', '.pptx', '.thmx', '.PSD', '.XCF', '.AI', '.CDR', '.tif', '.tiff', '.bmp', '.jpg', '.jpeg', '.gif', '.png', '.eps', '.raw', '.cr2', '.nef', '.orf', '.sr2', '.WEBP', '.heif', '.heic', '.ind', '.indd', '.indt', '.SVG', '.EPS', '.jpe', '.jif', '.jfif', '.jfi', '.gif', '.dib', '.jp2', '.j2k', '.jpf', '.jpx', '.jpm', '.mj2', '.svgz', '.afphoto', '.WEBM', '.MPG', '.MP2', '.MPEG', '.MPE', '.MPV', '.OGG', '.MP4', '.M4P', '.M4V', '.AVI', '.WMV', '.MOV', '.QT', '.FLV', '.SWF', '.AVCHD', '.mkv', '.MKV', '.Mkv',]
for formats in range(len(all_formats)):
  all_formats[formats] = all_formats[formats].lower()
