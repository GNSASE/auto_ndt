-- Run this first to create the ndt_webuser account

'GRANT ALL PRIVILEGES ON *.* TO \'ndt_webuser\'@\'%\' IDENTIFIED BY PASSWORD \'*575BDED6ABD25D242F1C80F7C176D49708CC0AF2\' WITH GRANT OPTION'

CREATE DATABASE  IF NOT EXISTS `ndt_tool` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `ndt_tool`;
-- MySQL dump 10.13  Distrib 5.6.13, for Win32 (x86)
--
-- Host: localhost    Database: ndt_tool
-- ------------------------------------------------------
-- Server version   5.6.14

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ndt_form_data`
--

DROP TABLE IF EXISTS `ndt_form_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ndt_form_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pid` text,
  `scale_unit` text,
  `data_key` text,
  `data_value` text,
  `datetime` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_values` (`pid`(100),`data_key`(100))
) ENGINE=MyISAM AUTO_INCREMENT=1537 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ndt_form_data`
--

LOCK TABLES `ndt_form_data` WRITE;
/*!40000 ALTER TABLE `ndt_form_data` DISABLE KEYS */;
INSERT INTO `ndt_form_data` VALUES (1522,'123456','EVO_Cagg','XE_TOR_SKU','Nexus 3048','2013-12-02 14:56:03'),(1535,'123456','EVO_Cagg','DC','CO1','2013-12-02 14:56:03'),(1532,'123456','EVO_Cagg','BE_TOR_SKU','Nexus 3048','2013-12-02 14:56:03'),(1528,'123456','EVO_Cagg','AGG_INSTANCE_NUM','2','2013-12-02 14:56:03'),(1527,'123456','EVO_Cagg','LB_PREF','something-yyy','2013-12-02 14:56:03'),(1529,'123456','EVO_Cagg','LB_SKU','F5 Bigip 8950','2013-12-02 14:56:03'),(1519,'123456','EVO_Cagg','L3AGG_SKU','Nexus 3064X','2013-12-02 14:56:03'),(1516,'123456','EVO_Cagg','L3AGG_PREF','something-xxx','2013-12-02 14:56:03'),(1530,'123456','EVO_Cagg','STAMP','something','2013-12-02 14:56:03'),(1517,'123456','EVO_Cagg','PROPERTY','hot','2013-12-02 14:56:03'),(1521,'123456','EVO_Cagg','DCFX_PORT_2','','2013-12-02 14:56:03'),(1534,'123456','EVO_Cagg','OOB_SW_PORT','','2013-12-02 14:56:03'),(1523,'123456','EVO_Cagg','DCFX_PREF','','2013-12-02 14:56:03'),(1515,'123456','EVO_Cagg','OOB_SW','','2013-12-02 14:56:03'),(1526,'123456','EVO_Cagg','TEST_IP','10.10.10.0/24','2013-12-02 14:56:03'),(1524,'123456','EVO_Cagg','MGMT_SW','','2013-12-02 14:56:03'),(1518,'123456','EVO_Cagg','DCFX_PORT_1','','2013-12-02 14:56:03'),(1520,'123456','EVO_Cagg','MGMT_SW_PORT','132','2013-12-02 14:56:03'),(1525,'123456','EVO_Cagg','TEST_OOB_CABLING','123','2013-12-02 14:56:03'),(1531,'123456','EVO_Cagg','TEST_MGMT_CABLING','test','2013-12-02 14:56:03'),(1533,'123456','EVO_Cagg','TEST_PORT_PLAN','','2013-12-02 14:56:03'),(1536,'123456','EVO_Cagg','TEST_INBAND_CABLING','test','2013-12-02 14:56:03'),(1505,'1234','EVO_Cagg','LB_PREF','something-zzz','2013-11-27 14:44:32'),(1506,'1234','EVO_Cagg','XE_TOR_SKU','Nexus 3048','2013-11-27 14:44:32'),(1507,'1234','EVO_Cagg','L3AGG_PREF','something-xxx','2013-11-27 14:44:32'),(1508,'1234','EVO_Cagg','AGG_INSTANCE_NUM','2','2013-11-27 14:44:32'),(1509,'1234','EVO_Cagg','DC','CO1','2013-11-27 14:44:32'),(1510,'1234','EVO_Cagg','PROPERTY','hot','2013-11-27 14:44:32'),(1511,'1234','EVO_Cagg','L3AGG_SKU','Nexus 3064X','2013-11-27 14:44:32'),(1512,'1234','EVO_Cagg','LB_SKU','F5 Bigip 8950','2013-11-27 14:44:32'),(1513,'1234','EVO_Cagg','STAMP','something','2013-11-27 14:44:32'),(1514,'1234','EVO_Cagg','BE_TOR_SKU','Nexus 3048','2013-11-27 14:44:32');
/*!40000 ALTER TABLE `ndt_form_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-12-03  9:22:12

CREATE DATABASE  IF NOT EXISTS `ndt_tool` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `ndt_tool`;
-- MySQL dump 10.13  Distrib 5.6.13, for Win32 (x86)
--
-- Host: localhost    Database: ndt_tool
-- ------------------------------------------------------
-- Server version   5.6.14

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ndt_index`
--

DROP TABLE IF EXISTS `ndt_index`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ndt_index` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pid` text COMMENT 'Current project ID number for the network deployment.',
  `scale_unit` text COMMENT 'Sisyphus required scale unit identifier.',
  `datetime` datetime DEFAULT CURRENT_TIMESTAMP COMMENT 'Datetime stamp of entry creation.',
  PRIMARY KEY (`id`),
  UNIQUE KEY `pid` (`pid`(20)),
  UNIQUE KEY `pid_2` (`pid`(20))
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=utf8 COMMENT='This table contains the PID number,network type for all existing ndt submitted.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ndt_index`
--

LOCK TABLES `ndt_index` WRITE;
/*!40000 ALTER TABLE `ndt_index` DISABLE KEYS */;
INSERT INTO `ndt_index` VALUES (24,'123456','EVO_Cagg','2013-11-27 10:45:26'),(26,'1234','EVO_Cagg','2013-11-27 14:44:32');
/*!40000 ALTER TABLE `ndt_index` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-12-03  9:22:12

CREATE DATABASE  IF NOT EXISTS `ndt_tool` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `ndt_tool`;
-- MySQL dump 10.13  Distrib 5.6.13, for Win32 (x86)
--
-- Host: localhost    Database: ndt_tool
-- ------------------------------------------------------
-- Server version   5.6.14

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `scale_unit_index`
--

DROP TABLE IF EXISTS `scale_unit_index`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scale_unit_index` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `scale_unit` text,
  `xml_template_filename` text,
  `network_standard_url` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `scale_unit_UNIQUE` (`scale_unit`(40))
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='Mapping of scale unit to xml files to load.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scale_unit_index`
--

LOCK TABLES `scale_unit_index` WRITE;
/*!40000 ALTER TABLE `scale_unit_index` DISABLE KEYS */;
INSERT INTO `scale_unit_index` VALUES (1,'EVO_Cagg','template_evo_cagg.xml','http://sharepoint/sites/gnseng/Design%20Standards/Forms/AllItems.aspx?RootFolder=%2Fsites%2Fgnseng%2FDesign%20Standards%2FShared%2Fdcfx');
/*!40000 ALTER TABLE `scale_unit_index` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-12-03  9:22:12

