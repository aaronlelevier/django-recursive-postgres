# Django Postgres Recursive

This add-on ads support for Recursive Queries in Postgres with the Django ORM.

# Requirements

- Python 3.6
- Django 2.0
- psycopg2-binary

# Current functionality

The current recursive queries will return the full unidirectional graph in a single direction, per the `UniDirectionalManager.in_nodes` or `UniDirectionalManager.out_nodes` methods.

# Roadmap

Add the ability to filter query results by:

- standard SQL `WHERE` filter clause on the Django Model (no filtering on related Models, yet...)
- depth filtering - Graph algorithms usually provide some sort of dept filtering

	- i.e. give me the related nodes of depth 1-3 where "x" is true

`Managers` for the 2 other types of Graphs:

- [Bidirected Graph](https://en.wikipedia.org/wiki/Bidirected_graph)

	- Graph node edges can be incoming and outgoing between the same two nodes
	- example: Twitter - a User can be following and followed by the another User
- [Undirected Graph](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)#Undirected_graph)

	- Graph nodes are connected, but have no direction
	- example: LinkedIn - Users have connections, but there is no direction between the connections

TBD

- potentially other Graph types, [DAG - Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) for example
