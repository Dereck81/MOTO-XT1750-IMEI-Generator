#!/usr/bin/python
# IMEI GENERATOR MOTOROLA MAUMETA

import random

class HexIMEIGenerator(object):
	'''Sec is IMEI 1 or 2'''

	def __init__(self, IMEI: str, Sec: int):
		self.IMEI = IMEI
		self.Sec = Sec

	def generator(self) -> tuple:
		if self.__checkIMEI() == False:
			return

		self.IMEIDec=list()
		self.IMEIHex=list()

		dictValues={
			1:[list(range(128,144)), list(range(144,160)), list(range(160,176)), list(range(176,192)),list(range(192,208)), list(range(208,224)), list(range(224,240)), list(range(240,256)), list(range(1,16)), list(range(16,32))],
			2:[list(range(192,208)), list(range(208,224)), list(range(224,240)), list(range(240,256)), list(range(1,16)), list(range(16,32)), list(range(32,48)), list(range(48,64)), list(range(64,80)), list(range(80,96))],
			3:[list(range(128,144)), list(range(144,160)), list(range(160,176)), list(range(176,192)), list(range(192,208)), list(range(208,224)), list(range(224,240)), list(range(240,256)), list(range(1,16)), list(range(16,32))],
			4:[list(range(224,240)), list(range(240,256)), list(range(1,16)), list(range(16,32)), list(range(32,48)), list(range(48,64)), list(range(64,80)), list(range(80,96)), list(range(96,112)), list(range(112,128))],
			5:[list(range(32,48)), list(range(48,64)), list(range(64,80)), list(range(80,96)), list(range(96,112)), list(range(112,128)), list(range(128,144)), list(range(144,160)), list(range(160,176)), list(range(176,192))],
			6:[list(range(16,32)), list(range(32,48)), list(range(48,64)), list(range(64,80)), list(range(80,96)), list(range(96,112)), list(range(112,128)), list(range(128,144)), list(range(144,160)), list(range(160,176))],
			7:[list(range(64,80)), list(range(80,96)), list(range(96,112)), list(range(112,128)), list(range(128,144)), list(range(144,160)), list(range(160,176)), list(range(176,192)), list(range(192,208)), list(range(208,224))],
			8:[list(range(128,144)), list(range(144,160)), list(range(160,176)), list(range(176,192)), list(range(192,208)), list(range(208,224)), list(range(224,240)), list(range(240,256)), list(range(1,16)), list(range(16,32))],
			9:[list(range(176,192)),list(range(192,208)), list(range(208,224)), list(range(224,240)), list(range(240,256)), list(range(1,16)), list(range(16,32)), list(range(32,48)), list(range(48,64)), list(range(64,80))],
			10:[list(range(32,48)), list(range(48,64)), list(range(64,80)), list(range(80,96)), list(range(96,112)), list(range(112,128)), list(range(128,144)), list(range(144,160)), list(range(160,176)), list(range(176,192))],
			11:[list(range(224,240)), list(range(240,256)), list(range(1,16)), list(range(16,32)), list(range(32,48)), list(range(48,64)), list(range(64,80)), list(range(80,96)), list(range(96,112)), list(range(112,128))],
			12:[list(range(192,208)), list(range(208,224)), list(range(224,240)), list(range(240,256)), list(range(1,16)), list(range(16,32)), list(range(32,48)), list(range(48,64)), list(range(64,80)), list(range(80,96))],
			13:[list(range(64,80)), list(range(80,96)), list(range(96,112)), list(range(112,128)), list(range(128,144)), list(range(144,160)), list(range(160,176)), list(range(176,192)), list(range(192,208)), list(range(208,224))],
			14:[list(range(176,192)),list(range(192,208)), list(range(208,224)), list(range(224,240)), list(range(240,256)), list(range(1,16)), list(range(16,32)), list(range(32,48)), list(range(48,64)), list(range(64,80))],
			15:[list(range(224,240)), list(range(240,256)), list(range(1,16)), list(range(16,32)), list(range(32,48)), list(range(48,64)), list(range(64,80)), list(range(80,96)), list(range(96,112)), list(range(112,128))]}

		for i in range(0,15):
			number = self.IMEI[i]
			temp_value = self.__randomNumber(dictValues[i+1][int(number)])
			self.IMEIDec.append(f"nvram_ef_barcode_num[{self.SecArray}] = {temp_value}")
			temp_value_hex = "0x0" + hex(int(temp_value)).lstrip('0x') if len(hex(int(temp_value)).lstrip('0x')) == 1 else hex(int(temp_value))
			self.IMEIHex.append(f"nvram_ef_barcode_num[{self.SecArray}] = {temp_value_hex}")
			self.SecArray+=1

		return self.IMEIDec, self.IMEIHex


	def __checkIMEI(self) -> bool:
		if not (len(self.IMEI) == 15 and self.IMEI.isdigit()):
			return False;

		if self.Sec == 1:
			self.SecArray = 26
		elif self.Sec == 2:
			self.SecArray = 42
		else:
			return False

		return True

	def __randomNumber(self, list_values: list) -> int:
		LS = max(list_values)
		Indice = list_values.index(LS)
		randomx = random.randrange(0, Indice+1)
		return list_values[randomx]
