CREATE DATABASE  IF NOT EXISTS `lockbox` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `lockbox`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: lockbox
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `lockers`
--

DROP TABLE IF EXISTS `lockers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lockers` (
  `lockerID` int NOT NULL AUTO_INCREMENT,
  `service_name` varchar(45) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `locker_owner_ID` int NOT NULL,
  PRIMARY KEY (`lockerID`),
  KEY `locker_owner_ID_idx` (`locker_owner_ID`),
  CONSTRAINT `locker_owner_ID` FOREIGN KEY (`locker_owner_ID`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lockers`
--

LOCK TABLES `lockers` WRITE;
/*!40000 ALTER TABLE `lockers` DISABLE KEYS */;
INSERT INTO `lockers` VALUES (13,'Google','giovadesio26@gmail.com','dbuSdb627SVwj1!@$%#sb2',1),(14,'Google','giovadesio26@gmail.com','dbuSdb627SVwj1!@$%#sb2',1),(15,'Google','giovadesio26@gmail.com','dbuSdb627SVwj1!@$%#sb2',1),(16,'Google','giovadesio26@gmail.com','dbuSdb627SVwj1!@$%#sb2',1),(17,'Google','giovadesio26@gmail.com','dbuSdb627SVwj1!@$%#sb2',1),(18,'Google','giovadesio26@gmail.com','dbuSdb627SVwj1!@$%#sb2',1),(19,'Google','giovadesio26@gmail.com','dbuSdb627SVwj1!@$%#sb2',1),(20,'','','',1),(21,'','','',1),(22,'','','',1),(23,'','','',1),(24,'','','',1),(25,'','','',1),(26,'','','',1),(27,'Amazon','amuchinas','pass',1),(28,'s','s','s',1),(29,'','','',1),(30,'a','a','ss',1),(31,'d','d','dd',1),(32,'s','s','s',1),(33,'','','',1),(34,'s','s','f',1),(35,'','','',1),(36,'','','',1),(37,'','','',1);
/*!40000 ALTER TABLE `lockers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-01 18:20:36
