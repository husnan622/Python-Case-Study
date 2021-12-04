-- phpMyAdmin SQL Dump
-- version 3.4.5
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Sep 08, 2017 at 08:02 AM
-- Server version: 5.5.16
-- PHP Version: 5.3.8

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `db_petugas`
--

-- --------------------------------------------------------

--
-- Table structure for table `petugas`
--

CREATE TABLE IF NOT EXISTS `petugas` (
  `petugas_kode` varchar(10) NOT NULL,
  `petugas_nama` varchar(30) NOT NULL,
  `petugas_tgl_lahir` date NOT NULL,
  `petugas_alamat` varchar(30) NOT NULL,
  `petugas_no_hp` varchar(15) NOT NULL,
  PRIMARY KEY (`petugas_kode`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `petugas`
--

INSERT INTO `petugas` (`petugas_kode`, `petugas_nama`, `petugas_tgl_lahir`, `petugas_alamat`, `petugas_no_hp`) VALUES
('0001', 'Tania Noor', '2001-11-06', 'Cisalak Rt02 Rw12 No.17\r\n', '08128829964'),
('0002', 'Ganesha Noor', '2017-05-03', 'Cisalak rt02 rw12 No. 17', '021111111');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
