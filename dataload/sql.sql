CREATE DATABASE IF NOT EXISTS `yelp` DEFAULT CHARSET utf8mb4 COLLATE utf8mb4_general_ci;
USE yelp;

CREATE TABLE `users`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'new id',
    `user_id` CHAR(22) NOT NULL UNIQUE COMMENT '原有的id',
    `name` CHAR(60) NOT NULL COMMENT '名字',
    `review_count` INT UNSIGNED,
    `yelping_since` DATETIME,
    `useful` INT UNSIGNED,
    `funny` INT UNSIGNED,
    `cool` INT UNSIGNED,
    `elite` VARCHAR(100),
    `friends` TEXT,
    `fans` INT UNSIGNED,
    `average_stars` DOUBLE,
    `compliment_hot` INT UNSIGNED,
    `compliment_more` INT UNSIGNED,
    `compliment_profile` INT UNSIGNED,
    `compliment_list` INT UNSIGNED,
    `compliment_note` INT UNSIGNED,
    `compliment_plain` INT UNSIGNED,
    `compliment_cool` INT UNSIGNED,
    `compliment_funny` INT UNSIGNED,
    `compliment_writer` INT UNSIGNED,
    `compliment_photos` INT UNSIGNED,
    `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `updated` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT 'yelp user table';






CREATE TABLE `business`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'id',
    `business_id` CHAR(22) NOT NULL UNIQUE COMMENT '原有的id',
    `name` VARCHAR(100) NOT NULL,
    `address` VARCHAR(200),
    `city` CHAR(100),
    `state` CHAR(10),
    `postal_code` CHAR(10),
    `latitude`  DECIMAL(10,7),
    `longitude` DECIMAL(10,7),
    `stars` DOUBLE,
    `review_count` INT UNSIGNED DEFAULT 0,
    `is_open` TINYINT UNSIGNED DEFAULT 0,
    `attributes` TEXT COMMENT '每个属性用逗号隔开',
    `categories` VARCHAR(500),
    `hours` VARCHAR(200),
    `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `updated` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT 'yelp business table';



CREATE TABLE `checkins`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'id',
    `business_id` CHAR(22) NOT NULL,
    `date` DATETIME NOT NULL,
    `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `updated` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT 'yelp checkins table';

CREATE TABLE `tips`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'id',
    `user_id` CHAR(22) NOT NULL,
    `business_id` CHAR(22) NOT NULL,
    `text` TEXT NOT NULL ,
    `date` DATETIME,
    `compliment_count` INT UNSIGNED DEFAULT 0,
    `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `updated` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT 'yelp tips table';

CREATE TABLE `reviews`(
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'id',
    `review_id` CHAR(22) NOT NULL,
    `user_id` CHAR(22) NOT NULL,
    `business_id` CHAR(22) NOT NULL,
    `stars` DOUBLE,
    `useful` INT UNSIGNED,
    `funny` INT UNSIGNED,
    `cool` INT UNSIGNED,
    `text` TEXT,
    `date` DATETIME,
    `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `updated` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT 'yelp reviews table';

SELECT COUNT(*) AS checkins_count FROM checkins;
SELECT COUNT(*) AS tips_count FROM tips;
SELECT COUNT(*) AS reviews_count FROM reviews;
show tables;


show databases ;
USE yelp;
SHOW TABLES;

CREATE DATABASE IF NOT EXISTS `enwikis` DEFAULT CHARSET utf8mb4 COLLATE utf8mb4_general_ci;

use enwikis;
show tables ;

CREATE TABLE `articles` (
    `id` BIGINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'id',
    `article_id` INTEGER,
    `title` VARCHAR(255) ,
    `section_title` TEXT,
    `section_text` LONGTEXT,
    `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `updated` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT 'enwikis articles table';
