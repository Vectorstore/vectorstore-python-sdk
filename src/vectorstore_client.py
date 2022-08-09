import requests


class Item:
    # item_id is uint32 type,
    def __init__(self, item_id, vector, metadata):
        self.item_id = item_id
        self.vector = vector
        self.metadata = metadata


# API Reference: https://docs.google.com/document/d/1kwZr28YJa_baLFfd3ii2dvnHzY__rwCg1KiUq3QPeJU/edit?usp=sharing
class VectorstoreClient:
    def __init__(self, host_name, api_key):
        self.host_name = host_name
        self.headers = {"api_key": api_key, 'Content-type': 'application/json'}

    # Link: https://docs.google.com/document/d/1kwZr28YJa_baLFfd3ii2dvnHzY__rwCg1KiUq3QPeJU/edit#heading=h.r3ld8u9wfcqr
    def create_index(self, index_name, dimension, max_num_vectors):
        create_index_endpoint = self.host_name + "/create_index"
        data = {
            "index_name": index_name,
            "dimension": dimension,
            "max_num_vectors": max_num_vectors
        }

        return requests.post(create_index_endpoint, headers=self.headers, json=data)

    # Link: https://docs.google.com/document/d/1kwZr28YJa_baLFfd3ii2dvnHzY__rwCg1KiUq3QPeJU/edit#heading=h.xlmif9wuvdd0
    def delete_index(self, index_name):
        delete_index_endpoint = self.host_name + "/delete_index"
        data = {
            "index_name": index_name
        }

        return requests.post(delete_index_endpoint, headers=self.headers, json=data)

    # Link: https://docs.google.com/document/d/1kwZr28YJa_baLFfd3ii2dvnHzY__rwCg1KiUq3QPeJU/edit#heading=h.fv2axfumuzbr
    def index_item(self, index_name, item):
        index_item_endpoint = self.host_name + "/index_item"
        data = {
            "index_name": index_name,
            "item_id": item.item_id,
            "vector": item.vector,
            "metadata": item.metadata
        }

        return requests.post(index_item_endpoint, headers=self.headers, json=data)

    # Link: https://docs.google.com/document/d/1N_a7PEYJrMRxfyYGg0D4ii2LctyJHM5jwc41txaY-zs/edit#heading=h.zd6oyf32g7bx
    def batch_index_item(self, index_name, items):
        batch_index_item_endpoint = self.host_name + "/batch_index_items"
        data_items = []
        for item in items:
            data_items.append({
                "item_id": item.item_id,
                "vector": item.vector,
                "metadata": item.metadata
            })
        data = {
            "index_name": index_name,
            "items": data_items
        }
        return requests.post(batch_index_item_endpoint, headers=self.headers, json=data)

    # Link: https://docs.google.com/document/d/1kwZr28YJa_baLFfd3ii2dvnHzY__rwCg1KiUq3QPeJU/edit#heading=h.a2qlw4xxor4i
    def query(self, index_name, vector, size, filter_expr=""):
        query_endpoint = self.host_name + "/query"
        data = {
            "index_name": index_name,
            "vector": vector,
            "size": size,
            "filter_expr": filter_expr
        }

        return requests.post(query_endpoint, headers=self.headers, json=data)

    # Link: https://docs.google.com/document/d/1kwZr28YJa_baLFfd3ii2dvnHzY__rwCg1KiUq3QPeJU/edit#heading=h.b1mkdu4inp2w
    def index_stats(self, index_name):
        index_stats_endpoint = self.host_name + "/index_stats"
        data = {
            "index_name": index_name
        }

        return requests.post(index_stats_endpoint, headers=self.headers, json=data)

    # Link: https://docs.google.com/document/d/1kwZr28YJa_baLFfd3ii2dvnHzY__rwCg1KiUq3QPeJU/edit#heading=h.4v4ov79yb52s
    def list_indexes(self):
        list_indexes_endpoint = self.host_name + "/list_indexes"
        return requests.post(list_indexes_endpoint, headers=self.headers)
