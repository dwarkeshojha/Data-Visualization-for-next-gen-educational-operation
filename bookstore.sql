/*
SQLyog Community v11.31 (32 bit)
MySQL - 4.1.14-nt : Database - bookstore
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bookstore` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `bookstore`;

/*Table structure for table `book` */

DROP TABLE IF EXISTS `book`;

CREATE TABLE `book` (
  `title` varchar(40) default NULL,
  `author` varchar(40) default NULL,
  `category` varchar(30) default NULL,
  `year` int(11) default NULL,
  `isbn` int(11) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `book` */

insert  into `book`(`title`,`author`,`category`,`year`,`isbn`) values ('Accountancy','D.S Arora','BUSINESS',2012,3652),('C Explorer','D.S Verma','CSE',2013,3653),('C++ programming','R.N Sinha','CSE',2011,4521),('Mechanics','K.L verma','ME',2015,3256),('Fluid Mechanics','H.R Harish','ME',2006,3242),('Transformation Mechanic','B.L Bani','ME',2014,6598),('Embadded System','K.l Punia','ECE',2012,3654),('Charter Accont','F.M Verma','ACCOUNT',2013,3697),('Environment','P.N punia','CE',2011,2546),('The World Economy','B.S basu','ECONOMICS',2017,9875),('Transformers','K.L pandu','EE',2013,2546);

/*Table structure for table `circular` */

DROP TABLE IF EXISTS `circular`;

CREATE TABLE `circular` (
  `CIRNO` int(10) NOT NULL default '0',
  `CIRDATE` int(10) default NULL,
  `CIRCULAR` char(30) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `circular` */

insert  into `circular`(`CIRNO`,`CIRDATE`,`CIRCULAR`) values (0,6,'NTHNG'),(12034,25,'counselling will close tomorro');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `username` varchar(30) default NULL,
  `password` varchar(30) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`username`,`password`) values ('admin','admin1234'),('aamir','aamir786'),('tabis','1234'),('no','1234'),('nazia','786');

/*Table structure for table `marks` */

DROP TABLE IF EXISTS `marks`;

CREATE TABLE `marks` (
  `ROLL_NO` int(11) NOT NULL default '0',
  `name` varchar(30) default NULL,
  `course` varchar(30) default NULL,
  `sem1` int(11) default NULL,
  `sem2` int(11) default NULL,
  `sem3` int(11) default NULL,
  `sem4` int(11) default NULL,
  `sem5` int(11) default NULL,
  `sem6` int(11) default NULL,
  `sem7` int(11) default NULL,
  `sem8` int(11) default NULL,
  `total` int(15) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `marks` */

insert  into `marks`(`ROLL_NO`,`name`,`course`,`sem1`,`sem2`,`sem3`,`sem4`,`sem5`,`sem6`,`sem7`,`sem8`,`total`) values (54,'asd','MBA',66,88,67,88,98,889,89,899,1875),(36,'saad','BTECH',689,700,855,965,845,798,765,890,1486),(6,'dc','BTECH',65,87,66,26,58,87,65,85,561),(3,'Kunal','Reena',897,987,566,625,366,366,665,366,3657),(8,'asad','BTECH',987,658,698,668,665,569,668,956,5869);

/*Table structure for table `students` */

DROP TABLE IF EXISTS `students`;

CREATE TABLE `students` (
  `ROLL_NO` int(15) NOT NULL default '0',
  `NAME` varchar(30) default NULL,
  `SEMESTER` varchar(10) default NULL,
  `COURSE` varchar(30) default NULL,
  `F_NAME` varchar(30) default NULL,
  `M_NAME` varchar(30) default NULL,
  `YEAR_OF_ADM` int(10) default NULL,
  `EMAIL` varchar(30) default NULL,
  `ADDRESS` varchar(40) default NULL,
  PRIMARY KEY  (`ROLL_NO`),
  KEY `ID` (`ROLL_NO`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `students` */

insert  into `students`(`ROLL_NO`,`NAME`,`SEMESTER`,`COURSE`,`F_NAME`,`M_NAME`,`YEAR_OF_ADM`,`EMAIL`,`ADDRESS`) values (1,'Bakul Nagpal','bakul@gmai','Monika Nagpal','A','Parveen Nagpal',2016,NULL,NULL),(3,'Kunal','kamal@yaho','Reena','A','S.Raj',2015,NULL,NULL),(5,'Aasij','6','BTECH','md asid','maotu',2016,'asib','njdic'),(6,'dc','2','BTECH','jcds','jncdsj',2015,'jnsd','jnsdk'),(8,'asad','7','BTECH','dvfe','wefvw',2015,'dwef','wef'),(12,'ares','2','BTECH','h','maat',2016,'sid','jisp'),(35,'d','1','BTECH','dv','vgrt',2016,'d','de'),(36,'saad','5','BTECH','Mohd Rajoid','Sahh Bano',2016,'saad@gmail.com','Delhi'),(42,'RGMDK','3','BTECH','FDGG','GDRH',NULL,'AGGH',NULL),(45,'uguyg','1','BTECH','gvkyt','fyt',2015,'fyt','ftyf'),(54,'asd','3','MBA','anam','utr',NULL,'aamir.asd','janak'),(78,'edewf','1','MBA','dewf','def',2017,'tr','regtr'),(102,'Alam','alam@gmail','perween','A','MD. Alam',2015,NULL,NULL),(123,'ashds','7','BTECH','mana','sana',2013,'aamir.andome','uttamanagar'),(798,'sdds','4','MBA','Aamir','reem',2018,'aamir@gmail.com','qewfwf'),(1548,'sajid','5','BTECH','msda',NULL,NULL,NULL,NULL),(6547,'HATIM','3','BTECH','AAMIR','REEM',NULL,NULL,NULL),(8598,'BGIYT','1',NULL,NULL,NULL,NULL,NULL,NULL),(77878,'ferb','6','MCA','ewgre','dfrg',2016,'dewgr','dwf'),(151531001,'Noor','7','BTECH','Md.Noor','Naseema Bano',2016,'noor555@gmail.com','saheen bagh new delhi'),(151531010,'Amrit','7','BTECH','Mr. Chaudhary','Shila Dixit',2015,'amrit@gmail.com','Muzaffernagr'),(515310001,'Aamir Abdine','7','BTECH','Md. Asif','Naushaba perween',2017,'aamir.abdine@gmail.com','jankapuri, New Delhi'),(1515310001,'Aamir Abdine','aamir.abdi','Naushaba Perween','A','MD. Asif',2015,NULL,NULL),(1515310002,'Abdul','7','BTECH','Md.Khursheed','Sazia Bano',2015,'noor555@gmail.com','saheen bagh'),(1515310008,'Aman Kumar','7','BTECH','Kumar Verma','Shila Devi',2015,'amankumar@gmail.com','greater noida');

/*Table structure for table `teachers` */

DROP TABLE IF EXISTS `teachers`;

CREATE TABLE `teachers` (
  `ID` int(10) NOT NULL default '0',
  `NAME` char(30) default NULL,
  `DEPARTMENT` char(30) default NULL,
  `DESIGNATION` char(30) default NULL,
  `EMAIL` char(30) default NULL,
  `ADDRESS` char(30) default NULL,
  PRIMARY KEY  (`ID`),
  KEY `ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `teachers` */

insert  into `teachers`(`ID`,`NAME`,`DEPARTMENT`,`DESIGNATION`,`EMAIL`,`ADDRESS`) values (1,'Rohit Sharma','B-90','rohit1@gmail.com','Python','Computer Science'),(2,'Sanjay Gupta','A-90','sanjay@gmail.com','java','Computer Science'),(13,'asad','CE','Asst. Professor','asad@gmail.com','g.noida'),(98,'EDEF','CSE','ASST. PROFESSOR','FVVFVV','EVVRV'),(1012,'Dhsndhri Parihsr','CSE','Asst. Professor','parihar@gmail.com','Vaishali,New Delhi'),(2314,'wdwefrw','CE','Professor','sa','bdyuw');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
