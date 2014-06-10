register 'lib/elephant-bird-core-4.1.jar';
register 'lib/elephant-bird-pig-4.1.jar';
register 'lib/elephant-bird-hadoop-compat-4.1.jar';
register 'lib/json-simple-1.1.jar';
register 'lib/google-collections-1.0.jar';
register 'pig-0.11.1/pig-0.11.1.jar';

--load business
business = LOAD 'dataset/business.json' USING com.twitter.elephantbird.pig.load.JsonLoader('nestedLoad') AS raw;

--Select business_id and categories from each row
fields = FOREACH business GENERATE raw#'business_id' AS business_id,
                                raw#'categories' AS categories;

--filter out empty categories
fltr_fields = FILTER fields BY categories IS NOT NULL;

--store into a file
STORE fltr_fields INTO 'business_tags' USING PigStorage('\t');
~                                                                       
