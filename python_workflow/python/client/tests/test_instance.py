'''
Created on 22 juin 2020

@author: laurentmichel
'''
import unittest
import os
from client.inst_builder.json_mapping_builder import JsonMappingBuilder
from client.launchers.instance_from_votable import InstanceFromVotable
from tests import logger
from utils.dict_utils import DictUtils

class TestInstance(unittest.TestCase):


    def test_1(self):
        votable_path = os.path.dirname(os.path.realpath(__file__))
        votable_path = os.path.join(votable_path, "./data/test_instance.xml")
        json_ref_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./data/test_instance_1.json")
        logger.info("extract vodml block from %s", votable_path)
        instanceFromVotable = InstanceFromVotable(votable_path)
        
        instanceFromVotable._extract_vodml_block()
        instanceFromVotable._validate_vodml_block()
        
        builder = JsonMappingBuilder(json_dict=instanceFromVotable.json_block)
        builder.revert_elements("INSTANCE")
        builder.revert_elements("VALUE")
        #print(DictUtils.get_pretty_json(builder.json["VODML"]["TEMPLATES"]))
        self.assertDictEqual(builder.json["VODML"]["TEMPLATES"], DictUtils.read_dict_from_file(json_ref_path), "=======")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()