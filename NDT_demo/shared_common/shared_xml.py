#!python
import xml.etree.ElementTree as ET

def xml_read_variables(schema_section, filename):
    """
    This function will read the provided xml template file and return the variables
    required to build the user web form.
    """
    tree = ET.ElementTree(file=filename)
    root = tree.getroot()

    # Read through the tree and return Variables child section if it exists.
    for child in root:
        if child.tag == schema_section:
            return child

