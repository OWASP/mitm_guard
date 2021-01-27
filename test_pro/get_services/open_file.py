class open_file:
    def __init__(self,location,file):
        self.get_cont = self.get_content(location,file)
    def get_content(self,location,file):
        f_r = open(location+file_name, 'r')
        content = f_r.readline()
        f_r.close()
