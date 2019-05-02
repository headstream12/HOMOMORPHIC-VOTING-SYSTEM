from sage.all import *
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
		x = 7#randrange(1, 10)
		#print("x = ", x)
		e = (pow(self.g, number, self.N**2)*pow(x,self.N, self.N**2)) % self.N**2
		#print("e = ", e)
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
ahah = encrypter.encrypt(12)
print(ahah)
print(encrypter.decrypt(ahah))
#print(encrypter.decrypt(76740892273306418113817965124005066585871728617737571851601638454673545950539359641901688923520808158022759046220210011951839881865113060707354759756004423007552382257959881468724440973518810200971632213720042247347115441580021193614065939205117904421406361816990093136609429608265517184619563397573700304968012856925926561118593171083269798229432765675600300535420015013766706254053655951108449619570414663578489226748792868527913039073022602409274830037687187535005867555039171559332452388422577307782780321712144481161000731503785636005260276038556627250479038924531492716069058631227500543027722818957971478517185776381557573303918707443011697054054850883734390155156170356585619645488502615374778393016156629698315680248969797372626039136637353802103147616814338175025238944338753699836777048724881004123657569039583478625097847372947293739863111112120347380493723592501413700394940367855615057085463910822752855218403712361532456840169225622850554557040848956711854135454197204375290455252985259666605200023013559387397814952909598108898371125757012082790492064526002706595081405778055665682183352197041706430587058108774333997741399276528037779512785695557586069639438852861647716289577591811225266440343694752609671465034813))
# let1 = encrypter.encrypt(1)
# let2 = encrypter.encrypt(0)
# a = encrypter.decrypt(let1)
# b = encrypter.decrypt(let2)
# sumarnaya = 1
# for i in range(20000):
# 	sumarnaya = (sumarnaya * let1 * let2) % encrypter.N ** 2
# 	#print(i)
# 	#print(encrypter.decrypt(sumarnaya))
# res = encrypter.decrypt(sumarnaya)
#
# print('let1', let1)
# print('let2', let2)
# print(a)
# print(b)
# print(res)
