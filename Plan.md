# Rough draft 

## Backend 

### REST application 

Will use a FastAPI backend to handle all of our difficult logic and return the quote(s) of the day and clip if its a really famous one / thats possible. For example there are a bunch of different ways to represent a date: July 4th, Jul. 4th, Independence Day, dd/mm/yyyy, mm/dd/yyyy, etc. etc. The backend will handle all of this logic.


### Movie Quote Fetching
Doesn't seem like IMDB has an API for fetching movie quotes, need to come up with some way to get a LOT of movie quotes.

Some options: 
1. Scrape IMDB for quotes, most likely starting with https://www.imdb.com/chart/top/. Pro: ez pz, done something like this before for movie posters. Con: Limited to what we can scrape and popular quotes, not sure thats a con though. 
2. Hit some LLM and ask for a movie quote for today. Pro: So easy. Con: Prelimary testing shows that LLMs will lie to me and just make up movie quotes. 
3. Scrape full screen plays from [imsdb](https://imsdb.com/), maybe starting with the IMDB top 250 or letterboxed top 500, then parse only the quotes out of that. Pros: A significanly larger dataset so we are more likely to hit a quote with todays date. Cons: A lot more processing since the screenplays are not structured in a way that makes quotes obvious, the URL path for a movie can be less than ideal, movies don't usually match screenplays 1:1. 
4. Search [quodb](https://www.quodb.com/) for the date and then pull quotes from that. Pros: Larger dataset, easy to get. Cons: Usually just quote fragments would most likely need to enhance with screenplay.

Options 1 and 3 would most likely require a database. 

## Frontend
Need a simple homepage that is well styled and displays the quote of the day / if we can fetch a clip showing the quote, the clip. Probably going to over engineer this with react + mantine. 
