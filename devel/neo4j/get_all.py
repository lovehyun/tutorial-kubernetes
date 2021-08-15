# pip install neo4j
# pip install kubernetes
from kubernetes import client, config
import json
import logging
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
 
class App:
 
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
 
    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()
 
    def create_node(self, object_name, node_name):
        with self.driver.session() as session:
            session.write_transaction(self._create_node, object_name, node_name)
 
    @staticmethod
    def _create_node(tx, object_name, node_name):
        if object_name == "service":
            query = ("MERGE (:service { name: $node_name }) ")
        elif object_name == "deployment":
            query = ("MERGE (:deployment { name: $node_name }) ")
        elif object_name == "replicaset":
            query = ("MERGE (:replicaret { name: $node_name }) ")
        elif object_name == "pod":
            query = ("MERGE (:pod { name: $node_name }) ")
        if object_name != "":
            tx.run(query, object_name=object_name, node_name=node_name)
 
    def create_relation(self, first_node, second_node):
        with self.driver.session() as session:
            session.write_transaction(self._create_relation, first_node, second_node)
 
    @staticmethod
    def _create_relation(tx, first_node, second_node):
        query = (
            "MATCH (a), (b) "
            "WHERE a.name = $first_node and b.name = $second_node "
            "MERGE (a)-[:relation_to]->(b) "
        )
        tx.run(query, first_node=first_node, second_node=second_node)
 
 
def main(app):
    # kubectl describe secret default-token-xxxxx -n kube-public
    # kubectl describe secret neo4j-sa-token-xxxxx
    # aToken = "(token from 'kubectl describe secret neo4j-sa-token-xxxxx')"
    aConfiguration = client.Configuration()
    # K8s
    # aConfiguration.host = "https://127.0.0.1:6443"
    # MiniKube with proxy
    aConfiguration.host = "http://127.0.0.1:8080"

    aConfiguration.verify_ssl = False
    aConfiguration.api_key = {"authorization": "Bearer " + aToken}
    aApiClient = client.ApiClient(aConfiguration)
 
    v1 = client.CoreV1Api(aApiClient)
    v2 = client.AppsV1Api(aApiClient)
    v4 = v1.list_service_for_all_namespaces(watch=False)
    v5 = v2.list_deployment_for_all_namespaces(watch=False)
    v6 = v2.list_replica_set_for_all_namespaces(watch=False)
 
    service_dict = {}
    deployment_dict = {}
    replica_set_dict = {}
 
    for i in v4.items:
        selector = i.spec.selector
        if selector == None:
            continue
        for key, value in selector.items():
            temp = '%s=%s' % (key, value)
            service_dict[temp] = i
    for i in v5.items:
        selector = i.spec.selector.match_labels
        if selector == None:
            continue
        for key, value in selector.items():
            temp = '%s=%s' % (key, value)
            deployment_dict[temp] = i
    for i in v6.items:
        selector = i.spec.selector.match_labels
        if selector == None:
            continue
        for key, value in selector.items():
            temp = '%s=%s' % (key, value)
            replica_set_dict[temp] = i
 
    v7 = v1.list_namespaced_pod("default")
 
    for i in v7.items:
        labels = ""
        for key, value in i.metadata.labels.items():
            labels = '%s=%s' % (key, value)
            break
        app.create_node('pod', i.metadata.name)
        if labels in service_dict.keys():
            app.create_node('service', service_dict[labels].metadata.name)
            app.create_relation(service_dict[labels].metadata.name, i.metadata.name)
        if labels in deployment_dict.keys():
            app.create_node('deployment', deployment_dict[labels].metadata.name)
            app.create_node('replicaset', replica_set_dict[labels].metadata.name)
            app.create_relation(deployment_dict[labels].metadata.name, replica_set_dict[labels].metadata.name)
            app.create_relation(replica_set_dict[labels].metadata.name, i.metadata.name)

 
if __name__ == '__main__':
    scheme = "neo4j"
    host_name = "127.0.0.1"
    port = 7687
    url = "{scheme}://{host_name}:{port}".format(scheme=scheme, host_name=host_name, port=port)
    user = "neo4j"
    password = ""
    app = App(url, user, password)
    main(app)
    app.close()
