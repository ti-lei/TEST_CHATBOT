from urllib.parse import parse_qsl

query_string = "key1=value1&key2=value2&key3=value3"
parameters = parse_qsl(query_string)
print(type(parameters))
for key, value in parameters:
    print(key, value)