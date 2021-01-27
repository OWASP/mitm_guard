from bson import json_util
import json
import ast
class create_json:
    def __init__(self,dic):
        self.ret_json = json_dic.ret_json(dic)
class JSONEncoder(json.JSONEncoder):
    def default(self, aaa):
        if hasattr(aaa, 'isoformat'): #handles both date and datetime objects
            return aaa.isoformat()
        else:
            return json.JSONEncoder.default(self, aaa)
class json_dic:
    def ret_json(dic):
        #ast.literal_eval(dic)
        json_dic = json.dumps(dic, cls=JSONEncoder)
        all_compare_result_json = json.loads(json_dic, object_hook=json_util.object_hook)
        return all_compare_result_json
