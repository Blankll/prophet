package com.blank.prophet.utils;

import com.google.gson.*;

import java.lang.reflect.Type;

public class BooleanTypeAddapter implements JsonSerializer<Boolean>, JsonDeserializer<Integer>{
    public JsonElement serialize(Boolean ts, Type t, JsonSerializationContext jsc) {
        return new JsonPrimitive(ts);
    }
    public Integer deserialize(JsonElement json, Type t, JsonDeserializationContext jsc) throws JsonParseException {
        if (!(json instanceof JsonPrimitive)) {
            throw new JsonParseException("The date should be a string value");
        }
        Integer value = null;
        try {
            value = Integer.parseInt(json.getAsString());
            return value;
        } catch (Exception e) { }

        boolean item = json.getAsBoolean();
        return item ? 1 : 0;
    }
}
