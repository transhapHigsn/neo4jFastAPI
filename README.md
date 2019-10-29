# neo4jFastAPI
Fast API web server and Neo4j Graph Database back-end. 

# To get started
1. Add a dev.ini file inside config folder with following content.
	```
	[neo4j]
	uri=<enter_link_to_test_db_here>
	username=<enter_test_username>
	password=<enter_test_password>
	```

2. Run command uvicorn main:app --reload