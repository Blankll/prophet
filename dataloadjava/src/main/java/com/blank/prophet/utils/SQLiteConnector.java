package com.blank.prophet.utils;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 * @Auther: Blank
 * @Description: com.blank.prophet.utils
 * @Date: 11/27/19
 * @Version: 1.0
 */
public class SQLiteConnector {
    private Connection connector = null;
    private String url = "";

    public SQLiteConnector(String fileName) {
        this.url = "jdbc:sqlite:" + this.getClass().getClassLoader().getResource(fileName).getPath();
        try {
            Class.forName("org.sqlite.JDBC");
            this.connector = DriverManager.getConnection(this.url);
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        }
    }

    public static Connection getConnect (String fileName) {
        SQLiteConnector ins = new SQLiteConnector(fileName);
        Connection connector = ins.connector;

        return connector;
    }

}
