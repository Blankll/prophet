package com.blank.prophet.dataload;

import com.blank.prophet.pojos.Article;
import com.blank.prophet.utils.MySQLConnector;
import com.blank.prophet.utils.SQLiteConnector;

import java.sql.*;
import java.text.SimpleDateFormat;
import java.util.Hashtable;

/**
 * @Auther: Blank
 * @Description: com.blank.prophet.dataload
 * @Date: 11/27/19
 * @Version: 1.0
 */
public class EnWikiLoad extends Thread {
    private int hash = 0;
    private int count = 0;
    public EnWikiLoad(int hash, int count) {
        this.hash = hash;
        this.count = count;
    }
    public void loadDataArticle() {
        Connection sqliteConnector = SQLiteConnector.getConnect("enwiki-20170820.db");
        Connection mysqlConnector = MySQLConnector.getConnector();

        Statement sqliteStm = null;
        PreparedStatement pMysqlStm = null;
        String sqliteSql = "SELECT * FROM articles";
        String mysqlSql = "INSERT INTO `articles`(`article_id`, `title`, `section_title`, `section_text`) VALUES (?, ?, ?, ?)";

        ResultSet resultSet = null;
        try {
            mysqlConnector.setAutoCommit(false);
            sqliteStm = sqliteConnector.createStatement();
            pMysqlStm = mysqlConnector.prepareStatement(mysqlSql);
            resultSet = sqliteStm.executeQuery(sqliteSql);
            int insertCount = 0;
            for (int i = 0; resultSet.next(); i++) {
                if ( i % count == this.hash) {
                    pMysqlStm.setInt(1, resultSet.getInt("ARTICLE_ID"));
                    pMysqlStm.setString(2, resultSet.getString("TITLE"));
                    pMysqlStm.setString(3, resultSet.getString("SECTION_TITLE"));
                    pMysqlStm.setString(4, resultSet.getString("SECTION_TEXT"));
                    pMysqlStm.execute();
                    insertCount++;
                }
                if ((insertCount %= 1000) == 0) {
                    mysqlConnector.commit();
                    SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
                    System.out.println("THREAD: " + currentThread().getId()+ ": " + format.format(System.currentTimeMillis()) + "; INSERT SUCCESS!");
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

    }

    @Override
    public void run() {
        this.loadDataArticle();
    }
}
