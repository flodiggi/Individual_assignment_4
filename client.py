# -*- coding: utf-8 -*-


#%%
import requests

localhost = "http://127.0.0.1:5000"

#graph examples: Like in LinkedIn, each edge, is listed as a node again

graph1 = {
        "a": ["b","c","z"],
        "b": ["a","d"],
        "c": ["a","d"],
        "d": ["b","e",],
        "e":["d"],
        "f":[],
        "z":["a"]
        }

graph2 = {"a":["b"]}

graph3 = {}

graph_false = ["a","b","c"] #dataformatnotallowed



#%%

def upload_graph(graph):
    url = localhost+"/graph/upload"
    data = graph
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json() 
    else:
        return response.status_code
    
    
def get_currentgraph():
    response = requests.get(localhost+"/graph")
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code      


def get_degrees_of_separation(origin,destination):
    response = requests.get(localhost+"/degrees_of_separation/"+origin+"/"+destination)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code
    





