-- load libraries to read json dump
REGISTER '/share/lib/elephant-bird-core-4.1.jar';
REGISTER '/share/lib/elephant-bird-pig-4.1.jar';
REGISTER '/share/lib/elephant-bird-hadoop-compat-4.1.jar';
REGISTER '/share/lib/google-collections-1.0.jar';
REGISTER '/share/lib/json-simple-1.1.jar';
REGISTER '/usr/lib/hadoop/lib/hadoop-lzo-cdh4-0.4.15-gplextras.jar';


--avoid java.lang.OutOfMemoryError: Java heap space (execmode: -x local)
set io.sort.mb 10;
--Loading  data
--load user
user = load 'user.json' using com.twitter.elephantbird.pig.load.JsonLoader('-nestedLoad');

--collect business_id and tags
user_reputation = FOREACH user GENERATE
        $0#'user_id' AS user_id,
        $0#'votes'#'useful' AS useful_votes,
        $0#'review_count' AS review_count,
        $0#'average_stars' AS average_stars,
        --$0#'votes'#'funny' AS funny_votes,
        --$0#'votes'#'useful' AS useful_votes,
        --$0#'votes'#'cool' AS cool_votes,
        --$0#'elite' AS elite,
        --$0#'compliments' AS compliments,
        $0#'fans' AS fans;

--sort user_reputation by funny_votes
user_reputation = ORDER user_reputation BY useful_votes DESC;

--display result
DUMP user_reputation;
