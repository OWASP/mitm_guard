class get_var_name:
    def __init__(self,my_var):
        self.get_name = self.get_variable_name(my_var)
    def get_variable_name(self,my_var):
        my_var_name = [ k for k,v in locals().items() if v == my_var][0]
        return my_var_name
