from urllib.parse import parse_qsl, urlparse

def set_query_field(url):

    
    return dict(parse_qsl((urlparse(url)).query))

url = "http://example.net?name=alex&school=anna"
res = set_query_field(url)
print(res)