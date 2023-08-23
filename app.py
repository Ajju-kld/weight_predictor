from flask import Flask,render_template,request
import htow as ht
 

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def hello():
      if request.method =='POST':
            height=ht.cm_to_inches(request.form['height'])
            weight=ht.pounds_to_kg(ht.predict([[float(height)]]))
            
            return render_template('index.html',hei=weight)
      return render_template('index.html')


@app.route('/lbs')
def lbs():
      return render_template('lbs.html')
if __name__=="__main__":
        app.run()