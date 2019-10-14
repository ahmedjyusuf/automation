import machine, time, sys
import gsm
from machine import Pin



#machine.reset() seems to be crashing the code


# APN credentials (replace with yours)
led = Pin(2, Pin.OUT)


GSM_APN  = 'simple' # Your APN
GSM_USER = '' # Your User
GSM_PASS = '' # Your Pass

# Power on the GSM module
main_pwr = Pin(23, Pin.OUT) #power on
main_pwr.value(1)

GSM_PWR = machine.Pin(4, machine.Pin.OUT)
GSM_RST = machine.Pin(5, machine.Pin.OUT)

GSM_PWR.value(0)
GSM_RST.value(1)

# Init PPPoS

gsm.debug(True)  # Uncomment this to see more logs, investigate issues, etc.

gsm.start(tx=27, rx=26, apn=GSM_APN, user=GSM_USER, password=GSM_PASS)
gsm.sms_cb(None) #stops flagging unread msgs
led.value(0)
def smscb(indexes):
	if indexes:
		msg = gsm.readSMS(int(indexes[0]), True)
		if msg:
			print("New message from", msg[2])
			print(msg[6])

			sender = msg[2]
			sms = msg[6]
			gsm.sendSMS(sender, sms)
			
			led.value(0)
			time.sleep(1)
			text = sms.split()
			led.value(0)
			time.sleep(1)
			if text[0] == '[-EVCPlus-]' and text[1] == 'waxaad' and text[10] == 'waa':
				def evcplus():
					customer = text[5]
					amount = text[2][1:]
					credit = float(amount)*60
					#print(f'{credit} minutes')
					print('{} {}'.format(credit, 'Minutes'))

					while (credit >= 1):
						# do whatever you do
						led.value(1)
						#print('hello\n')
						#print(int(credit), end='Daqiiqo\n')
						wakhti = '{} {}'.format(int(credit), 'Daqiiqo/Minutes\n')
						print(wakhti)
						gsm.sendSMS(sender, wakhti)
						credit -= 1
						time.sleep(60)
					led.value(0)
					print('\nFadlan ku shubo')
					time.sleep(1)
					gsm.sendSMS(sender, 'Fadlan ku shubo')
				evcplus()		
led.value(0)
gsm.sms_cb(smscb, 15)
