register 'elephant-bird-core-4.1.jar';
register 'elephant-bird-pig-4.1.jar';
register 'elephant-bird-hadoop-compat-4.1.jar';
register 'json-simple-1.1.jar';
register 'google-collections-1.0.jar';
register 'pig-0.11.1/pig-0.11.1.jar';

--Loading  data
--load review
review_data = LOAD 'review.json' using com.twitter.elephantbird.pig.load.JsonLoader('-nestedLoad');


--select business_id, ratings and review
cols_review = FOREACH review_data GENERATE
        $0#'business_id' AS business_id,
	$0#'stars' AS ratings,
        REPLACE($0#'text','\n+',' ') AS review;

--remove empty rows
cln_reviews = FILTER cols_review  BY business_id IS NOT NULL;

STORE cln_reviews INTO 'review_rating' USING PigStorage(':');
