Execute the following command in the current directory:
python menu.py

This will take you to a menu where you can select one of the options repeatedly until you choose to exit.

Applying NLP to Online News Articles

1. Collecting data:

Data was gather by crawling and scraping several online news portals (The Hindu, TOI etc.). Links were followed, proceeding only if the newly mined link was novel and met certain criteria (for example: chiefly sections focusing on national and international news were included in the search) Data was retrieved from links identified as being news articles (patterns were identified during a preliminary investigation that indicated that the link contained a news article). The article was parsed into a python dictionary.


2. Judging popularity:

Similarity was used to build up counts for each article. The minimum was 0 and the maximum was 3, 1 for each portal(not counting source portal). The method used was cosine-similarity. I used a threshold of 0.4. I arrived at that
number through trial and error, playing around with the texts and judging the results subjectively. I found that a score of 0.4 was an optimal point because it usually identified two articles on the same subject to be related (and hence, a part of the same news story) but did not lead to many false positives.

The count increments for each story once for 1 newspaper, once a match is found in a newspaper, further matches are discarded. To identify the most popular article (just any one article with the maximum score; if multiple articles have the maximum, the first will be retained) the algorithm came up with a reasonable choice.

3. Judging positive/negative valence

A Naive Bayes Classifier was used to judge whether a news story is negative or positive. A data set consisting of labeled (negative/positive) movie reviews was used as training data.
