from copr.client import CoprClient
from operator import itemgetter
import sys
import time
import urllib2

def build_project(project_name,copr_client):
    found_project = False
    result = copr_client.get_projects_list("xvican01").projects_list
    for project in result:
        if project.projectname == project_name:
            found_project = True
            break
    if not found_project:
        chroot = ["fedora-21-x86_64", "fedora-21-i386", "fedora-22-x86_64",
                  "fedora-22-i386", "fedora-rawhide-i386", "fedora-rawhide-x86_64"]
        copr_client.create_project(project_name, chroots=chroot)  
    result=copr_client.create_new_build(project_name, pkgs=[sys.argv[3]])
    return result

def main():
    cl = CoprClient(username="xvican01", login=sys.argv[1], token=sys.argv[2],
                    copr_url="http://copr.fedoraproject.org")
    results=build_project(sys.argv[4],cl)
    for bw in results.builds_list: 
        build_id = bw.build_id 
        while True: 
            count_chroot = 6
            for ch, status in bw.handle.get_build_details().data["chroots"].items(): 
                if status in ["skipped", "failed", "succeeded"]: 
                    count_chroot -= 1 
            time.sleep(10) 
            if count_chroot == 0: 
                break
        sort_result=sorted(bw.handle.get_build_details().data["chroots"].items(), key=itemgetter(0))
        i=1
        exit_code=0
        for ch, status in sort_result:
            print("echo -en \"travis_fold:start:rpg-{}\\\\r\"".format(ch))
            if (status == "succeeded"):
                print("echo \"{}  $(tput setaf 2)succeeded $(tput sgr0)\"".format(ch))
            else:
                print("echo \"{}  $(tput setaf 1){} $(tput sgr0)\"".format(ch,status))
                exit_code += 1
            url="https://copr-be.cloud.fedoraproject.org/results/xvican01/"+sys.argv[4]+"/"+ch+"/"+'0'*(8-len(str(build_id)))+str(build_id)+"-rpg/build.log.gz"
            logfile = urllib2.urlopen(url)
            output = open("/home/travis/build"+str(i)+".log.gz",'wb')
            output.write(logfile.read())
            output.close()
            print("zcat "+"build"+str(i)+".log.gz")
            i += 1  
            print("echo -en \"travis_fold:end:rpg-{}\\\\r\"".format(ch))
        print("exit {}".format(exit_code))

if __name__ == '__main__':
    main()