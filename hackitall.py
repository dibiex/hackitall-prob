import json
import os
import random
import requests
from pprint import pprint

inputs1 = {'1': 'Show stock',
           '2': 'Exit'}

inputs2 = {'1': 'Yes',
           '2': 'No'}

inputList = [inputs1, inputs2]


def print_inputs(id):
    for key in inputList[id]:
        print(key + ': ' + inputList[id][key])


def print_stock(json_obj):
    indx = 1
    for product in json_obj:
        print(str(indx) + ') ' + product['productName'] + ':', product['price'] +
              '$ -', product['stock'] + ' left in stock')
        indx += 1


def check_stock():
    f = open('stock.json')
    d = json.load(f)
    print_stock(d)

    return d


states = ['start', 'showstock', 'buy']


def take_input():
    currentState = 0
    state = states[currentState]

    boughtProduct = None
    while(True):
        if state == 'start':
            os.system('clear')
            print_inputs(0)
            i = input()
            if int(i) == 2:
                exit()
            currentState += 1
            state = states[currentState]
        elif state == 'showstock':
            os.system('clear')
            stock = check_stock()
            i = int(input())

            boughtProduct = stock[i-1]
            print("Purchase", boughtProduct['productName'] + '?')
            print_inputs(1)
            i = int(input())

            if i == 1:
                currentState += 1
                state = states[currentState]
        elif state == 'buy':
            print("We'll you're kinda buying")
            if int(boughtProduct['stock']) > 0:
                print("Please enter your card details: ")

                card_nr = input("Card Number: ")
                cvv = input("CVV: ")
                name = input("Holder Name: ")
                expiration_date = input("Expiration Date: ")

                transaction_id = random.getrandbits(128)

                url = "http://web:5000/transaction/" + \
                    str(transaction_id)
                payload = {
                    'productName': boughtProduct['productName'],
                    'price': boughtProduct['price'],
                    'card_details': {'card_nr': card_nr,
                                     'cvv': cvv,
                                     'name': name,
                                     'expiration_date': expiration_date}}
                headers = {'content-type': 'application/json'}

                r = requests.post(url, data=json.dumps(
                    payload), headers=headers)

                if r.json()['result'] == True:
                    boughtProduct['stock'] = str(
                        int(boughtProduct['stock']) - 1)
                    print("Transaction completed")
                    print("Do you want to purchase anything else?[y/n]")
                    confirm = input()
                    if confirm == "y":
                        currentState = 0
                        state = states[0]   
                        continue
                    else:
                        exit()
                else:
                    print("Transaction failed!")
                    print("Do you want to purchase anything else?[y/n]")
                    confirm = input()
                    if confirm == "y":
                        currentState = 0
                        state = states[0]   
                        continue
                    else:
                        exit()
            else:
                print("The stock is empty!")
                currentState = 1
                state = states[currentState]
                continue

            i = int(input())


if __name__ == '__main__':
    take_input()
