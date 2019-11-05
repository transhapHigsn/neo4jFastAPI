# neo4jFastAPI  ![](https://github.com/transhaphigsn/neo4jFastAPI/workflows/Python%20application/badge.svg)
Fast API web server and Neo4j Graph Database back-end. 

# To get started
1. Add a dev.ini file inside config folder with following content. Assumption you have a neo4j instance running in background.
	```
	[neo4j]
	uri=<enter_link_to_test_db_here>
	username=<enter_test_username>
	password=<enter_test_password>
	```

	In order to setup neo4j database (on linux), use this:
	```
	sudo docker run \                                                      
    --name testneo4j \
    -p7474:7474 -p7687:7687 \
    -d \
    -v $HOME/neo4j/data:/data \
    --env NEO4J_AUTH=neo4j/test \
    neo4j:latest
	```

	Above command creates a `neo4j` docker container exposing ports `7474` and `7687`, and storing data at path `$HOME/neo4j/data` with database username as `neo4j` and password as `test`. For more info, [refer here](https://neo4j.com/developer/docker-run-neo4j/)

2. Create a virtualenv, you can use any of your choice. I prefer using virtualenv. 
	```
	python -m pip install virtualenv
	python -m virtualenv --python=python
	```

3. Install dependencies using this ```pip install -r requirements.txt```

3. Run command ```uvicorn src.main:app --reload``` to start FastAPI webserver.
