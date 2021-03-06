#!/usr/bin/python3
# -*- coding: utf-8 -*-
from transform import  *
            
def main():
    mapping_generator = MappingGenerator()
    mapping_generator.parse_vodml_file(filename="../../models/TimeDomainML.vo-dml.xml", model='TimeDomainML')

    mapping_generator.resolve_inheritance();
    mapping_generator.resolve_constaints();
    #root_object_id = 'cube:DataProduct'
    mapping_generator.root_object_id ='timedomain.Characterisation'
    # role > type
    mapping_generator.concrete_classe = {}
#    mapping_generator.concrete_classes = {"cube:DataProduct.coordSys": "coords:AstroCoordSystem",
#                        "cube:DataProduct.coordSys": ["coords:domain.space.SpaceFrame"
#                                                             , "coords:domain.time.TimeFrame"
#                                                             , "coords:GenericCoordFrame"], 
#                        "trans:FrameTransform.operation": "trans:TProjection",
#                        "trans:FrameTransform.nativeFrame": "coords:domain.time.TimeFrame",
#                        "trans:FrameTransform.targetFrame": "coords:domain.space.SpaceFrame",
#                        "cube:MeasurementAxis.measure": "meas:StdTimeMeasure",
#                        "cube:NDPoint.observable": ["cube:Observable", "cube:Observable", "cube:Observable"],
#                        "cube:DataProduct.dataset": "ds:experiment.ObsDataset"
#                        #"cube:NDPoint.observable": ["meas:TimeMeasure"
#                        #                            , "meas:GenericCoordMeasure"
#                        #                            ],
#                        }
    
    mapping_generator.concrete_types = {}
#    mapping_generator.concrete_types = {"coords:domain.space.SpaceFrame.refPosition": "coords:domain.space.StdRefLocation",
#                      "coords:domain.time.TimeFrame.refPosition": "coords:domain.space.StdRefLocation",
#                      "coords:domain.time.TimeFrame.refDirection": "coords:domain.space.StdRefLocation",
#                      "coords:domain.time.TimeFrame.time0": "coords:domain.time.MJD",
#                      "meas:CoordMeasure.coord": "coords:domain.time.JD",
#                      "meas:Error1D.statError": "meas:Symmetrical1D",
#                      "meas:Error1D.sysError": "meas:Symmetrical1D",
#                      "meas:Error1D.ranError": "meas:Symmetrical1D"
                      #"meas:Error2D.statError": "meas:Symmetrical2D",
                      #meas:Error2D.sysError": "meas:Symmetrical2D",
                      #"meas:Error2D.ranError": "meas:SymmetricalZD"
#                        }
    #mapping_generator.concrete_classes = {}
    #mapping_generator.concrete_types={}
    mapping_generator.generate_mapping()
    
    for ac in mapping_generator.mapped_abstract_classes :
        print("Abstract class mapped " + ac)
        for sc in mapping_generator.get_sub_classes(ac):
            abstract = ""
            if  mapping_generator.object_types[sc].abstract == True:
                abstract = "Abstract "
            print("   " + abstract + sc)
            if abstract != "":
                for sc2 in mapping_generator.get_sub_classes(sc):
                    print("       " + sc2)
               
    for ac in mapping_generator.mapped_abstract_types :
        print("Abstract type mapped " + ac)
        for sc in mapping_generator.get_sub_types(ac):
            print("   " + sc)
    #parse_vodml_file(filename="/home/michel/workspace/vo-datamodels/provenance/vo-dml/xml/ProvenanceDM.vo-dml.xml", model='provenance')
    #root_object_id = 'provenance:provenance.Entity'
    #print(root_object_id)
    #generate_mapping()

    root = etree.fromstring(mapping_generator.xml_string + "\n")
    print((etree.tostring(root, pretty_print=True)).decode("utf-8") )
if __name__ == "__main__":
    main()   
    sys.exit()   
        
    
