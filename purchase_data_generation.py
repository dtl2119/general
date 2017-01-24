#!/usr/bin/python

from faker import Factory

purchase_data_file_path = "/Users/drewlimm/insight/general/batch_purchase.csv"
rows = 100000
rows = 3


fake = Factory.create()

with open(purchase_data_file_path, "w") as outFile:
    for x in range (rows):
        name = fake.name()
        address = fake.address()
        #lorem = fake.lorem()

        row = ",".join([name, address,"\n"])

        outFile.write(row)
    
