import psycopg2
from  user_input import *

conn = psycopg2.connect(host = host,
                        port = port,
                        database = database,
                        user = user,
                        password = password)
cur = conn.cursor()

path = '/Users/okeefe/Downloads'

filelist = []
for i in range(10, 18):
    filelist.append('/Users/okeefe/Downloads/filesenr.asp(' + str(i) + ').txt')
    
headers = []

for path in filelist:
    with open(path) as f:
        headers.append(f.readline())

        
query = ""

for 

SELECT
FROM
WHERE


cur.execute(query)


output = cur.fetchall()
# cur.execute(
# """

# """
# )