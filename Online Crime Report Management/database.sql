-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: management
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `criminal`
--

DROP TABLE IF EXISTS `criminal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `criminal` (
  `Case_id` varchar(45) NOT NULL,
  `Criminal_no` varchar(45) DEFAULT NULL,
  `Criminal_name` varchar(45) DEFAULT NULL,
  `Nick_name` varchar(45) DEFAULT NULL,
  `arrest_date` varchar(45) DEFAULT NULL,
  `dateOfcrime` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `age` varchar(45) DEFAULT NULL,
  `occupation` varchar(45) DEFAULT NULL,
  `BirthMark` varchar(45) DEFAULT NULL,
  `crimeType` varchar(45) DEFAULT NULL,
  `fatherName` varchar(45) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `wanted` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Case_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `criminal`
--

LOCK TABLES `criminal` WRITE;
/*!40000 ALTER TABLE `criminal` DISABLE KEYS */;
INSERT INTO `criminal` VALUES ('1','101','Osama','laden','02/05/2011','01/12/1998','SA','50','Terrorism','TIll','terrorist','Bin','male','yes'),('2','102','Omid','Nino','02/05/2005','01/12/2004','Iran','25','Kindanapping','Till','mail fruad','Rishan','male','yes');
/*!40000 ALTER TABLE `criminal` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-17  9:59:50
