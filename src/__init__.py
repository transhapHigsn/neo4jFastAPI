from neo4j import GraphDatabase
from config import get_config

driver = GraphDatabase.driver(
	get_config('neo4j', 'uri'),
	auth=(
		get_config('neo4j', 'username'),
		get_config('neo4j', 'password')
	)
)
