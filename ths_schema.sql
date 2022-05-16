CREATE TABLE `pupils`(
    `studentid` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `first_name` VARCHAR(255) NOT NULL,
    `middle_name` VARCHAR(255) NOT NULL,
    `last_name` VARCHAR(255) NOT NULL,
    `address` TEXT NOT NULL,
    `date_of_birth` DATE NOT NULL,
    `place_of_birth` VARCHAR(255) NOT NULL,
    `date_of_admission` DATE NOT NULL,
    `sex` INT NOT NULL,
    `classid` INT NOT NULL,
    `subjectid` INT NOT NULL,
    `familyid` INT NOT NULL
);
ALTER TABLE
    `pupils` ADD UNIQUE `pupils_studentid_unique`(`studentid`);
ALTER TABLE
    `pupils` ADD INDEX `pupils_familyid_index`(`familyid`);
CREATE TABLE `teachers`(
    `teacherid` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `first_name` INT NOT NULL,
    `last_name` INT NOT NULL,
    `sex` INT NOT NULL,
    `date_of_birth` INT NOT NULL,
    `email` INT NOT NULL,
    `address` INT NOT NULL,
    `phone_number` INT NOT NULL,
    `date_of_hire` INT NOT NULL,
    `years_of_service` INT NOT NULL,
    `salary` INT NOT NULL
);
CREATE TABLE `classes`(
    `classid` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `teacherid` INT NOT NULL,
    `studentid` INT NOT NULL,
    `class_name` INT NOT NULL
);
CREATE TABLE `subjects`(
    `subjectid` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `subject_name` INT NOT NULL
);
CREATE TABLE `attendance`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `date` DATE NOT NULL,
    `attended` TINYINT(1) NOT NULL,
    `teacherid` INT NOT NULL,
    `studentid` INT NOT NULL
);
ALTER TABLE
    `attendance` ADD INDEX `attendance_studentid_index`(`studentid`);
CREATE TABLE `family_data`(
    `familyid` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `mother_first_name` INT NOT NULL,
    `mother_last_name` INT NOT NULL,
    `email` INT NOT NULL,
    `phone_number` INT NOT NULL,
    `sex` INT NOT NULL,
    `address` INT NOT NULL,
    `studentid` INT NOT NULL,
    `father_date_of_birth` INT NOT NULL,
    `mother_profession` INT NOT NULL,
    `mother_place_of_work` INT NOT NULL,
    `father_first_name` INT NOT NULL,
    `father_last_name` INT NOT NULL,
    `father_profession` INT NOT NULL,
    `father_place_of_work` INT NOT NULL,
    `mother_date_of_birth` INT NOT NULL
);
CREATE TABLE `results`(
    `resultid` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `studentid` INT NOT NULL,
    `classid` INT NOT NULL,
    `subjectid` INT NOT NULL,
    `teacherid` INT NOT NULL,
    `score` INT NOT NULL,
    `test` INT NOT NULL,
    `exam` INT NOT NULL,
    `first_semester` TINYINT(1) NOT NULL,
    `second_semester` TINYINT(1) NOT NULL,
    `third_semester` TINYINT(1) NOT NULL,
    `year` YEAR NOT NULL
);
ALTER TABLE
    `results` ADD INDEX `results_studentid_classid_subjectid_teacherid_index`(
        `studentid`,
        `classid`,
        `subjectid`,
        `teacherid`
    );
CREATE TABLE `user`(
    `userid` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `username` INT NOT NULL,
    `password` INT NOT NULL
);
ALTER TABLE
    `user` ADD UNIQUE `user_username_unique`(`username`);
ALTER TABLE
    `user` ADD UNIQUE `user_password_unique`(`password`);
CREATE TABLE `admin`(
    `adminid` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `studentid` INT NOT NULL,
    `familyid` INT NOT NULL,
    `teacherid` INT NOT NULL
);
ALTER TABLE
    `pupils` ADD CONSTRAINT `pupils_familyid_foreign` FOREIGN KEY(`familyid`) REFERENCES `family_data`(`familyid`);
ALTER TABLE
    `attendance` ADD CONSTRAINT `attendance_teacherid_foreign` FOREIGN KEY(`teacherid`) REFERENCES `teachers`(`teacherid`);
ALTER TABLE
    `results` ADD CONSTRAINT `results_classid_foreign` FOREIGN KEY(`classid`) REFERENCES `classes`(`classid`);
ALTER TABLE
    `classes` ADD CONSTRAINT `classes_teacherid_foreign` FOREIGN KEY(`teacherid`) REFERENCES `teachers`(`teacherid`);
ALTER TABLE
    `results` ADD CONSTRAINT `results_subjectid_foreign` FOREIGN KEY(`subjectid`) REFERENCES `subjects`(`subjectid`);