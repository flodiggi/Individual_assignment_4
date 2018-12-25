# -*- coding: utf-8 -*-

#%%

#%%
from flask import Flask, jsonify, request



server = Flask("Graph server ")

usergraph = {"currentusergraph": None}

    

@server.route("/graph/upload", methods = ["POST"])
def graph_upload():
    body = request.get_json()
    if type(body) == dict:
        values = body.values()
        for i in values:
            #allows empty dictionaries to be posted, but checks for valid format if not empty
            if type(i) != list:
                return jsonify({"message":"Graph not posted, please upload a valid graph as a dictionary. Edges for each node have to be in a list"})
        usergraph["currentusergraph"] = body
        return jsonify({"message":"Graph posted", "data":usergraph})
    return jsonify({"message":"Graph not posted, please upload a valid graph as a dictionary. Edges for each node have to be in a list"})


@server.route("/graph")
def graph_handler():
    if usergraph["currentusergraph"] == None:
        return jsonify({"message":"Please upload a graph", "data":None})
    return jsonify({"message":"Current Graph", "data":usergraph})

#%%

#Closest path/degree is required, hence all possible paths need to be found first

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for conn in graph[start]:
        if conn not in path:
            newpaths = find_all_paths(graph, conn, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

#Degrees are defined as in  Linkedin (I am one degree away from myself += 1 for each additional node--- not connected nodes will return None)

def degrees_of_separation(graph, start, end):
    all_paths = find_all_paths(graph, start, end)
    degrees = None
    for path in all_paths:
        steps = 0
        for step in path:
            steps += 1
        if degrees is None or steps < degrees:
            degrees = steps   
    return degrees 

def hello(a,b):
    return a

#%%   



@server.route("/degrees_of_separation/<origin>/<destination>")
def degrees_handler(origin, destination):
    if usergraph["currentusergraph"] == None:
        return jsonify({"message":"Please upload a graph first", "data":None})
    else:
        degrees = degrees_of_separation(usergraph["currentusergraph"], origin, destination)
        if degrees == None:
            return jsonify({"message":"Origin and Destination are not connected!","degrees_of_separation":degrees,"origin":origin, "destination":destination})
        return jsonify({"message":"Degrees of separation for Current Graph", "degrees_of_separation":degrees,"origin":origin, "destination":destination})





server.run()