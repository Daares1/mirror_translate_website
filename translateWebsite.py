#Script used to translate to Hindu the mirrored website www.classcentral.com

#Import function to find the links of the main HTML file of the mirrored website www.classcentral.com
from findHTML_links import findHTML_links 
from translateFile import translate_HTML_File
import os
import traceback

#Constant path of the main HTML mirrored website www.classcentral.com

absolute_path = os.path.dirname(__file__)
#Path to the main website of www.classcentral.com
RELATIVE_PATH = "website/www.classcentral.com/index.html"
website_path = os.path.join(absolute_path, RELATIVE_PATH)
print(website_path)
#Call the function findHTML_links with the WEBSITE_PATH to get a list of the HTML files to be translated
links = findHTML_links("file://"+website_path)

#Code to translate all the HTML files from English to Hindi
print("Translating "+website_path+"...")
try:
    translate_HTML_File(file=website_path)
    print("Done!!!\n")
except:
    print("Problems with the google API service.\n")
    traceback.print_exc()

#It's necessary to truncate the string path to eliminate the "file://" part.
#For every link found It's used the funtion "traslate_HTML_File()"
for link in links:
    if link == None:
        continue
    elif link[0:7] == "file://":
        try:
            print("Translating "+link[7::]+"...")
            translate_HTML_File(file=link[7::])
            print("Done!!!\n")
        except:
            print("Problems with the google API service.\n")
    else:
        print("It's not possible to translate the file in the link because is not local in the machine or it's an extern domain.\n", link,"\n")




