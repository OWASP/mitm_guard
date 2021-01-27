class write_line:
    def __init__(self,line,str):
        setting = open('~/.run_agent/.setting', 'r')
        ary= setting.readlines()
        ary[line-1] = str
        setting = open('~/.run_agent/.setting', 'w')
        for count in range(len(ary)):
            setting.write(ary[count])
