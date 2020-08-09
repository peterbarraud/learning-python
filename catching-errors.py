try:
    print(1 + ' one')
except TypeError as te: # catching specific errors
    print('Type error: {}'.format(te))
except Exception as te: # the final catch-all
    print(te)