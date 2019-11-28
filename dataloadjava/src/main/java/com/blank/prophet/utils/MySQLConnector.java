package com.blank.prophet.utils;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 * @author Blank
 * @Description: com.blank.prophet.utils
 * @Date: 11/27/19
 * @Version: 1.0
 */
public class MySQLConnector {
    public static Connection getConnector() {
        Connection con = null;
        try {
            String driver = Config.get("driver");
            Class.forName(driver);
            String url = "jdbc:mariadb://" + Config.get("host") + ":" + Config.get("port") + "/" + Config.get("dbname") + "?characterEncoding=utf-8&useSSL" + Config.get("ssl");
            con = DriverManager.getConnection(url, Config.get("username"), Config.get("password"));
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        }

        return con;
    }
}
