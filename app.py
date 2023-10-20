from flask import Flask,render_template,request,url_for,redirect
app=Flask(__name__)


Student_list = [{"Name": "Mahalakshmi", "Age": 24, "Roll_NO": 101, "Marks": [90, 75, 80, 98, 75]},

 

                {"Name": "Nijanthan", "Age": 23, "Roll_NO": 102, "Marks": [90, 75, 80, 98, 65]},

 

                {"Name": "Selva", "Age": 22, "Roll_NO": 103, "Marks": [90, 75, 80, 78, 99]},

 

                {"Name": "Preethi", "Age": 22, "Roll_NO": 104, "Marks": [94, 75, 80, 88, 35]},

 

                {"Name": "Ajay", "Age": 23, "Roll_NO": 105, "Marks": [70, 85, 80, 98, 35]},

 

                {"Name": "Anand", "Age": 26, "Roll_NO": 106, "Marks": [90, 75, 85, 98, 35]},

 

                {"Name": "Pavitran", "Age": 21, "Roll_NO": 107, "Marks": [80, 98, 35, 90, 75]},

 

                {"Name": "Kumar", "Age": 25, "Roll_NO": 108, "Marks": [90, 80, 98, 35, 75]},

 

                {"Name": "Saranya", "Age": 26, "Roll_NO": 109, "Marks": [75, 80, 90, 98, 35]},

 

                {"Name": "Jeffin", "Age": 22, "Roll_NO": 110, "Marks": [98, 35, 90, 75, 80]}]
@app.route('/',methods=["GET","POST"])
def home():
    if request.method=="POST":
        dict_1={}
        dict_1.update({"Name":request.form.get("name")})
        dict_1.update({"Age":request.form.get("age")})
        dict_1.update({"Roll_NO":request.form.get("rollno")})
        marks_1=[]
        marks_1.append(request.form.get("tamil"))
        marks_1.append(request.form.get("english"))
        marks_1.append(request.form.get("maths"))
        marks_1.append(request.form.get("science"))
        marks_1.append(request.form.get("social"))
        dict_1.update({"Marks":marks_1})
        Student_list.append(dict_1)
        return render_template("index.html",data=Student_list)
    return render_template("index.html",data=Student_list)


@app.route('/<string:a>')
def home1(a):
    Student_list.pop(int(a)-1)
    return render_template("index.html",data=Student_list)

@app.route('/edit/<string:b>',methods=["GET","POST"])
def edit(b):
    dict_1=Student_list[int(b)-1]
    if request.method=="POST":
        
        dict_1.update({"Name":request.form.get("name")})
        dict_1.update({"Age":request.form.get("age")})
        dict_1.update({"Roll_NO":request.form.get("rollno")})    
        marks_1=[]
        marks_1.append(request.form.get("tamil"))
        marks_1.append(request.form.get("english"))
        marks_1.append(request.form.get("maths"))
        marks_1.append(request.form.get("science"))
        marks_1.append(request.form.get("social"))
        dict_1.update({"Marks":marks_1})
        # Student_list.append(dict_1)
        return redirect(url_for('home')) 
    return render_template("edit.html",amazon=dict_1)
if __name__ =="__main__":
    app.run(debug=True)