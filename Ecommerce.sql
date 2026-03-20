CREATE DATABASE  IF NOT EXISTS `e_commerce` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `e_commerce`;
-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: e_commerce
-- ------------------------------------------------------
-- Server version	8.0.41

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
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart` (
  `ID` varchar(10) NOT NULL,
  `ProductName` varchar(255) DEFAULT NULL,
  `Category` varchar(50) DEFAULT NULL,
  `Price` decimal(10,2) DEFAULT NULL,
  `StockAvailability` varchar(50) DEFAULT NULL,
  `Rating` decimal(3,1) DEFAULT NULL,
  `Seller` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `ID` varchar(10) NOT NULL,
  `ProductName` varchar(255) DEFAULT NULL,
  `Category` varchar(50) DEFAULT NULL,
  `Price` decimal(10,2) DEFAULT NULL,
  `StockAvailability` varchar(50) DEFAULT NULL,
  `Rating` decimal(3,1) DEFAULT NULL,
  `Seller` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES ('P001','iPhone 14','Electronics',799.00,'In Stock',4.5,'Apple Store'),('P002','Adidas Sneakers','Footwear',120.00,'Limited Stock',4.7,'Adidas Official'),('P003','Samsung Galaxy S23','Electronics',999.00,'Out of Stock',4.6,'Samsung Store'),('P004','Wooden Dining Table','Furniture',450.00,'In Stock',4.3,'Home Decor Ltd.'),('P005','Sony Headphones','Electronics',199.00,'In Stock',4.8,'Sony Official'),('P006','Smartwatch Series 8','Electronics',399.00,'In Stock',4.6,'Apple Store'),('P007','Gaming Laptop','Electronics',1200.00,'Limited Stock',4.5,'Dell Official'),('P008','Wireless Earbuds','Electronics',150.00,'In Stock',4.7,'Bose Official'),('P009','Yoga Mat','Fitness',50.00,'In Stock',4.8,'Sports Gear'),('P010','DSLR Camera','Electronics',1500.00,'Out of Stock',4.6,'Canon Store'),('P011','Bluetooth Speaker','Electronics',99.00,'In Stock',4.7,'JBL Store'),('P012','Office Chair','Furniture',230.00,'Limited Stock',4.4,'Home Essentials'),('P013','Smart TV','Electronics',780.00,'In Stock',4.5,'Samsung Store'),('P014','Fitness Tracker','Fitness',89.00,'Out of Stock',4.6,'Fitbit Official'),('P015','Tablet PC','Electronics',650.00,'In Stock',4.6,'Microsoft Store'),('P016','Running Shoes','Footwear',75.00,'Limited Stock',4.5,'Nike Store'),('P017','Backpack','Accessories',55.00,'In Stock',4.7,'Outdoor Gear'),('P018','Coffee Maker','Home Appliances',120.00,'Out of Stock',4.5,'KitchenPro'),('P019','Gaming Mouse','Electronics',45.00,'In Stock',4.6,'Logitech Store'),('P020','Smart Home Camera','Electronics',130.00,'Limited Stock',4.5,'Security Plus'),('P021','Eco-Friendly Reusable Straws','Kitchen',15.00,'In Stock',4.8,'GreenLiving'),('P022','Personalized Pet Collar','Pet Supplies',25.00,'Limited Stock',4.7,'PetCare'),('P023','Smart LED Desk Lamp','Home & Office',45.00,'In Stock',4.6,'BrightTech'),('P024','Portable Mini Projector','Electronics',120.00,'Out of Stock',4.5,'ViewMax'),('P025','Wireless Charging Notebook','Office Supplies',35.00,'Limited Stock',4.7,'TechGear'),('P026','Handmade Artisanal Candles','Home Decor',30.00,'In Stock',4.8,'CozyGlow'),('P027','Smart Water Bottle','Fitness',40.00,'Limited Stock',4.6,'HydrateTech'),('P028','Electric Heated Socks','Outdoor',50.00,'In Stock',4.7,'WarmFeet'),('P029','Magnetic Eyelashes Kit','Beauty',20.00,'Out of Stock',4.5,'GlamLook'),('P030','Smart Home Air Purifier','Home Appliances',180.00,'Limited Stock',4.6,'PureAir'),('P031','Wireless Mouse','Electronics',40.00,'In Stock',4.6,'Logitech Store'),('P032','Smart Light Bulbs','Home Automation',25.00,'Limited Stock',4.7,'Philips Hue'),('P033','Portable Power Bank','Electronics',50.00,'In Stock',4.5,'Anker Official'),('P034','Gaming Chair','Furniture',300.00,'Out of Stock',4.6,'DXRacer'),('P035','Electric Hair Trimmer','Personal Care',80.00,'In Stock',4.7,'Philips Store'),('P036','Smart Water Bottle','Fitness',35.00,'Limited Stock',4.5,'HydrateTech'),('P037','Noise Cancelling Earbuds','Electronics',250.00,'In Stock',4.8,'Sony Official'),('P038','Adjustable Standing Desk','Furniture',450.00,'Out of Stock',4.6,'ErgoTech'),('P039','Smart Security Camera','Home Security',150.00,'In Stock',4.7,'Nest Store'),('P040','Wireless Charging Pad','Electronics',30.00,'Limited Stock',4.6,'Samsung Store'),('P041','Smart Doorbell','Home Security',200.00,'In Stock',4.7,'Ring Official'),('P042','Electric Toothbrush','Personal Care',90.00,'Out of Stock',4.6,'Oral-B Store'),('P043','Smart Coffee Mug','Home Appliances',120.00,'In Stock',4.5,'Ember'),('P044','Portable Air Purifier','Home Appliances',180.00,'Limited Stock',4.7,'Dyson'),('P045','Smart Thermostat','Home Automation',250.00,'In Stock',4.6,'Nest Store'),('P046','Wireless Headset','Electronics',220.00,'Out of Stock',4.8,'Bose Official'),('P047','Smart Fitness Scale','Fitness',100.00,'In Stock',4.6,'Fitbit Official'),('P048','Electric Kettle','Home Appliances',60.00,'Limited Stock',4.5,'Home Essentials'),('P049','Smart Mirror','Home Automation',300.00,'In Stock',4.7,'TechMirror'),('P050','Portable Blender','Home Appliances',70.00,'Out of Stock',4.6,'NutriBullet'),('P051','Smart Bike Lock','Outdoor',90.00,'In Stock',4.5,'CycloSafe'),('P052','Wireless Door Sensor','Home Security',40.00,'Limited Stock',4.7,'Ring Official'),('P053','Smart Pet Feeder','Pet Supplies',150.00,'In Stock',4.6,'PetTech'),('P054','Electric Heated Blanket','Home Appliances',80.00,'Out of Stock',4.5,'CozyWarm'),('P055','Smart Air Conditioner','Home Appliances',500.00,'Limited Stock',4.7,'LG Store'),('P056','Portable Camping Stove','Outdoor',120.00,'In Stock',4.6,'CampGear'),('P057','Smart Home Hub','Home Automation',250.00,'Out of Stock',4.7,'Amazon Echo'),('P058','Wireless Car Charger','Automotive',50.00,'In Stock',4.6,'Anker Official'),('P059','Smart Sleep Mask','Personal Care',100.00,'Limited Stock',4.5,'SleepTech'),('P060','Electric Foot Massager','Personal Care',150.00,'In Stock',4.7,'RelaxPro'),('P061','Smart Notebook','Office Supplies',40.00,'Out of Stock',4.6,'Rocketbook'),('P062','Portable Espresso Maker','Home Appliances',90.00,'Limited Stock',4.5,'CoffeeTech'),('P063','Smart UV Sanitizer','Personal Care',70.00,'In Stock',4.7,'CleanTech'),('P064','Wireless Meat Thermometer','Kitchen',80.00,'Out of Stock',4.6,'ChefMate'),('P065','Smart Plant Monitor','Home & Garden',60.00,'Limited Stock',4.5,'GreenThumb'),('P066','Electric Bike','Outdoor',1200.00,'In Stock',4.7,'E-Ride'),('P067','Smart Water Filter','Home Appliances',200.00,'Out of Stock',4.6,'PureTech'),('P068','Wireless Video Doorbell','Home Security',180.00,'Limited Stock',4.5,'Ring Official'),('P069','Smart Baby Monitor','Baby Care',150.00,'In Stock',4.7,'BabySafe'),('P070','Electric Scooter','Outdoor',800.00,'Out of Stock',4.6,'E-Ride'),('P071','Smart Alarm Clock','Home Appliances',90.00,'Limited Stock',4.5,'WakeTech'),('P072','Wireless Charging Backpack','Accessories',120.00,'In Stock',4.7,'TechGear'),('P073','Smart Water Dispenser','Home Appliances',250.00,'Out of Stock',4.6,'PureTech'),('P074','Electric Heated Socks','Outdoor',60.00,'Limited Stock',4.5,'WarmFeet'),('P075','Smart Home Speaker','Electronics',150.00,'In Stock',4.7,'Amazon Echo'),('P076','Wireless Charging Desk','Furniture',300.00,'Out of Stock',4.6,'ErgoTech'),('P077','Smart Cooking Pot','Kitchen',200.00,'Limited Stock',4.5,'ChefMate'),('P078','Electric Heated Gloves','Outdoor',80.00,'In Stock',4.7,'WarmHands'),('P079','Smart Home Projector','Electronics',500.00,'Out of Stock',4.6,'ViewTech'),('P080','Wireless Charging Mouse Pad','Accessories',40.00,'Limited Stock',4.5,'TechGear'),('P081','Smart Home Vacuum','Home Appliances',400.00,'In Stock',4.7,'Dyson'),('P082','Electric Heated Jacket','Outdoor',250.00,'Out of Stock',4.6,'WarmWear'),('P083','Smart Home Thermometer','Home Automation',100.00,'Limited Stock',4.5,'Nest Store'),('P084','Wireless Charging Wallet','Accessories',80.00,'In Stock',4.7,'TechGear'),('P085','Smart Home Fan','Home Appliances',150.00,'Out of Stock',4.6,'Dyson'),('P086','Electric Heated Mattress','Home Appliances',300.00,'Limited Stock',4.5,'CozyWarm'),('P087','Smart Home Air Purifier','Home Appliances',350.00,'In Stock',4.7,'Dyson'),('P088','Wireless Charging Suitcase','Accessories',200.00,'Out of Stock',4.6,'TechGear'),('P089','Smart Home Humidifier','Home Appliances',180.00,'Limited Stock',4.5,'Dyson'),('P090','Electric Heated Pillow','Home Appliances',100.00,'In Stock',4.7,'CozyWarm'),('P100','Electric Kettle','Home Appliances',60.00,'In Stock',4.5,'Home Essentials');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-20 20:25:03
