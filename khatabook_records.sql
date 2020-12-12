-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: khatabook_records
-- ------------------------------------------------------
-- Server version	8.0.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bad_debts`
--

DROP TABLE IF EXISTS `bad_debts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bad_debts` (
  `name` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phone` varchar(200) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  `date` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bad_debts`
--

LOCK TABLES `bad_debts` WRITE;
/*!40000 ALTER TABLE `bad_debts` DISABLE KEYS */;
/*!40000 ALTER TABLE `bad_debts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `records`
--

DROP TABLE IF EXISTS `records`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `records` (
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `phone` varchar(200) NOT NULL,
  `amount` int(11) NOT NULL,
  `date` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `records`
--

LOCK TABLES `records` WRITE;
/*!40000 ALTER TABLE `records` DISABLE KEYS */;
INSERT INTO `records` VALUES ('louish hofmann','germany','12233',12000,'2021-01-20'),('agnes nielsn','winden','2332436',6700,'2021-10-08'),('ulrich nielsen','winden','34323',12000,'2020-06-20'),('egon ','germany ','3758347893',8900,'2021-09-08'),('elizabeth doppler','winden','456789',7800,'2021-11-25'),('maja shone','germany','73394',9000,'2021-08-05'),('paullux','germany','78231',8900,'2021-04-22'),('jordies triebel','germany','78234409',8900,'2021-07-15'),('gina sitabitz','germany','78342',8900,'2021-03-11'),('oliver massuci','germany','7853584',9000,'2021-06-16'),('jonas khanwald ','winden','78548',10000,'2020-01-01'),('egon tiedemenn','winden','7883948',5600,'2020-09-10'),('silja khanwald','winden','8348',16700,'2020-10-14'),('franziska doppler','winden','8388',9200,'2020-03-05'),('lisa vicari ','munich','84277',8900,'2021-12-28'),('martha nielsen','winden','88388',5600,'2020-12-11'),('hannah khanwald','winden','890349',12300,'2021-08-13'),('bartorz tiedemenn','winden','89232657',6700,'2020-04-16'),('mikkel nielsen','winden','893457',5600,'2020-05-14'),('magnus nielsen','winden','8939',12000,'2020-02-06'),('kathrina nielsen','winden','899343',7800,'2020-07-09'),('micheal khanwald','winden','899344432',8970,'2021-05-06'),('helge doppler','winden','89989',14500,'2020-11-12'),('morith jahn','germany','9385',9000,'2021-02-11');
/*!40000 ALTER TABLE `records` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-11 22:15:01
