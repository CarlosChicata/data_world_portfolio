from random import randint, uniform
from datetime import datetime

from flask import Flask, request, jsonify


app = Flask(__name__)


CURRENCY = [ "EUR", "GBP", "AUD", "NZD", "USD", "CAD", "CHF", "JPY"]
OPERATION_TYPE = ["deposit", "withdrawal"]
NUMBER_USERS = 10000
MAX_AMOUNT = 200.00
MIN_AMOUNT = 5.00


def random_transaction():
   '''
      generate a random dummy data to simulate a transaction.
      return: Dict
   '''
   random_data = {
      'currency' : CURRENCY[randint(0, len(CURRENCY)-1)],
      'amount' : round(uniform(MIN_AMOUNT, MAX_AMOUNT),2),
      'operation_type' : OPERATION_TYPE[randint(0, len(OPERATION_TYPE)-1)],
      'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
      "user_id": randint(0, NUMBER_USERS),
   }
   return random_data 


@app.route('/transaction')
def generate_random_one_transaction():
   '''
   Generate one synthetic transaction.
   return: JSON
   '''
   return jsonify(random_transaction())


@app.route("/transaction_batch")
def generate_random_batch_transaction():
   '''
   Generate batch synthetic transaction. The number of transaction in random.
   return: JSON
   '''
   random_item = randint(1,200)
   print(random_item)
   rpta = []
   while random_item > 0:
      rpta.append(random_transaction())
      random_item = random_item - 1

   return jsonify(rpta)


@app.route("/", methods=['POST'])
def generate_data(request):
   if request.args.get('mode') == None or request.args.get('mode').lower() == 'single':
      return generate_random_one_transaction()
   elif request.args.get('mode') != None and request.args.get('mode').lower() == 'batch':
      return generate_random_batch_transaction()


if __name__ == '__main__':
   app.run()

