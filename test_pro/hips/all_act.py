

class all_actions():
    def proc_terminal(self,proc_number):
        self.p = psutil.Process(proc_number)
        return self.p.terminal()
    def proc_terminate(self,proc_number):#os.kill(pid, signal.SIGTERM)
        self.p = psutil.Process(proc_number)
        return self.p.terminate()
    def proc_kill(self,proc_number):#os.kill(pid, signal.SIGKILL)
        self.p = psutil.Process(proc_number)
        return self.p.kill()
    def proc_children_term(self,proc_number):
        self.pro = psutil.Process(proc_number)
        aaa = self.pro.children()
        for pp in aaa:
            pp.terminate()
        gone, alive = psutil.wait_procs(aaa, timeout=3)
        for pr in alive:
            pr.kill()
    def proc_parent_term(self,proc_number):
        self.pro = psutil.Process(proc_number)
        self.pro.terminate()
        self.pro.kill()
