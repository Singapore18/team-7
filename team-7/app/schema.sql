--
-- Database: `samplevideo_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

DROP TABLE IF EXISTS `user_details`;

CREATE TABLE IF NOT EXISTS `user_details` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `role` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `ethnic_code` int(11) DEFAULT NULL,
  `monthly_income` varchar(255) DEFAULT NULL,
  `district` int(11) DEFAULT NULL,
  `tertiary_class` varchar(255) DEFAULT NULL,
  `tertiary_name` varchar(255) DEFAULT NULL
  --CONSTRAINT name_unique UNIQUE (username)
);

--ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10001 ;

--
-- Dumping data for table `user_details`
--

INSERT INTO `user_details` (`id`, `role`, `username`, `password`, `gender`, `email`, `ethnic_code`, `monthly_income`, `district`, `tertiary_class`, `tertiary_name`) VALUES
(1, 0, 'user', 'password', 'Female', 'example@gmail.com', '4', '$3,000 to $4,999', '27', 'ITE', 'ite ce');
