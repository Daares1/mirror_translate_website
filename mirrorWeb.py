#Scrip to mirror the website www.classcentral.com using wget command
import os
WEBSITE = "www.classcentral.com"

os.system("echo Website {}".format(WEBSITE)+" is going to be mirrored")
#Wget 
os.system("wget -U \'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36\' --recursive --level=1 --no-clobber --page-requisites --adjust-extension --span-host --retry-on-http-error=429 --waitretry=20 --tries=4 --convert-links --no-parent --restrict-file-names=windows --timestamping --timeout=60 --directory-prefix=\"website\" \"https://www.classcentral.com\" ")