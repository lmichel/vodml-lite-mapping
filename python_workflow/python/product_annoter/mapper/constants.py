'''
Created on 15 avr. 2020

@author: laurentmichel
'''
from collections import namedtuple


ParamTemplates = namedtuple('ParamTemplates', ['POSITION'])
PARAM_TEMPLATES = ParamTemplates(
    """
    <INSTANCE dmrole="mango:Source.parameters" dmtype="mango:Parameter">
    <VALUE dmrole="mango:Parameter.semantic" dmtype="ivoa:string" value="@@@@@@"/>
    <VALUE dmrole="mango:Parameter.ucd" dmtype="ivoa:string" value="@@@@@@"/>
    <VALUE dmrole="mango:Parameter.description" dmtype="ivoa:string" value="@@@@@@"/>
    </INSTANCE>
    """
    )

AttributeDefault = namedtuple('AttributeDefault', ['TO_BE_SET', 'NOT_SET'])
ATTRIBUTE_DEFAULT = AttributeDefault(
    "@@@@@@",
    "NotSet"
    )
