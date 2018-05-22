'''
Created on May 21, 2018

@author: jstrick
'''
import spam
import xml
import xml.etree.ElementTree as ET

e = ET.Element('thing')

from spam import ham
from spam import *

spam.ham()
ham()