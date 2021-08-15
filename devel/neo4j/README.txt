# Kubernetes API 접속
https://kubernetes.io/ko/docs/tasks/administer-cluster/access-cluster-api/
https://kubernetes.io/ko/docs/tasks/administer-cluster/access-cluster-api/#rest-api%EC%97%90-%EC%A7%81%EC%A0%91-%EC%A0%91%EA%B7%BC


kubectl proxy --port=8080 &
curl http://localhost:8080/api/

Output
{
  "versions": [
    "v1"
  ],
  "serverAddressByClientCIDRs": [
    {
      "clientCIDR": "0.0.0.0/0",
      "serverAddress": "10.0.1.149:443"
    }
  ]
}


==============================================================================

# GraphDB - Neo4j
https://neo4j.com/developer/get-started/


# 도커 이미지로 Neo4j 설치
docker run -p7474:7474 -p7687:7687 -e NEO4J_AUTH=neo4j/s3cr3t neo4j
# then open http://localhost:7474 to connect with Neo4j Browser


# 호스트에 Neo4j 설치
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -
sudo add-apt-repository "deb https://debian.neo4j.com stable 4.1"
sudo apt install neo4j
sudo systemctl enable neo4j.service
sudo systemctl status neo4j.service


# Neo4j 설정
cypher-shell

cypher-shell prompt
username: neo4j
password: *****     <-- neo4j
Password change required
new password: ********************
Connected to Neo4j 4.1.0 at neo4j://localhost:7687 as user neo4j.
Type :help for a list of available commands or :exit to exit the shell.
Note that Cypher queries must end with a semicolon.
neo4j@neo4j>


# Neo4j Remote접속 설정
sudo nano /etc/neo4j/neo4j.conf

. . .
#*****************************************************************
# Network connector configuration
#*****************************************************************

# With default configuration Neo4j only accepts local connections.
# To accept non-local connections, uncomment this line:
dbms.default_listen_address=0.0.0.0
. . .


cypher-shell -a 'neo4j://your_hostname:7687'

neo4j@neo4j> CREATE (:Shark {name: 'Great White'});


neo4j@neo4j> CREATE
neo4j@neo4j> (:Shark {name: 'Hammerhead'})-[:FRIEND]->
neo4j@neo4j> (:Shark {name: 'Sammy'})-[:FRIEND]->
neo4j@neo4j> (:Shark {name: 'Megalodon'});

neo4j@neo4j> MATCH (a:Shark),(b:Shark)
neo4j@neo4j> WHERE a.name = 'Sammy' AND b.name = 'Megalodon'
neo4j@neo4j> CREATE (a)-[r:ORDER { name: 'Lamniformes' }]->(b)
neo4j@neo4j> RETURN type(r), r.name;

Output
+-------------------------+
| type(r) | r.name        |
+-------------------------+
| "ORDER" | "Lamniformes" |
+-------------------------+

neo4j@neo4j> MATCH (a:Shark),(b:Shark)
neo4j@neo4j> WHERE a.name = 'Sammy' AND b.name = 'Hammerhead'
neo4j@neo4j> CREATE (a)-[r:SUPERORDER { name: 'Selachimorpha'}]->(b)
neo4j@neo4j> RETURN type(r), r.name;

Output
+--------------------------------+
| type(r)      | r.name          |
+--------------------------------+
| "SUPERORDER" | "Selachimorpha" |
+--------------------------------+

neo4j@neo4j> MATCH (a)-[r]->(b)
neo4j@neo4j> RETURN a.name,r,b.name
neo4j@neo4j> ORDER BY r;

Output
+---------------------------------------------------------------------+
| a.name       | r                                     | b.name       |
+---------------------------------------------------------------------+
| "Hammerhead" | [:FRIEND]                             | "Sammy"      |
| "Sammy"      | [:FRIEND]                             | "Megalodon"  |
| "Sammy"      | [:ORDER {name: "Lamniformes"}]        | "Megalodon"  |
| "Sammy"      | [:SUPERORDER {name: "Selachimorpha"}] | "Hammerhead" |
+---------------------------------------------------------------------+


