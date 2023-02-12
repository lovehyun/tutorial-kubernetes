# kubectl proxy --port=8888
from kubernetes import client

configuration = client.Configuration()
configuration.host = "127.0.0.1:8888"
api_client = client.ApiClient(configuration)

v1 = client.CoreV1Api(api_client)

print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
