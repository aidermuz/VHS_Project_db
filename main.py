-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: vhs_project_db
-- ------------------------------------------------------
-- Server version	8.0.27

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
-- Table structure for table `account`
--

DROP TABLE IF EXISTS `account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account` (
  `idaccount` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `Guest_idGuest` int NOT NULL,
  PRIMARY KEY (`idaccount`),
  KEY `fk_account_Guest1_idx` (`Guest_idGuest`),
  CONSTRAINT `fk_account_Guest1` FOREIGN KEY (`Guest_idGuest`) REFERENCES `guest` (`idGuest`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account`
--

LOCK TABLES `account` WRITE;
/*!40000 ALTER TABLE `account` DISABLE KEYS */;
INSERT INTO `account` VALUES (1,'admin','admin',1),(2,'aider@gmail.com','1234567890',2);
/*!40000 ALTER TABLE `account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genre`
--

DROP TABLE IF EXISTS `genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genre` (
  `idGenre` int NOT NULL AUTO_INCREMENT,
  `description` varchar(500) DEFAULT NULL,
  `price` varchar(45) DEFAULT NULL,
  `img` varchar(500) DEFAULT NULL,
  `genre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idGenre`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genre`
--

LOCK TABLES `genre` WRITE;
/*!40000 ALTER TABLE `genre` DISABLE KEYS */;
INSERT INTO `genre` VALUES (1,'«Оно́» — американский сверхъестественный фильм ужасов режиссёра Энди Мускетти, вышедший на экраны в 2017 году.','600','https://upload.wikimedia.org/wikipedia/ru/f/ff/%D0%9E%D0%BD%D0%BE_%28%D0%BF%D0%BE%D1%81%D1%82%D0%B5%D1%80_%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%D0%B0%2C_2017%29.jpg','horror'),(2,'«Зелёная ми́ля» — фэнтезийная драма по одноимённому роману Стивена Кинга.','600','https://upload.wikimedia.org/wikipedia/ru/thumb/b/b0/Green_mile_film.jpg/211px-Green_mile_film.jpg','drama'),(3,'«Троя» — историко-приключенческая драма 2004 года режиссёра Вольфганга Петерсена по сценарию Дэвида Бениоффа.','750','https://upload.wikimedia.org/wikipedia/ru/thumb/0/07/Troy-poster.jpg/214px-Troy-poster.jpg','historical'),(4,'Космическая одиссея 2001 года» — культовый научно-фантастический фильм Стэнли Кубрика 1968 года, ставший вехой в развитии кинофантастики и мирового кинематографа в целом.','800','https://upload.wikimedia.org/wikipedia/ru/3/38/2001_A_Space_Odyssey.jpg?20111212101944','science'),(5,'«Молча́ние ягня́т» — американский психологический фильм ужасов 1991 года режиссёра Джонатана Демми, снятый по мотивам одноимённого романа Томаса Харриса о серийном убийце Ганнибале Лектере.','450','https://upload.wikimedia.org/wikipedia/ru/thumb/9/95/The_Silence_Of_The_Lambs.jpg/203px-The_Silence_Of_The_Lambs.jpg','thriller'),(6,'«Джанго освобождённый» — художественный фильм 2012 года режиссёра Квентина Тарантино в жанре спагетти-вестерн','700','https://upload.wikimedia.org/wikipedia/ru/thumb/b/ba/Django_Unchained.jpg/200px-Django_Unchained.jpg','western'),(7,'«Друзья́» — американский ситком, повествующий о жизни шестерых друзей. Признан одним из лучших комедийных сериалов в истории американского телевидения и стал одним из наиболее знаменитых проектов 1990-х годов','550','https://avatars.mds.yandex.net/get-kinopoisk-image/1900788/35c6cb89-75e3-4efa-8d00-5bbf7175c066/300x450','comedy'),(8,'qdqdas','678','https://mirpozitiva.ru/wp-content/uploads/2019/11/1472042719_15.jpg','horror'),(9,'adadasdasdadada','asdadasdasdas','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmWTnm3HPjxvo4rrDLtuotzql49rXqGNu3Ggo4EngBAA&s','horrasdad');
/*!40000 ALTER TABLE `genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `guest`
--

DROP TABLE IF EXISTS `guest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `guest` (
  `idGuest` int NOT NULL AUTO_INCREMENT,
  `fname` varchar(45) DEFAULT NULL,
  `lname` varchar(45) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `checkIn` varchar(45) DEFAULT NULL,
  `checkOut` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idGuest`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guest`
--

LOCK TABLES `guest` WRITE;
/*!40000 ALTER TABLE `guest` DISABLE KEYS */;
INSERT INTO `guest` VALUES (1,'Marlen','Osmanov','+79789999999','marlen@gmail.com',NULL,NULL),(2,'Enver','Chaush','+79783333333','chaush.e@gmail.com',NULL,NULL),(3,'Server','Chaush','+79788888888','chaush.s@gamil.com',NULL,NULL),(4,'Sergey','Hoptyak','+79786666666','serega@gamil.com',NULL,NULL),(5,'adads','asdsad','+79786666666','aider@a.i','2023-01-04','2023-01-28'),(6,'qwerty','qwerty','+79786666666','bronzorree@gmail.com','2023-01-04','2023-01-20');
/*!40000 ALTER TABLE `guest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie`
--

DROP TABLE IF EXISTS `movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie` (
  `idMovie` int NOT NULL AUTO_INCREMENT,
  `status` varchar(45) DEFAULT NULL,
  `nameMovie` varchar(45) DEFAULT NULL,
  `Genre_idGenre` int NOT NULL,
  PRIMARY KEY (`idMovie`),
  KEY `fk_Movie_Genre1_idx` (`Genre_idGenre`),
  CONSTRAINT `fk_Movie_Genre1` FOREIGN KEY (`Genre_idGenre`) REFERENCES `genre` (`idGenre`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie`
--

LOCK TABLES `movie` WRITE;
/*!40000 ALTER TABLE `movie` DISABLE KEYS */;
INSERT INTO `movie` VALUES (1,'можно взять в прокат','Оно',1),(2,'можно взять в прокат','Зеленая миля',2),(3,'можно взять в прокат','Троя',3),(4,'можно взять в прокат','Космическая одиссея 2001 года',4),(5,'можно взять в прокат','Молчание ягнят',5),(6,'можно взять в прокат','Джанго освобожденный',6),(7,'можно взять в прокат','Друзья',7);
/*!40000 ALTER TABLE `movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rental`
--

DROP TABLE IF EXISTS `rental`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rental` (
  `idRental` int NOT NULL,
  `RentalDate` date DEFAULT NULL,
  `checkIn` date DEFAULT NULL,
  `checkOut` date DEFAULT NULL,
  `Movie_idMovie` int NOT NULL,
  `Guest_idGuest` int NOT NULL,
  PRIMARY KEY (`idRental`),
  KEY `fk_Rental_Movie1_idx` (`Movie_idMovie`),
  KEY `fk_Rental_Guest1_idx` (`Guest_idGuest`),
  CONSTRAINT `fk_Rental_Guest1` FOREIGN KEY (`Guest_idGuest`) REFERENCES `guest` (`idGuest`),
  CONSTRAINT `fk_Rental_Movie1` FOREIGN KEY (`Movie_idMovie`) REFERENCES `movie` (`idMovie`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rental`
--

LOCK TABLES `rental` WRITE;
/*!40000 ALTER TABLE `rental` DISABLE KEYS */;
INSERT INTO `rental` VALUES (1,'2017-06-05','2017-06-05','2017-06-05',1,1);
/*!40000 ALTER TABLE `rental` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'vhs_project_db'
--

--
-- Dumping routines for database 'vhs_project_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-10  5:08:32
