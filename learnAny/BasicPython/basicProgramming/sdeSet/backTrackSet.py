
class BackTrackSet:

    def checkIPvalid(self,string):
        check=False
        if(len(string)<=15):
            ip=string.split(".")
            if len(ip) in range(3,5):
                for i in ip:
                    if len(i) in range(1,4):
                        check=True
                    else:
                        check=False
                        break
        return check



    def generateIp(self,string="0"):
        print("Possible Generate IP's are : ")
        ip=""
        if((string.isdecimal() or not string) and len(string)<=15):
            if(len(string)<=4):
                for i in range(len(string),4):
                    string="0"+string
                for i  in range(len(string)):
                    ip=ip+string[i]+"."
                ip = ip[:-1]
                if self.checkIPvalid(ip):
                    print(ip)
            else:
                for i in range(len(string)):
                    repI=1+i
                    ip=string[:repI]+"."
                    for j in range(repI,len(string)):
                        repj=1+j
                        sj=string[repI:repj]+"."
                        ip=ip+sj
                        for k in range(repj, len(string)):
                            repk = 1 + k
                            sk = string[repj:repk] + "." + string[repk:]
                            ip=ip+sk
                            if (self.checkIPvalid(ip)):
                                print(ip)
                            ip=ip+sj
                        ip=string[:repI]+"."

        else:
            print("IP address should not contain alphabetics")

bc=BackTrackSet()
bc.generateIp("11211")
