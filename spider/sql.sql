CREATE DATABASE IF NOT EXISTS `prophet` DEFAULT CHARSET utf8mb4 COLLATE utf8mb4_general_ci;
USE `prophet`;

CREATE TABLE `proxies`(
    `id` BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT 'id',
    `ip` CHAR(15) NOT NULL UNIQUE COMMENT 'ip地址',
    `port` INT UNSIGNED NOT NULL COMMENT '端口号',
    `serve_addr` VARCHAR(60) COMMENT '代理所在地址',
    `desc`  CHAR(20) COMMENT '是否匿名',
    `proxy_type` CHAR(10) COMMENT 'HTTP,HTTPS',
    `speed` FLOAT COMMENT '速度',
    `connect_time` FLOAT COMMENT '连接时间',
    `validate_time` DATETIME COMMENT '验证时间',
    `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT '代理ip表';

CREATE TABLE `lagou_jobs`(
    `id` BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT 'id',
    `title` CHAR(250) NOT NULL COMMENT '标题',
    `url` VARCHAR(200) NOT NULL UNIQUE COMMENT 'url',
    `url_object_id` CHAR(32) NOT NULL UNIQUE COMMENT 'URLMD5唯一编码',
    `salary_min` int DEFAULT NULL COMMENT '薪水 最低',
    `salary_max` int DEFAULT NULL COMMENT '薪水 最高',
    `job_city`  VARCHAR(100) COMMENT '工作城市',
    `work_years` CHAR(10) COMMENT '工作年限',
    `degree_need` CHAR(30) COMMENT '学历要求',
    `job_type` VARCHAR(100) COMMENT '工作类型',
    `tags` VARCHAR(200) COMMENT '标签',
    `publish_date` DATETIME COMMENT '发布时间',
    `job_advantage`  VARCHAR(100) COMMENT '职位优势',
    `job_desc` VARCHAR(500) COMMENT '职位描述要求',
    `job_addr` VARCHAR(200) COMMENT '工作地点',
    `company_name` CHAR(100) COMMENT '公司名称',
    `company_url` CHAR(100) COMMENT '公司网址',
    `create_time` TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间'
)ENGINE = InnoDB DEFAULT CHAR SET = utf8mb4 COMMENT '拉钩职位表';

