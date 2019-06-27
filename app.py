from flask import Flask, jsonify, render_template, request 
import sqlite3
app = Flask(__name__)
@app.route('/',methods = ['POST', 'GET'])
def index():
    return render_template('index.html')
@app.route('/credit/',methods = ['POST', 'GET'])
def credit():
    return render_template('credit.html')
@app.route('/search/',methods = ['POST', 'GET'])
def search():
    return render_template('index.html')
@app.route('/chapter/',methods=['POST', 'GET'])
def chapters():
    conn = sqlite3.connect('ipc.db')
    res=conn.execute("select * from chapters;")
    data={}
    for row in res:
        data[row[0]]={'num':row[1],'frm':row[2], 'ttl':row[4]}
    conn.close() 
    return render_template('chapters.html',len=len(data),data=data)
@app.route('/chapter/<num>',methods=['POST', 'GET'])
def chapter(num):
    conn = sqlite3.connect('ipc.db')
    res=conn.execute("select * from ipc where chapter=? and type=?;",(num,'article'))
    res2=conn.execute("select * from chapters where num=?;",(num,))
    data={}
    data['num']=num
    for row2 in res2:
        data['frm']=row2[2]
        data['dis']=row2[3]
    i=0
    for row in res:
        data[i]={'num':row[1],'txt':row[3]}
        i=i+1
    conn.close() 
    return render_template('chapter.html',len=len(data)-3,data=data)
@app.route('/section/',methods=['POST', 'GET'])
def sections():
    conn = sqlite3.connect('ipc.db')
    res=conn.execute("select * from ipc where type=?;", ('article',))
    data={}
    i=0
    for row in res:
        data[i]={'num':row[1], 'chap':row[4]}
        i=i+1
    conn.close() 
    return render_template('sections.html',len=len(data),data=data)
@app.route('/section/<num>',methods=['POST', 'GET'])
def section(num):
    conn = sqlite3.connect('ipc.db')
    res=conn.execute("select * from ipc where num=?;",(num,))
    data={}
    data['num']=num
    for row in res:
        data['txt']=row[3]
        data['chap']=row[4]
    res2=conn.execute("select * from chapters where num=?;",(data['chap'],))
    for row2 in res2:
        data['frm']=row2[2]
        data['ttl']=row2[4]
    conn.close() 
    return render_template('section.html',data=data)
@app.route('/search/<q>',methods=['POST', 'GET'])
def searchresult(q):
    conn = sqlite3.connect('ipc.db')
    res=conn.execute("select * from ipc where text like ?",
  ('%'+q+'%', ))
    data={}
    data['q']=q
    i=0
    for row in res:
        data[i]={}
        data[i]['num']=row[1]
        data[i]['chap']=row[4]
        res2=conn.execute("select * from chapters where num=?;",(data[i]['chap'],))
        for row2 in res2:
            data[i]['ttl']=row2[4]
            i=i+1
    conn.close() 
    return render_template('search.html',len=len(data)-1,data=data)

if __name__ == '__main__':
   app.run(debug = True)
  
