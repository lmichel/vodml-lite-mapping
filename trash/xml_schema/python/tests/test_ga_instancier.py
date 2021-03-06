'''
Created on 31 mars 2020

@author: laurentmichel
'''

import os, json
from utils.json_encoder import MyEncoder
from launcher.instance_builder_runner import InstanceBuilderRunner
from inst_builder.astropy_wrapper import AstropyWrapper

if __name__ == '__main__':
    base_path = os.path.dirname(os.path.realpath(__file__)) 
    votable_path = os.path.join(base_path, 
                                "../../mapping_sample",
                                "sample_ga.vot"
                                )
    json_inst_path = votable_path.replace('.vot',
                                          '.inst.json'
                                          )
    instance_builder_runner = InstanceBuilderRunner(
        votable_path,
        json_inst_path)
    instance_builder_runner.run()
    
    instance = instance_builder_runner.instance
    while True:
        inst = instance._get_next_row_instance()
        if inst != None:
            print(json.dumps(inst, 
                             indent=2,
                             sort_keys=True,
                             cls=MyEncoder))
        else:
            break
    
    types_test = ["coords:SpaceFrame"]
    for dmtype in types_test:
        print("element matching dmtype={}".format(dmtype))
        searched_types = instance.search_instance_by_type(dmtype)
        for ele in searched_types:
            print("==============")
            print(json.dumps(ele, 
                         indent=2,
                         sort_keys=True,
                         cls=MyEncoder))
            print("==============")

            astropy_wrapper = AstropyWrapper(instance)
            print(astropy_wrapper.get_space_frame(ele))
                
                                        
                                                        
            

    
