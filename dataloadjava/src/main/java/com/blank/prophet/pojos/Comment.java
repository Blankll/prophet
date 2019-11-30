package com.blank.prophet.pojos;

import com.google.gson.annotations.SerializedName;

import java.sql.Timestamp;

public class Comment {
    private String id;
    @SerializedName("parent_id")
    private String parentId;
    @SerializedName("subreddit_id")
    private String subredditId;
    @SerializedName("link_id")
    private String linkId;
    private String author;
    private String name;
    private Integer ups;
    private Integer score;
    private Integer downs;
    private Integer gilded;
    @SerializedName("retrieved_on")
    private Integer retrievedOn;
    private Integer controversiality;
    private String body;
    private String distinguished;
    private String subreddit;
    private String removalReason;
    @SerializedName("author_flair_text")
    private String authorFlairText;
    @SerializedName("author_flair_css_class")
    private String authorFlairCssClass;
    private Integer archived;
    private Integer edited;
    @SerializedName("score_hidden")
    private Integer scoreHidden;
    @SerializedName("created_utc")
    private Timestamp createdUtc;


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getParentId() {
        return parentId;
    }

    public void setParentId(String parentId) {
        this.parentId = parentId;
    }

    public String getSubredditId() {
        return subredditId;
    }

    public void setSubredditId(String subredditId) {
        this.subredditId = subredditId;
    }

    public String getLinkId() {
        return linkId;
    }

    public void setLinkId(String linkId) {
        this.linkId = linkId;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getUps() {
        return ups;
    }

    public void setUps(Integer ups) {
        this.ups = ups;
    }

    public Integer getScore() {
        return score;
    }

    public void setScore(Integer score) {
        this.score = score;
    }

    public Integer getDowns() {
        return downs;
    }

    public void setDowns(Integer downs) {
        this.downs = downs;
    }

    public Integer getGilded() {
        return gilded;
    }

    public void setGilded(Integer gilded) {
        this.gilded = gilded;
    }

    public Integer getRetrievedOn() {
        return retrievedOn;
    }

    public void setRetrievedOn(Integer retrievedOn) {
        this.retrievedOn = retrievedOn;
    }

    public Integer getControversiality() {
        return controversiality;
    }

    public void setControversiality(Integer controversiality) {
        this.controversiality = controversiality;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public String getDistinguished() {
        return distinguished;
    }

    public void setDistinguished(String distinguished) {
        this.distinguished = distinguished;
    }

    public String getSubreddit() {
        return subreddit;
    }

    public void setSubreddit(String subreddit) {
        this.subreddit = subreddit;
    }

    public String getRemovalReason() {
        return removalReason;
    }

    public void setRemovalReason(String removalReason) {
        this.removalReason = removalReason;
    }

    public String getAuthorFlairText() {
        return authorFlairText;
    }

    public void setAuthorFlairText(String authorFlairText) {
        this.authorFlairText = authorFlairText;
    }

    public String getAuthorFlairCssClass() {
        return authorFlairCssClass;
    }

    public void setAuthorFlairCssClass(String authorFlairCssClass) {
        this.authorFlairCssClass = authorFlairCssClass;
    }

    public Integer getArchived() {
        return archived;
    }

    public void setArchived(Integer archived) {
        this.archived = archived;
    }

    public Integer getEdited() {
        return edited;
    }

    public void setEdited(Integer edited) {
        this.edited = edited;
    }

    public Integer getScoreHidden() {
        return scoreHidden;
    }

    public void setScoreHidden(Integer scoreHidden) {
        this.scoreHidden = scoreHidden;
    }

    public Timestamp getCreatedUtc() {
        return createdUtc;
    }

    public void setCreatedUtc(Timestamp createdUtc) {
        this.createdUtc = createdUtc;
    }
}