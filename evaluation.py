import utils

if __name__ == '__main__':
    endpoint = 'https://backend.dblp-july-2025.skynet.coypu.org'
    sparql = """PREFIX dblp: <https://dblp.org/rdf/schema#>
            SELECT ?paper ?title ?year WHERE {
              ?paper dblp:title ?title .
              ?paper dblp:publishedIn "SIGIR" .
              ?paper dblp:yearOfPublication ?year
            }
            ORDER BY DESC(?year)
            LIMIT 10    
    """
    result = utils.run_sparql_query(sparql_endpoint=endpoint,sparql_query=sparql)
    print(utils.extruct_values(result))