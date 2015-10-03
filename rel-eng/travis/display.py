from copr.client import CoprClient
import sys
import time
import urllib2

found_project = False
cl = CoprClient(username="xvican01", login=sys.argv[1], token=sys.argv[2],
                copr_url="http://copr.fedoraproject.org")
result = cl.get_projects_list("xvican01").projects_list
for project in result:
    if project.projectname == "rpg":
        found_project = True
        break
if not found_project:
    chroot = ["fedora-21-x86_64", "fedora-21-i386", "fedora-22-x86_64",
              "fedora-22-i386", "fedora-rawhide-i386", "fedora-rawhide-x86_64"]
    cl.create_project("rpg", chroots=chroot)
srpm_name = sys.argv[3]
result = cl.get_build_details(123657,"rpg");
bw=result
#type(bw.handle.get_build_details().data["chroots"])
from operator import itemgetter
novy=sorted(bw.handle.get_build_details().data["chroots"].items(), key=itemgetter(0))
i=1
for ch, status in novy:
    print("echo -en \"travis_fold:start:rpg-{}\\\\r\"".format(ch))
    if (status == "succeeded"):
        print("echo \"{}  $(tput setaf 2)succeeded $(tput sgr0)\"".format(ch))
    else:
        print("echo \"{}  $(tput setaf 1){} $(tput sgr0)\"".format(ch,status))
    logfile = urllib2.urlopen("https://copr-be.cloud.fedoraproject.org/results/xvican01/rpg/"+ch+"/00123657-rpg/build.log.gz")
    output = open("build"+str(i)+".log.gz",'wb')
    output.write(logfile.read())
    output.close()
    print("zcat "+"build"+str(i)+".log.gz")
    i += 1  
    print("echo -en \"travis_fold:end:rpg-{}\\\\r\"".format(ch))
