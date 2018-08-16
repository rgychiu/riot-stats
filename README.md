# Riot Stats
Application making use of the Riot Games API and statistics. Using the Riot's
developer portal, the web application will analyze the data and display statistics
ranging from matchup win rates, counter-picks, common runes, and more.

###Project Setup
In order to get started with using the API Developer Portal and the Harvesters, 
first clone the repository:
```
https://github.com/rgychiu/riot-stats.git
```

Using the Riot API also requires an API key, which can be obtained through
their website: 
```
https://developer.riotgames.com/
```

A League of Legends account can also be used rather than creating an account
if it exists.

Navigate towards the account profile and copy the API key, or regenerate the
key and copy it if it's expired. After copying the API key, create a file
named ```credentials.json``` under the parent directory and copy the following 
JSON into the file:
```
{
    "api_key": "YOUR_API_KEY_HERE"
}
```
**Note that the API Key also needs to be within a pair of double quotes.
The credentials.json file is also not included in the repository to ensure
the privacy of the API Key**

After copying the API Key in the JSON file, the project should be setup and
ready for use.