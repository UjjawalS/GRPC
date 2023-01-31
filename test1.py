from GRPC.pmpclient.source.resource import Resource

if __name__ == '__main__':
    res = Resource()
    result = res.create_resource(resource_name="Ramakrish14",resource_type="windows",account_name="Richa",pass_word="SankarRaj",notes="here is new acc")
    print(f'{result}')
 