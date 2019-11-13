#!/bin/sh

cd src/config
touch dev_.ini
echo '[neo_4j]' > dev_.ini
echo 'uri=bolt://localhost:7687' >> dev_.ini
echo 'username=neo4j' >> dev_.ini
echo 'password=test' >> dev_.ini 