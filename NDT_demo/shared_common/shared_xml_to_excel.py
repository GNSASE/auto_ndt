import xml.dom.minidom as minidom
import xlwt
import re


class parse_xml:
    """
    The parse_xml class is responsible for reading in the XML file and
    assigning the values to a dictionary object for iteration by the
    generate_excel class
    """
    def __init__(self, xml_file):
        self.doc = minidom.parse(xml_file)
        self.deviceElem = self.doc.getElementsByTagName('DeviceInterfaceLink')
        self.length = len(self.deviceElem)

    def iter_xml(self, section, group):
        i = -1

        if 'console' == section:
            section = 'console'
        else:
            section = ('{}+'.format(section))

        for dev in self.deviceElem:
            if(re.match(section, dev.attributes['StartPort'].value)):
                i += 1
                group.append([])
                group[i].append(dev.attributes['StartDevice'].value)
                group[i].append(dev.attributes['StartPort'].value)
                group[i].append(dev.attributes['EndDevice'].value)
                group[i].append(dev.attributes['EndPort'].value)
                group[i].append(dev.attributes['Bandwidth'].value)
                group[i].append(dev.attributes['ConnectionType'].value)
                group[i].append(dev.attributes['MediaType'].value)
                if 'Ethernet+' in section:
                    group[i].append(dev.attributes['Optics'].value)
                if 'console' in section:
                    group[i].append(dev.attributes['location'].value)
        return group


