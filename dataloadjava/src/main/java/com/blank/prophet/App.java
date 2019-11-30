package com.blank.prophet;

import com.blank.prophet.dataload.EnWikiLoad;
import com.blank.prophet.dataload.RedditLoad;
import com.blank.prophet.utils.Config;
import com.blank.prophet.utils.SQLiteConnector;
import org.apache.commons.cli.*;

import java.io.File;
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
        commad(args);
    }

    public static void InsertRedditData(String path) {
        List<File> files = RedditLoad.getFiles(path);
        files.forEach(file -> System.out.println(file.getName()));
        RedditLoad.readData(files);
    }
    public static void InsertEnWiki() {
        List<EnWikiLoad> list = new ArrayList<>(8);
        for (int i = 0; i < 8; i++) { list.add(new EnWikiLoad(i, 8)); }
        list.forEach(Thread::start);
    }
    private static void commad(String[] args) {
        Options options = new Options();
        options.addOption("h","help",false,"Print this usage information");
        options.addOption("ops", true, "ops detonate table");
        options.addOption("d", true, "file dir name");
        CommandLineParser parser = new DefaultParser();
        CommandLine cmd = null;
        String result = "";
        try {
            cmd = parser.parse(options, args);
        } catch (ParseException e) {
            e.printStackTrace();
            return;
        }
        if (cmd.hasOption("h")) {
            System.out.println("-d <file dir> relative file dir to load data");
            System.out.println("-h help info display");
            System.out.println("-ops [enwiki][reddit] ops detonate table");
            return;
        }
        switch (cmd.getOptionValue("ops")) {
            case "reddit": InsertRedditData(cmd.getOptionValue("d"));
            break;
            case "enwiki": InsertEnWiki();
            break;
            default: System.out.println("-h for help");
            break;
        }
    }
}
