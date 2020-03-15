import json

# create a dictionary to store credentials

twitter_cred = dict()

twitter_cred['CONSUMER_KEY'] = 'X6eRSFIzQ7A8GX8EKS6pjNsVF'
twitter_cred['CONSUMER_SECRET'] = 'UcpNwe39JqQ83zdigXA7fLqSfFAFlc4k15eCRW2vL7upuAdhLX'
twitter_cred['ACCESS_KEY'] = '740559384380604417-SLDNlS5cjZMhBzbEFsKTKKaISdehZGL'
twitter_cred['ACCESS_SECRET'] = 'Iy1MbQwla7mebPV3kPAo417xfP7acsNOxR0g7XydHMzLa'

with open('twitter_credentials.json', 'w') as secret_info:
    json.dump(twitter_cred, secret_info, indent=4, sort_keys=True)


print("done")
