# major
from getpass import getpass
from flask import Flask, render_template, request, redirect, url_for
import time
import serial
import json
import os
#import request
import sys
from flask_wtf import Form

sys.setrecursionlimit(1500)

app = Flask(__name__, static_url_path='/static')
#app.config['SECRET_KEY'] = '23456789'

data = serial.Serial(
                     port='/dev/ttyS0',
                     baudrate = 9600,
                     parity = serial.PARITY_NONE,
                     stopbits = serial.STOPBITS_ONE,
                     bytesize = serial.EIGHTBITS
                    )
print " "

try:
        while 1:
                x= data.readline(12)
                print (x)

                           

                #with open('info.json') as json_file:
                        #info = json.load(json_file)
                        #for users in info['users']:
                                #if(x==users['id']):
                        #print("true",users['id'])
                @app.route("/")
                def start():
                        return render_template('pin.html')
                @app.route("/pin", methods=["GET", "POST"])
                def pin():
                        if request.method == 'POST':
                                #pin = request.form.get('pin')
                                #print(pin)
                                pin='1234'
                                pin1='4567'
                                c=4321
                        #with open('info.json') as json_file:
                                #info = json.load(json_file)
                                #for users in info['users']:request.form.pin=='4321'
                                        #if(x==users['id']):
                        #if(x=='10004ACB8B1A' or x=='10004AF1D873' or x=='10004AA8897B'):
                       
                                if(x=='10004ACB8B1A' and pin=='1234'):
                                        return render_template('color.html')
                                elif(x=='10004AF1D873' and pin1=='4567'):                                                                   
                                        return render_template('color.html')
                                elif(x=='10004AA8897B' and pin==c):
                                        return redirect(url_for('color'))
                                else:
                                        return redirect(url_for('invalid'))

                @app.route("/color", methods=["GET", "POST"])
                def color():
                        if request.method == "POST":
                                code=request.form.get('colorcode')
                                code='1'
                                if(x=='10004ACB8B1A' and code=='1'):
                                        return render_template('transaction.html')
                                        #return redirect(url_for('color'))
                                elif(x=='10004AF1D873' and pin1=='4'):                                                                   
                                        return redirect(url_for('color'))
                                elif(x=='10004AA8897B' and pin1=='2'):
                                        return redirect(url_for('color'))
                                else:
                                        return redirect(url_for('invalid'))
                        
                
                
                @app.route("/invalid")
                def invalid():
                        return render_template('invalid.html')

                
                                
                                                

                if __name__ == '__main__':
                        app.run(debug=True)
except KeyboardInterrupt:
        data.close()


