CREATE TABLE IF NOT EXISTS `user_details` (
  `index` INTEGER PRIMARY KEY AUTOINCREMENT,
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

CREATE TABLE IF NOT EXISTS `questions_list` (
  `index` INTEGER PRIMARY KEY AUTOINCREMENT,
  `content` varchar(5000) NOT NULL
  --CONSTRAINT name_unique UNIQUE (username)
);

CREATE TABLE IF NOT EXISTS `workshop_list` (
  `index` INTEGER PRIMARY KEY AUTOINCREMENT,
  `workshop_name` varchar(5000) NOT NULL,
  `date` varchar(5000) NOT NULL
  --CONSTRAINT name_unique UNIQUE (username)
);

CREATE TABLE IF NOT EXISTS `surveys_list` (
  `index` INTEGER PRIMARY KEY AUTOINCREMENT,
  `user_index` int(11) DEFAULT NULL,
  `workshop_name` varchar(5000) NOT NULL,
  `date` varchar(5000) NOT NULL
  --CONSTRAINT name_unique UNIQUE (username)
  --FOREIGN KEY (user_index) REFERENCES user_details(index),
);

CREATE TABLE IF NOT EXISTS `response_list` (
  `index` INTEGER PRIMARY KEY AUTOINCREMENT,
  `workshop_index` INTEGER NOT NULL,
  `user_index` INTEGER NOT NULL,
  `question_index` INTEGER NOT NULL,
  `score` INTEGER NOT NULL
  --FOREIGN KEY (survey_index) REFERENCES surveys_list(index),
  --FOREIGN KEY (question_index) REFERENCES questions_list(index)
  --CONSTRAINT name_unique UNIQUE (username)
);

--ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10001 ;

--
-- Dumping data for table `user_details`
--

INSERT INTO `user_details` (`username`, `password`, `gender`, `email`, `ethnic_code`, `monthly_income`, `district`, `tertiary_class`, `tertiary_name`) VALUES
('af89bb4adc33c1ae7f99f74e78021ddc', 'password', 'Female', 'example@gmail.com', '4', '$3,000 to $4,999', '27', 'ITE', 'ite ce');
-- INSERT THE REST OF THE STUDENTS IN HERE

-- INSERT ALL THE DEFAULT QUESTIONS INTO DB
INSERT INTO `questions_list` (`content`) VALUES
("I have a certain amount of intelligence, and I can't really do much to change it."),
("My intelligence is something that I cannot change very much."),
("I believe that no matter who you are, you can significantly change your intelligence level."),
("I believe that you can't really change how intelligent you are."),
("I believe that you can always substantially change how intelligent you are."),
("You can learn new things, but you can't really change your basic intelligence."),
("No matter how much intelligence you have, whether high or low, you can always change it to quite a degree."),
("I can change even my basic intelligence level considerably."),
("People have a certain amount of talent, and you can't really do much to change it."),
("Your talent is something you can't change very much."),
("No matter who you are, you can significantly change your level of talent."),
("To be honest, you can't really change how much talent you have."),
("You can always substantially change how much talent you have."),
("I can learn new things, but I can't really change my basic level of talent."),
("No matter how much talent you have, you can always change it quite a bit."),
("You can change even your basic talent level considerably."),
("I can make unpopular or difficult decisions that affect other people if necessary."),
("I don't think of myself as a strong person when dealing with life's challenges and difficulties."),
("Under pressure, I stay focused and think clearly."),
("I prefer to take the lead in solving problems, rather than letting others make all the decisions."),
("I feel in control of my life."),
("I try to see the funny side of things when I am faced with problems."),
("Good or bad, I believe that most things happen for a reason."),
("I don't believe that I can achieve my goals if there are problems."),
("I work to attain my goals, no matter what problems I encounter along the way."),
("Having to cope with stress can make me stronger."),
("On a whole, I am satisfied with myself."),
("At times, I think I'm no good at all."),
("I feel that I have a number of good qualities."),
("I am able to do things as well as most people."),
("I feel I do not have much to be proud of."),
("I certainly feel useless at times."),
("I feel that I'm a person of worth, at least on an equal plane with others."),
("I wish I could have more respect for myself."),
("All in all, I am inclined to feel that I am a failure."),
("I take a positive attitude towards myself."),
("I can always manage to solve difficult problems if I try hard enough."),
("If someone opposes me, I can find means and ways to get what I want."),
("It is easy for me to stick to my aims and accomplish my goals."),
("I am confident that I can efficiently deal with unexpected events."),
("Thanks to my resourcefulness, I know how to handle unforeseen situations."),
("I can solve most problems if I invest the necessary effort."),
("I can remain calm when facing difficulties because I can rely on my coping abilities."),
("When I am confronted with a problem, I can usually find several solutions."),
("If I'm in a bind, I can usually think of something to do."),
("No matter what comes my way, I'm usually able to handle it."),
("It's fun to learn about unfamiliar subjects."),
("It's fascinating to learn new information."),
("I enjoy exploring new ideas."),
("If I get to learn something new, I like to find out more."),
("It's fun to discuss abstract concepts."),
("I paint an interesting picture of the future for my group."),
("I'm always seeking new opportunities for my group."),
("I inspire my group with my plan for the future."),
("I have a clear understanding of where we are going."),
("I'm able to get others committed to my dream."),
("I would describe myself as someone who actively seeks as much information as I can in a new situation."),
("When I am participating in an activity, I tend to get so involved that I lose track of time."),
("I frequently find myself looking for new opportunities to grow as a person."),
("I am not the type of person who probes deeply into new situations or things."),
("When I am actively interested in something, it takes a great deal to interrupt me."),
("My friends would describe me as someone who is 'extremely intense' when in the middle of doing something."),
("Everywhere I go, I am out looking for new things or experiences."),
("I am able to finish all my work during a set amount of time."),
("I know all the tasks I have to accomplish for the day."),
("I am able to plan and set goals for my projects."),
("I can set aside distractions and focus on what I am doing."),
("I set up a schedule for tasks and projects to be done."),
("I am sensitive to what others are not saying."),
("I am aware of what others imply but do not say."),
("I understand how others feel."),
("I listen for more than just the spoken words."),
("I assure others that I will remember what they say."),
("I summarise points of agreement and disagreement when appropriate."),
("I keep track of points others make."),
("I assure others that I am listening by using verbal acknowledgements."),
("I assure others that I am receptive to their ideas."),
("I ask questions that show my understanding of others' positions."),
("I show others that I am listening through my body language (e.g. head nods, eye contact)"),
("I am able to finish all my work during a set amount of time..1"),
("I know all the tasks I have to accomplish for the day..1"),
("I am able to plan and set goals for my projects..1"),
("I can set aside distractions and focus on what I am doing..1"),
("I set up a schedule for tasks and projects to be done..1"),
("How much do you contribute ideas/information/resources?"),
("How participatory are you?"),
("What is your typical standard of work quality?"),
("How well do you manage your time?"),
("How much do you support the team?"),
("How prepared are you usually?"),
("How do you participate in group problem solving?"),
("How aware are you of the team dynamics and your impact on the team?"),
("How supportive are you in a team?"),
("How flexible are you between roles?"),
("How self-reflective are you?");

-- INSERT ALL THE DEFAULT DATA INTO DB