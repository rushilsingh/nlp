### How to run:

- Execute the following commands to prepare a clean environment:
```
make clean
make prepare-venv
```

- Afterwards, source the virtual environment:

```
source env/bin/activate
```

- Lastly, launch the agent menu by running the following command:

```
python menu.py
```

### Development Report 

- Applying NLP to Online News Articles


- Collecting data:

Data was gather by crawling and scraping several online news portals (The Hindu,

TOI etc.). Links were followed, proceeding only if the newly mined link was novel

and met certain criteria (for example: chiefly sections focusing on national and

international news were included in the search)

Data was retrieved from links identified as being news articles (patterns were

identified during a preliminary investigation that indicated that the link contained a

news article). The article was parsed into a python dictionary.


- Judging popularity:


Used similarity to build up counts for each article. The minimum

was 0 and the maximum was 3, 1 for each portal(not counting source portal).

The method used was cosine-similarity. Used a threshold of 0.4. Arrived at that

number through trial and error, playing around with the texts and judging the results

subjectively. Found that a score of 0.4 was an optimal point because it usually

identified two articles on the same subject to be related (and hence, a part of the same

news story) but did not lead to many false positives. 


- Judging positive/negative valence


A Naive Bayes Classifier was used to judge whether a news story is negative or

positive. A data set consisting of labeled (negative/positive) movie reviews was used

as training data.
