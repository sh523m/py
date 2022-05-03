population = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}

def add():
    country=input("Enter country name to add:")
    country=country.lower()
    if country in population:
        print("Country already exist in our dataset. Terminating")
        return
    p=input(f"Enter population for {country}")
    p=float(p)
    population[country]=p # Adds new key value pair to dictionary
    print_all()

def remove():
    country = input("Enter country name to remove:")
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    del population[country]
    print_all()

def query():
    country = input("Enter country name to query:")
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        return
    print(f"Population of {country} is: {population[country]} crore")

def print_all():
    for country, p in population.items():
        print(f"{country}==>{p}")

def main():
    op=input("Enter operation (add, remove, query or print):")
    if op.lower() == 'add':
        add()
    elif op.lower() == 'remove':
        remove()
    elif op.lower() == 'query':
        query()
    elif op.lower() == 'print':
        print_all()

if __name__ == '__main__':
    main()
"""
cout={
    'china': '143',
    'India' : '136',
    'usa' : '32',
    'pakistan': '21'
}
input1=input("Enter operation(print,add or Remove):")
if input1=="print":
  print(cout)
elif input1 =="add":
  input2=input()
  if input2 in cout.keys():
    print("country already exist")
  elif input2 is not cout.keys():
    input3=input()
    cout[input2]=input3
    print(cout)
elif input1=="Remove":
  input4=input()
  if input4 in cout.keys():
    del cout[input4]
    print(cout)
  else:
    print("country does not exist")
"""
    
