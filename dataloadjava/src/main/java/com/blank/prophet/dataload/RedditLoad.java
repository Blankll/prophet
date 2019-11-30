package com.blank.prophet.dataload;

import com.blank.prophet.pojos.Comment;
import com.blank.prophet.utils.BooleanTypeAddapter;
import com.blank.prophet.utils.MySQLConnector;
import com.blank.prophet.utils.TimestampTypeAdapter;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import org.apache.commons.cli.*;

import java.io.*;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.Timestamp;
import java.text.SimpleDateFormat;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class RedditLoad {
    public static List<File> getFiles(String fileDir) {
        List<File> files = new ArrayList<>();
        File rootFile = new File(fileDir);
        File[] itemFiles = rootFile.listFiles();
        if (itemFiles == null) { return null; }
        Arrays.stream(itemFiles).forEach(item -> {
            if (item.isFile()) { files.add(item); }
            else if (item.isDirectory()) {
                List newItems = getFiles(item.getAbsolutePath());
                if (newItems != null) { files.addAll(newItems); }
            }
        });

        return files;
    }
    public static void readData (List<File> files) {
        files.forEach(file -> {
            Thread thread = new Thread(() -> {
                List<Thread> threads = new ArrayList<>(10);
                for (int i = 0; i < 10; i++) {
                    final int currentHash = i;
                    Thread reader = new Thread(() -> {
                        Connection mysqlConnector = MySQLConnector.getConnector();
                        String sql = "INSERT INTO reddit.comments(`id_str`, `parent_id`, `subreddit_id`, `link_id`, " +
                                "`author`, `name` , `ups`, `score`, `downs`, `gilded`, `retrieved_on`, `controversiality`, " +
                                "`body`, `distinguished`, `subreddit`, `removal_reason`, `author_flair_text`, " +
                                "`author_flair_css_class`, `archived`, `edited`, `score_hidden`, `created_utc`) " +
                                "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

                        GsonBuilder gsonBuilder = new GsonBuilder();
                        gsonBuilder.registerTypeAdapter(Timestamp.class, new TimestampTypeAdapter());
                        gsonBuilder.registerTypeAdapter(Integer.class, new BooleanTypeAddapter());
                        Gson gson = gsonBuilder.create();
                        int count = 10;
                        final int hash = currentHash;
                        SimpleDateFormat simpleDateFormat = new SimpleDateFormat("yyyy-MM-DD HH:mm:ss");
                        long startTime = System.currentTimeMillis();
                        long endTime = startTime;
                        System.out.println("[" + simpleDateFormat.format(startTime) + "];[file]" + file.getName() + ";[thread] "  + Thread.currentThread().getName() + " START");
                        int currentLine = 1, currentCount = 0, insertCount = 0;
                        BufferedReader bufferedReader = null;
                        try {
                            PreparedStatement pstm = mysqlConnector.prepareStatement(sql);
                            mysqlConnector.setAutoCommit(false);
                            bufferedReader = new BufferedReader(new InputStreamReader(new FileInputStream(file)));
                            for (String line = bufferedReader.readLine(); line != null; line = bufferedReader.readLine(), currentCount++) {
                                if (currentCount % count == hash) {
                                    Comment comment = gson.fromJson(line, Comment.class);
                                    try {
                                        pstm.setString(1, comment.getId());
                                        pstm.setString(2, comment.getParentId());
                                        pstm.setString(3, comment.getSubredditId());
                                        pstm.setString(4, comment.getLinkId());
                                        pstm.setString(5, comment.getAuthor());
                                        pstm.setString(6, comment.getName());
                                        pstm.setInt(7, comment.getUps());
                                        pstm.setInt(8, comment.getScore());
                                        pstm.setInt(9, comment.getDowns());
                                        pstm.setInt(10, comment.getGilded());
                                        pstm.setInt(11, comment.getRetrievedOn());
                                        pstm.setInt(12, comment.getControversiality());
                                        pstm.setString(13, comment.getBody());
                                        pstm.setString(14, comment.getDistinguished());
                                        pstm.setString(15, comment.getSubreddit());
                                        pstm.setString(16, comment.getRemovalReason());
                                        pstm.setString(17, comment.getAuthorFlairText());
                                        pstm.setString(18, comment.getAuthorFlairCssClass());
                                        pstm.setInt(19, comment.getArchived());
                                        pstm.setInt(20, comment.getEdited());
                                        pstm.setInt(21, comment.getScoreHidden());
                                        pstm.setTimestamp(22, comment.getCreatedUtc());
                                        pstm.execute();
                                        currentLine++;
                                        insertCount++;
                                    } catch (SQLException e) {
                                        if (Integer.parseInt(e.getSQLState()) != 23000) {
                                            System.exit(-4);
                                        }
                                        System.err.println("error in sql:" + e.getMessage() + "[code]" + e.getErrorCode());
                                    }
                                }
                                if ((currentLine %= 1000) == 0) {
                                    try {
                                        mysqlConnector.commit();
                                    } catch (SQLException e) {
                                        System.err.println("[commit error]" + e.getMessage() + ";[code]" + e.getSQLState());
                                        System.exit(-5);
                                    }
                                    endTime = System.currentTimeMillis();
                                    System.out.println("[" + simpleDateFormat.format(endTime) + "];[file]" + file.getName() + ";[thread] "  + Thread.currentThread().getName() + "[INSERT COUNT]: " + currentCount);
                                }
                            }

                        }catch (IOException | SQLException e) {
                            System.err.println("read file io error:" + e.getMessage());
                            System.exit(-2);
                        } finally {
                            try {
                                bufferedReader.close();
                                mysqlConnector.close();
                            } catch (SQLException | IOException e) {
                                e.printStackTrace();
                            }
                        }
                        endTime = System.currentTimeMillis();
                        System.out.println("[" + simpleDateFormat.format(endTime) + "];[file]" + file.getName() + ";[thread] "  + Thread.currentThread().getName() + "[insertCount]: " + insertCount);
                        System.out.println("[thread] "  + Thread.currentThread().getName() + "[insertCount]: " + insertCount + "; END; [duration]" + (endTime - startTime) % 1000 + "s");
                    }, "file_reader-"+file.getName() + "-id-" + currentHash);
                    threads.add(reader);
                }
                threads.forEach(Thread::start);

            }, "thread-" + file.getName());
            thread.start();
        });
    }

}
