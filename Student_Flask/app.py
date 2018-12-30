from flask import Flask, render_template, request, url_for
import time
import re

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def func():
	if(request.method=="GET"):
		msg=""
		return render_template("student.html", msg=msg)
	else:
		usn_pat = "^[1][A-Z][A-Z][1][5-8][A-Z][A-Z][0-9][0-9][0-9]$"
		if not re.match(usn_pat, request.form["usn"]):
			msg="USN format mismatch"
			return render_template("student.html", msg=msg)
		try:
			time.strptime(request.form["dob"],"%d-%m-%Y")
		except ValueError:
			msg="Invalid date format"
			return render_template("student.html", msg=msg)
		msg="Success"
		return render_template("student.html", msg=msg)
	
if __name__=="__main__":
	app.run(debug=True)