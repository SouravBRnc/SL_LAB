from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def cart():
	if(request.method=="GET"):
		return render_template("shop.html")
	else:
		a = int(request.form['apple'])
		b = int(request.form['banana'])
		c = int(request.form['mango'])
		cost = a*200 + b*50 + c*100
		msg=[]
		if a>0:
			app_dict={'item':'Apple','quantity':a,'rate':200,'total':a*200}
			msg.append(app_dict)
		if b>0:
			ban_dict={'item':'Banana','quantity':b,'rate':50,'total':b*50}
			msg.append(ban_dict)
		if c>0:
			man_dict={'item':'Mango','quantity':c,'rate':100,'total':c*100}
			msg.append(man_dict)
		return render_template("cart.html", msg=msg, cost=cost)

if(__name__)=="__main__":
	app.run(debug=True)	
