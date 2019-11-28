package com.blank.prophet.utils;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.Hashtable;
import java.util.Properties;

/**
 * @author seven
 * @description com.blank.prophet.utils
 * @date 11/27/19
 * @version 1.0
 */
public class Config {
    public static Hashtable<String, String> config = new Hashtable<>();

    private Config() {
        String configPath = this.getClass().getClassLoader().getResource("app.properties").getPath();
        Properties properties = new Properties();
        config.put("root", System.getProperty("user.dir"));
        config.put("app.properties", configPath);
        InputStream appStream = null;
        try {
            appStream = new FileInputStream(configPath);
            properties.load(appStream);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            System.err.println("file not exists");
            System.exit(-1);
        } catch (IOException e) {
            e.printStackTrace();
            System.err.println("file read failed");
            System.exit(-1);
        }

        properties.forEach((key, value) -> {
            config.put(key.toString(), value.toString());
        });
    }

    private static class InstanceHolder {
        private final static Config instance = new Config();
    }

    public static Config getInstance() {
        return InstanceHolder.instance;
    }
    public static void set(String key, String value) {
        config.put(key, value);
    }
    public static String get(String key) {
        Config instance = InstanceHolder.instance;
        return config.get(key);
    }

}
