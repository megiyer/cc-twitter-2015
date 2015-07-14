### Insight Data Engineering - Coding Challenge - 2015
#### https://github.com/InsightDataScience/cc-example/   
======================================================== 
#### Implemented two features to analyze tweets:

- Feature 1. Calculated the total number of times each word has been tweeted.
- Feature 2. Calculated the median number of *unique* words per tweet, and update this median as tweets come in. 

### Directory structure:

    ├── README.md  
	├── run.sh  				   --> Script that runs the program "analyze_tweets.py"
	├── src  
	│    └── analyze_tweets.py   --> Solution for Coding Challenge    
	├── tweet_input  
	│    └── tweets.txt  
	│── tweet_output  
	│    ├── ft1.txt  
	│    └── ft2.txt  
	└── test  
		 ├── tweets_test.py     --> Generates (a) random input file for testing (b) expected output files
		 ├── tweets_random.txt
		 ├── ft1_expected.txt  
		 ├── ft1_expected.txt  
		 └── test.sh  		  --> Script that runs "tweets_test.py" & "analyze_tweets.py" , and diffs their outputs
		 

#### Implementation
 
- Programming Language: Python  
- Library: Python Standard Library
- Imports: collections.defaultdict, heapq

#### Design:

- (Feature 1) Hashtable is used to keep a count of tweeted words.
- (Feature 2) Two heaps are used to record running median of unique number of words per tweet. 
 	

#### Testing: 

- Done on Mac 2.6GHz Intel Core i7 processor with 16GB memory
- Test results for large data were:
   - When tested on 1 million records (~115 MB file), solution runs in ~  21 seconds
   - When tested on 10 million records (~1.1 GB file), solution runs in ~ 220 seconds

#### Assumptions (based on challenge's README):

1. Assumed input file is 'tweets.txt' inside 'tweet_input' folder. Output is written to 'ft1.txt' and 'ft2.txt' in 'tweet_output' folder. 
2. Assumed that all of the files in the input directory are standard text files. 
3. Assumed that each tweet only contains lowercase letters, numbers, and ASCII characters like ':', '@', and '#'. 
4. Assumed that all punctuation is treated as part of the word itself, so 'business.' would be counted as a different word than 'business' without the period.
5. Assumed that all of the characters are ASCII characters (no Unicode).
6. Assumed that each new line of the text file corresponds to a new tweet. 
7. Assumed that all the tweets contain at least one word. A word in a tweet is defined as anything separated by whitespace.
8. Assumed that code is tested on a single machine, hence distributed technologies like Hadoop or Spark are not leveraged.





