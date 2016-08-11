import keycdn


def run_test():
    keycdn = keycdn.Api('sk_prod_Y2MzN2RkZjQ1MzgxNTRkNzU2')

    # returns dict object
    print(keycdn.get('zones.json'))

    result = keycdn.post('zones/37861.json', {'gzip': 'disabled'})
    if result['status'] == 'success':
        print('Successfully renamed zone')
    else:
        print('Did not have success')

if __name__ == '__main__':
    run_test()