class generate_excel:
    """
    This class calls the parse_xml class and iterates through the
    return data dictionary building a new excel file  and populating
    the returned data struct.
    """
    def __init__(self):

        # init the parse_xml object
        self.xml_data = parse_xml('trialxml.xml')
        self.book = xlwt.Workbook(encoding="utf-8")

        self.variables_tab()
        self.ip_tab()
        self.incabling_tab()
        self.mgmt_tab()
        self.oobcabling_tab()
        self.vlan_tab()
        self.write_excel()

    def variables_tab(self):
        self.var_Tab = self.book.add_sheet("Variables")
        #Basic Template for Variables Tab

    def ip_tab(self):
        self.ipAssign_Tab = self.book.add_sheet("IP_Assignment")
        #Basic Template for IP_Assigment Tab

        for i in range(10):
            self.ipAssign_Tab.col(i).width = 5500

        cellformat = """borders: left thick, right thick, top thick,
                        bottom thick; pattern: pattern solid,
                        fore_color 0x1E; font: color white, bold true"""

        self.ipAssign_Tab.write(0, 0, "Device",
                                xlwt.easyxf(cellformat))
        self.ipAssign_Tab.write(0, 1, "IP_ADDR",
                                xlwt.easyxf(cellformat))
        self.ipAssign_Tab.write(0, 2, "VLAN_INTERFACE",
                                xlwt.easyxf(cellformat))
        self.ipAssign_Tab.write(0, 3, "PHYSICAL_INTERFACE",
                                xlwt.easyxf(cellformat))

    def incabling_tab(self):
        self.inCabling_Tab = self.book.add_sheet("Inband_Cabling")
        #Basic Template for Inband_Cabling Tab

        for i in range(10):
            self.inCabling_Tab.col(i).width = 5000

        cellformat = """borders: left thick, right thick, top thick,
                        bottom thick; pattern: pattern solid,
                        fore_color 0x1E; font: color white, bold true"""

        self.inCabling_Tab.write(0, 0, "localDevice",
                                 xlwt.easyxf(cellformat))
        self.inCabling_Tab.write(0, 1, "localDevciePort",
                                 xlwt.easyxf(cellformat))
        self.inCabling_Tab.write(0, 2, "Local Port-Channel",
                                 xlwt.easyxf(cellformat))
        self.inCabling_Tab.write(0, 3, "remoteDevice",
                                 xlwt.easyxf(cellformat))
        self.inCabling_Tab.write(0, 4, "remoteDevicePort",
                                 xlwt.easyxf(cellformat))
        self.inCabling_Tab.write(0, 5, "Remote Port-Channel",
                                 xlwt.easyxf(cellformat))
        self.inCabling_Tab.write(0, 6, "connectionType",
                                 xlwt.easyxf(cellformat))
        self.inCabling_Tab.write(0, 7, "media type",
                                 xlwt.easyxf(cellformat))
        self.inCabling_Tab.write(0, 8, "Optics",
                                 xlwt.easyxf(cellformat))

        #Write details from xml to excel
        deviceDet_eth = []
        deviceDet = self.xml_data.iter_xml('Ethernet', deviceDet_eth)

        i = -1
        for dev in deviceDet:
            i += 1
            self.inCabling_Tab.write(i+1, 0,
                                     deviceDet[i][0])  # Local Device
            self.inCabling_Tab.write(i+1, 1,
                                     deviceDet[i][1])  # Local Device Port
            self.inCabling_Tab.write(i+1, 3,
                                     deviceDet[i][2])  # Remote Device
            self.inCabling_Tab.write(i+1, 4,
                                     deviceDet[i][3])  # Remote Device Port
            self.inCabling_Tab.write(i+1, 6,
                                     deviceDet[i][5])  # Connection Type
            self.inCabling_Tab.write(i+1, 7,
                                     deviceDet[i][6])  # Media Type
            self.inCabling_Tab.write(i+1, 8,
                                     deviceDet[i][7])  # Optics

    def mgmt_tab(self):
        self.mgmtCabling_Tab = self.book.add_sheet("MGMT_Cabling")
        #Basic Template for MGMT_Cabling Tab
        for i in range(10):
            self.mgmtCabling_Tab.col(i).width = 5000

        cellformat = """borders: left thick, right thick, top thick,
                        bottom thick; pattern: pattern solid,
                        fore_color 0x1E; font: color white, bold true"""

        self.mgmtCabling_Tab.write(0, 0, "localDevice",
                                   xlwt.easyxf(cellformat))
        self.mgmtCabling_Tab.write(0, 1, "localDevciePort",
                                   xlwt.easyxf(cellformat))
        self.mgmtCabling_Tab.write(0, 2, "remoteDevice",
                                   xlwt.easyxf(cellformat))
        self.mgmtCabling_Tab.write(0, 3, "remoteDevicePort",
                                   xlwt.easyxf(cellformat))
        self.mgmtCabling_Tab.write(0, 4, "connectionType",
                                   xlwt.easyxf(cellformat))
        self.mgmtCabling_Tab.write(0, 5, "media",
                                   xlwt.easyxf(cellformat))
        self.mgmtCabling_Tab.write(0, 6, "Validated",
                                   xlwt.easyxf(cellformat))

        #Write details from xml to excel
        deviceDet_mgmt = []
        deviceDet = self.xml_data.iter_xml('mgmt', deviceDet_mgmt)

        i = -1
        for dev in deviceDet:
            i += 1
            self.mgmtCabling_Tab.write(i+1, 0,
                                       deviceDet[i][0])  # Local Device
            self.mgmtCabling_Tab.write(i+1, 1,
                                       deviceDet[i][1])  # Local Device Port
            self.mgmtCabling_Tab.write(i+1, 2,
                                       deviceDet[i][2])  # Remote Device
            self.mgmtCabling_Tab.write(i+1, 3,
                                       deviceDet[i][3])  # Remote Device Port
            self.mgmtCabling_Tab.write(i+1, 4,
                                       deviceDet[i][5])  # Connection Type
            self.mgmtCabling_Tab.write(i+1, 5,
                                       deviceDet[i][6])  # Media Type

    def oobcabling_tab(self):
        self.oobCabling_Tab = self.book.add_sheet("OOB_Cabling")
        #Basic Template for OOB_Cabling Tab

        for i in range(10):
            self.oobCabling_Tab.col(i).width = 5000

        cellformat = """borders: left thick, right thick, top thick,
                        bottom thick; pattern: pattern solid,
                        fore_color 0x1E; font: color white, bold true"""

        self.oobCabling_Tab.write(0, 0, "localDevice",
                                  xlwt.easyxf(cellformat))
        self.oobCabling_Tab.write(0, 1, "localDevciePort",
                                  xlwt.easyxf(cellformat))
        self.oobCabling_Tab.write(0, 2, "remoteDevice",
                                  xlwt.easyxf(cellformat))
        self.oobCabling_Tab.write(0, 3, "remoteDevicePort",
                                  xlwt.easyxf(cellformat))
        self.oobCabling_Tab.write(0, 4, "connectionType",
                                  xlwt.easyxf(cellformat))
        self.oobCabling_Tab.write(0, 5, "location",
                                  xlwt.easyxf(cellformat))
        self.oobCabling_Tab.write(0, 6, "media",
                                  xlwt.easyxf(cellformat))
        self.oobCabling_Tab.write(0, 7, "Validated",
                                  xlwt.easyxf(cellformat))

        #Write details from xml to excel
        deviceDet_oob = []
        deviceDet = self.xml_data.iter_xml('console', deviceDet_oob)
        i = -1
        for dev in deviceDet:
            i += 1
            self.oobCabling_Tab.write(i+1, 0,
                                      deviceDet[i][0])  # Local Device
            self.oobCabling_Tab.write(i+1, 1,
                                      deviceDet[i][1])  # Local Device Port
            self.oobCabling_Tab.write(i+1, 2,
                                      deviceDet[i][2])  # Remote Device
            self.oobCabling_Tab.write(i+1, 3,
                                      deviceDet[i][3])  # Remote Device Port
            self.oobCabling_Tab.write(i+1, 4,
                                      deviceDet[i][5])  # Connection Type
            self.oobCabling_Tab.write(i+1, 5,
                                      deviceDet[i][7])  # Location
            self.oobCabling_Tab.write(i+1, 6,
                                      deviceDet[i][6])  # Media Type

    def vlan_tab(self):
        self.vlan_Tab = self.book.add_sheet("VLAN")
        #Basic Template for VLAN Tab

    def write_excel(self):
        self.book.save("ndt1.xls")

generate_excel()
