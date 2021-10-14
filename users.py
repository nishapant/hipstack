import pandas as pd
import string    
import random
from faker import Faker

user_data = []
S = 10 

usernames = []


for i in range(1000):
    fake = Faker()

    username = fake.simple_profile()['username']
    while (username in usernames):
        username = fake.simple_profile()['username']
    usernames.append(username)

    userpassword = fake.password(length=12)

    useremail = fake.email()

    user_data.append([username, userpassword, useremail])


df = pd.DataFrame(user_data, columns = ['UserName', 'UserPassword', 'UserEmail'])

df.to_csv('users.csv')