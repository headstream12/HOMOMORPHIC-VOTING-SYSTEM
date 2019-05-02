#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
# from flask_httpauth import HTTPBasicAuth
import sqlite3
import sys
from sage.all import *

app = Flask(__name__, static_url_path="")
# auth = HTTPBasicAuth()

# @auth.get_password
# def get_password(username):
#     if username == 'miguel':
#         return 'python'
#     return None
#

# @auth.error_handler
# def unauthorized():
#     return make_response(jsonify({'error': 'Unauthorized access'}), 403)
#     # return 403 instead of 401 to prevent browsers from displaying the default auth dialog

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

adverts = {
    "result": {
        "count": 2,
        "adverts": [
            {
                "id": "1",
                "price": 3230000,
                "isFavorite": True,
                "date": "2018-09-11T13:00:22+0400",
                "city": "pe",
                "car": {
                    "images": [
                        "https://t1-cms-ru.images.toyota-europe.com/toyotaone/ruru/002-new-camry-next-steps_tcm-3020-1324581.jpg",
                        "https://t1-cms-ru.images.toyota-europe.com/toyotaone/ruru/new-camry-4_tcm-3020-1362356.jpg"],
                    "brand": "Toyota",
                    "model": "Camry",
                    "year": 2018,
                    "engineType": "petrol",
                    "transmissionType": "manual",
                    "drivetrainType": "fwd",
                    "distance": 1000,
                    "enginePower": 279,
                    "engineVolume": 3.5
                }
            },
            {
                "id": "2",
                "price": 2300000,
                "isFavorite": False,
                "date": "2018-09-11T13:00:22+0400",
                "city": "das",
                "car": {
                    "images": ["http://dzhips.com/wp-content/uploads/2017/12/Lexus-LX-2018.jpg",
                               "http://dzhips.com/wp-content/uploads/2017/12/leksus-LX-570.jpg"],
                    "brand": "Lexus",
                    "model": "LX570",
                    "year": 2017,
                    "engineType": "diesel",
                    "transmissionType": "auto",
                    "drivetrainType": "awd",
                    "distance": 10000,
                    "enginePower": 350,
                    "engineVolume": 5.7
                }
            }
        ]
    },
    "errorMessage": "",
    "errorCode": 0
}

@app.route('/v1/getAdverts', methods=['POST'])
def getAdverts():
    # if not request.json:
    #     abort(400)
    #
    # limit = request.json['limit']
    # page = request.json['page']
    # type = request.json['type']

    """city = request.json['advertFilter']['city']
    minPrice = request.json['advertFilter']['minPrice']
    maxPrice = request.json['advertFilter']['maxPrice']

    brand = request.json['advertFilter']['carFilter']['brand']
    model = request.json['advertFilter']['carFilter']['model']
    minYear = request.json['advertFilter']['carFilter']['minYear']
    maxYear = request.json['advertFilter']['carFilter']['maxYear']
    minDistance = request.json['advertFilter']['carFilter']['minDistance']
    maxDistance = request.json['advertFilter']['carFilter']['maxDistance']
    minEnginePower = request.json['advertFilter']['carFilter']['minEnginePower']
    maxEnginePower = request.json['advertFilter']['carFilter']['maxEnginePower']
    minEngineVolume = request.json['advertFilter']['carFilter']['minEngineVolume']
    maxEngineVolume = request.json['advertFilter']['carFilter']['maxEngineVolume']
    transmissionTypes = request.json['advertFilter']['carFilter']['transmissionTypes']
    engineTypes = request.json['advertFilter']['carFilter']['engineTypes']
    drivetrainTypes = request.json['advertFilter']['carFilter']['drivetrainTypes']"""
    # c.execute('SELECT * FROM advertisements limit ' + str(limit))
    # print(c.fetchone())

    let1 = encrypter.encrypt(1)
    let2 = encrypter.encrypt(0)
    a = encrypter.decrypt(let1)
    b = encrypter.decrypt(let2)
    sumarnaya = 1
    for i in range(200000):
        sumarnaya = (sumarnaya * let1 * let2) % encrypter.N ** 2
    # print(i)
    # print(encrypter.decrypt(sumarnaya))
    res = encrypter.decrypt(sumarnaya)

    print('let1', let1)
    print('let2', let2)
    print(a)
    print(b)
    print(res)

    return jsonify(adverts)

class Encrypter(object):
    def __init__(self):
        super(Encrypter, self).__init__()
        self.N = 0
        self.g = 0
        self.secretKey = 0
        self.generateKeys()

    def generateKeys(self):
        p = random_prime(2**1024, false, 2**1023)
        print("p = ", p)
        q = random_prime(2**1024, false, 2**1023)
        print("q = ", q)
        self.secretKey = LCM(p-1,q-1)
        print("secretKey = ", self.secretKey)
        self.N = p * q
        print("N = ", self.N)
        self.g = randrange(1, self.secretKey-1)
        print("g = ", self.g)

    def encrypt(self, number):
        x = randrange(2**1023, 2**1024)
        print("x = ", x)
        e = (pow(self.g, number, self.N**2)*pow(x,self.N, self.N**2)) % self.N**2
        print("e = ", e)
        return e

    def L(self, u):
        #print('u = ', u)
        Uchisl = int(u - 1)
        #print('UChisl', Uchisl)
        #print('N = ', self.N)
        res = Uchisl / self.N
        #print('res', res)

        return res

    def decrypt(self, cipherNumber):
        pow1 = pow(cipherNumber, self.secretKey, self.N**2)
        #print('pow1', pow1)
        chisl = self.L(pow1)
        #print('chisl = ', chisl)
        znam = self.L(pow(self.g, self.secretKey, self.N ** 2))
        #print('chisl = ', znam)

        return (chisl / znam) % self.N


encrypter = Encrypter()

if __name__ == '__main__':
    conn = sqlite3.connect('carjunkstore.db', check_same_thread=False)
    c = conn.cursor()
    app.run(host='0.0.0.0', debug=True)
    conn.close()
