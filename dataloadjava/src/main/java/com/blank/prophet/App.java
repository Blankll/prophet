package com.blank.prophet;

import com.blank.prophet.dataload.EnWikiLoad;
import com.blank.prophet.utils.Config;
import com.blank.prophet.utils.SQLiteConnector;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args ) throws SQLException {
        System.out.println( "Hello World!" );
        List<EnWikiLoad> list = new ArrayList<>(8);
        for (int i = 0; i < 8; i++) { list.add(new EnWikiLoad(i, 8)); }
        list.forEach(el -> el.start());
//        Connection sqliteConnector = SQLiteConnector.getConnect("enwiki-20170820.db");
//        Statement stm = sqliteConnector.createStatement();
//        String sqliteSql = "SELECT * FROM articles";
//        try {
//            ResultSet resultSet = stm.executeQuery(sqliteSql);
//            for (int i = 0; resultSet.next(); i++) {
//                int articleId = resultSet.getInt("ARTICLE_ID");
//                String title = resultSet.getString("TITLE");
//                String sectionTitle = resultSet.getString("SECTION_TITLE");
//                String text = resultSet.getString("SECTION_TEXT");
//                System.out.println("read line" +  i);
//            }
//
//        } catch (SQLException e) {
//            e.printStackTrace();
//        }
    }
}
