import psutil
import datetime
import signal
class all_ps:
    def __init__(self,proc_number):
        self.p_name = self.proc_name(proc_number)
    def proc_name(self,proc_number):
        p = psutil.Process(proc_number)
        return p.name()
    def proc_username(self,proc_number):
        p = psutil.Process(proc_number)
        return p.username()
    def proc_exe(self,proc_number):
        p = psutil.Process(proc_number)
        return p.exe()
    def proc_cmdline(self,proc_number):
        p = psutil.Process(proc_number)
        return p.cmdline()
    def proc_create_time(self,proc_number):
        p = psutil.Process(proc_number)
        p_time = datetime.datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S")
        return p_time
    def proc_cwd(self,proc_number):
        p = psutil.Process(proc_number)
        return p.cwd()
    def proc_children(self,proc_number):
        p = psutil.Process(proc_number)
        return p.children(recursive=True)
    def proc_status(self,proc_number):
        p = psutil.Process(proc_number)
        return p.status()

    def proc_environ(self,proc_number):
        p = psutil.Process(proc_number)
        return p.environ()
    def proc_as_dict(self,proc_number):
        p = psutil.Process(proc_number)
        return p.as_dict(attrs=['pid', 'name', 'username'])
    def proc_ppid(self,proc_number):
        p = psutil.Process(proc_number)
        return p.ppid()
    def proc_parent(self,proc_number):
        p = psutil.Process(proc_number)
        return p.parent()
    def proc_uids(self,proc_number):
        p = psutil.Process(proc_number)
        return p.uids()

    def proc_nice(self,proc_number):
        p = psutil.Process(proc_number)
        p.nice(10) # set
        return p.nice() # get
    def proc_memory_info(self,proc_number):
        p = psutil.Process(proc_number)
        return p.memory_info()
    def proc_connections(self,proc_number):
        p = psutil.Process(proc_number)
        return p.connections()
    def proc_suspend(self,proc_number):#os.kill(pid, signal.SIGSTOP)
        p = psutil.Process(proc_number)
        return p.suspend()#
    def proc_resume(self,proc_number):#os.kill(pid, signal.SIGCONT)
        p = psutil.Process(proc_number)
        return p.resume()

    def Process_name(self,name):
        ls = []
        for p in psutil.process_iter(attrs=['name']):
            if p.info['name'] == name:
                ls.append(p)
        return ls

    #kill process tree
    def kill_proc_tree(self,proc_number, sig=signal.SIGTERM, include_parent=True,timeout=None, on_terminate=None):
        """Kill a process tree (including grandchildren) with signal
        "sig" and return a (gone, still_alive) tuple.
        "on_terminate", if specified, is a callabck function which is
        called as soon as a child terminates.
        """
        if proc_number == os.getpid():
            raise RuntimeError("I refuse to kill myself")
        parent = psutil.Process(proc_number)
        children = parent.children(recursive=True)
        if include_parent:
            children.append(parent)
        for p in children:
            p.send_signal(sig)
        gone, alive = psutil.wait_procs(children, timeout=timeout)
        return (gone, alive)

    #Terminate my children
    #This may be useful in unit tests whenever sub-processes are started.
    #This will help ensure that no extra children (zombies) stick around to hog resources.
    def reap_children(self,proc_number,timeout=3):
        "Tries hard to terminate and ultimately kill all the children of this process."
        procs = psutil.Process(proc_number).children()
        # send SIGTERM
        for p in procs:
            p.terminate()
        gone, alive = psutil.wait_procs(procs, timeout=timeout)
        if alive:
            # send SIGKILL
            for p in alive:
                print("process {} survived SIGTERM; trying SIGKILL" % p)
                p.kill()
            gone, alive = psutil.wait_procs(alive, timeout=timeout)
            if alive:
                # give up
                for p in alive:
                    print("process {} survived SIGKILL; giving up" % p)

    #Processes consuming more than 500M of memory
