import csv

def read_and_print():
    f=open('results.txt','w', newline='')
    with open('data.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            for obj in row:
                obj=obj.strip()
                if obj.isalpha():
                    obj = obj +' - alphabetical strings'
                elif obj.isdigit():
                    obj = obj +' - integer'
                elif obj.isalnum():
                    obj = obj +' - alphanumeric'
                else:
                    obj = obj +' - real numbers'
                print(obj)
                f.write(obj+'\n')
    f.close()

read_and_print()