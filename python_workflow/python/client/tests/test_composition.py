'''
Created on 22 juin 2020

@author: laurentmichel
'''
import unittest
import os
from client.translator.json_mapping_builder import JsonMappingBuilder
from client.translator.instance_from_votable import InstanceFromVotable
from client.tests import logger
from utils.dict_utils import DictUtils

class TestInstance(unittest.TestCase):


    def test_1(self):
        data_path = os.path.dirname(os.path.realpath(__file__))
        votable_path = os.path.join(data_path, "./data/test_composition.xml")
        json_ref_path = os.path.join(data_path, "./data/test_composition_1.json")
        logger.info("extract vodml block from %s", votable_path)
        instanceFromVotable = InstanceFromVotable(votable_path)
        
        instanceFromVotable._extract_vodml_block()
        instanceFromVotable._validate_vodml_block()
        
        builder = JsonMappingBuilder(json_dict=instanceFromVotable.json_block)
        builder.revert_compositions("COLLECTION")

        #print(DictUtils.get_pretty_json(builder.json["VODML"]["TEMPLATES"]))
        self.assertDictEqual(builder.json["VODML"]["TEMPLATES"], DictUtils.read_dict_from_file(json_ref_path), "=======")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()