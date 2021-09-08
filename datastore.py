# Below is a dictionary that contains information about real estate space for
# a doctor's office. Using the dictionary, create a csv file that has details
# for each space represented as rows. Name your file 'retail_space.csv.


'''
Your final output should look like:

room-number,use,sq-ft,price
100,reception,50,75
101,waiting,250,75
102,examination,125,150
103,examination,125,150
104,office,150,100

'''




datastore = { "medical":[
      { "room-number": 100,
        "use": "reception",
        "sq-ft": 50,
        "price": 75
      },
      { "room-number": 101,
        "use": "waiting",
        "sq-ft": 250,
        "price": 75
      },
      { "room-number": 102,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 103,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 104,
        "use": "office",
        "sq-ft": 150,
        "price": 100
      }

      ]
}

# to print the price 75
print(datastore['medical'][1]['price'])

# for loop to create csv file
# datastore['medical'] is a list and l is an element in this list (string)
outfile = open("retail_store.csv", 'w')
outfile.write('room-number,use,sq-ft,price\n')

for l in datastore['medical']:
  outfile.write(str(l["room-number"]) + ',' + l['use'] + ',' + str(l["sq-ft"]) + ',' + str(l["price"]) + '\n')
# str method must be used because integers and floats must be converted to a string in order to write a file

outfile.close()