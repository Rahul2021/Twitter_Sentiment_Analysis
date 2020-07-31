import tweepy,re
from textblob import TextBlob
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pac.model import *
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
filename="tweeter.pkl"
sa=pickle.load(open(filename,'rb'))
app.config['SEND_FILE_MAX_AGE_DEFAULT']=0

@app.route('/')
def home():
   return render_template('Student.html',bodyof="home",title="Home")

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if(request.method == 'POST'):
      hastag=request.form['ht']
      number=request.form['nt']
      val=sa.downloadData(hastag,number)
      key=["{}% people thought it was positive","{}% people thought it was weakly positive","{}% people thought it was strongly positive","{}% people thought it was negative","{}% people thought it was weakly negative","{}% people thought it was strongly negative","{}% people thought it was neutral"]
      rep_l=[key[i].format(j) for i,j in enumerate(val)]
      p=sa.plotPieChart(*val,hastag,number )
      li=sa.tx
      return render_template('report.html',val=rep_l,p=p,nt=li,bodyof="report",title="Report")

if __name__ == '__main__':
   app.run(debug = True)
