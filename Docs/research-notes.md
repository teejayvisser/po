Task Overview:  
 
Your task is to create a Python script that performs the following actions:  
 
1. Fetch data from the Pokédex API: You'll use the Pokédex API to retrieve information about various Pokémon species. The API documentation. Pokédex API Documentation, is readily available online.  
2. Process the data: Extract relevant information about each Pokémon from the API response. This information may include the Pokémon's name, type(s), abilities, and any other relevant data.  
3. Categorize Pokémon: Based on the information retrieved, categorize each Pokémon into different types. For example, categorize them as Water, Fire, Grass, Electric, etc., based on their primary or secondary types.  
4. Display the results: Display the list of Pokémon categories along with the names of Pokémon belonging to each category.

PokeAPI: [Link](https://pokeapi.co/ "https://pokeapi.co/") | [Docs](https://pokeapi.co/docs/v2 "https://pokeapi.co/docs/v2")  
 
Requirements:  
 
1. Use Python 3.x for your solution.  
2. Utilize the requests library to make API calls.  
3. Organize your code into functions for better readability and maintainability.  
4. Ensure your code is well-commented and follows best practices.


steps needed for data seed


1. create data layer for api calls using request api - python does not require the same scaffolding as c#
2. create relational db(in memory or docker instance?) for all tables associated with pokemon - not doing this as taking everything into a temp db may be overkill 
3. create data iterator to get all pokemon (cycle and store till done) - no db to store in will be stored in local variables instead
4. create data iterator to get all pokemon linked data data by pokemon id (only required to run once) - this changed as the beginning methodology no longer calls all pokemon
5. create data layer to access my db - no db not necessary
6. create manager layer for filter calls / categories 
7. create docker compose to run everything - not necessary as it is only teh script now 
8. unit tests? 



notes of places to look for (links)
~https://www.sqlite.org/inmemorydb.html
~https://stackoverflow.com/questions/62333314/python-sqlalchemy-in-memory-database-connect
~https://memgraph.com/blog/in-memory-databases-that-work-great-with-python
~https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/
~


concerns

~how to display data after fetched - show in terminal / save to json
~does an in memory db actually persist the data while the app is running - opted not to use in memory with time constraints as well as slow performance
~do i create a front end - no
~do i create docker containers with a compose in order to spin everything up together - only in the event a db container is required otherwise may be pointless 
~do i use django / flask in this dev showcase? - no opted to keep is simple 
~https://gist.github.com/ruimaranhao/4e18cbe3dad6f68040c32ed6709090a3