user1 = {'name': 'Harrison',

         'valid': True}

user2 = {'name': 'Wekesa',

         'valid': False}


def authenticated(fn):
    def wrappers(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
        else:
            print('request invalid')
    return(wrappers)  # code here


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
message_friends(user2)
