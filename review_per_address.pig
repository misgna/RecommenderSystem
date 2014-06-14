register '/home/haile/bigData/lib/elephant-bird-core-4.1.jar';
register '/home/haile/bigData/lib/elephant-bird-pig-4.1.jar';
register '/home/haile/bigData/lib/elephant-bird-hadoop-compat-4.1.jar';
register '/home/haile/bigData/lib/json-simple-1.1.jar';
register '/home/haile/bigData/lib/google-collections-1.0.jar';
register '/home/haile/bigData/pig-0.11.1/pig-0.11.1.jar';


--Loading  data
--load review
review = load 'review.json' using com.twitter.elephantbird.pig.load.JsonLoader('-nestedLoad');

--load business
business = load 'business.json' using com.twitter.elephantbird.pig.load.JsonLoader('-nestedLoad');

--select id and text
user_profile = FOREACH review GENERATE
        $0#'business_id' AS user_business_id,
        REPLACE($0#'text','\n',' ') AS review;

--business profile
business_profile = FOREACH business GENERATE
        $0#'business_id' AS business_id,
       REGEX_EXTRACT(REPLACE($0#'full_address','\n',' '),'AZ \\d{5}',0) AS zipcode;

--join business and user and update user profile
user_profile = JOIN business_profile BY business_id LEFT, user_profile BY user_business_id;

--business tags and review
user_profile = FOREACH user_profile GENERATE STRSPLIT(zipcode, ' ').$1 AS zipcode, review AS review;

--filter user profile
fltr_user_profile = FILTER user_profile BY zipcode IS NOT NULL;

--group according to zip code
grp_user_profile = GROUP fltr_user_profile BY zipcode;

--display result
DUMP grp_user_profile;
