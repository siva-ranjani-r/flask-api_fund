from flask import Flask, render_template,request
import requests


app = Flask(__name__)


# @app.route("/")
# def api():
#     url="https://api.mfapi.in/mf/120185"
#     resp=requests.get(url)
#     return render_template("index.html",data=resp.json())

# l=[120185]
# @app.route("/")
# def link_api():
#     url="https://api.mfapi.in/mf/"+str(l[0])
#     resp=requests.get(url)
#     return render_template("index.html",data=resp.json().get('data')[0].get('nav'))


lis=[148921,139619,149383,148404,119354,149366,149303,120413,147183,149183,150659,141223,118652,100631,150858,148980]
l2=[]
@app.route("/",methods=['POST','GET'])
def link_api():
    for i in range(len(lis)):
        url="https://api.mfapi.in/mf/"+str(lis[i])
        resp=requests.get(url)
        temp2=resp.json().get('meta').get('fund_house')
        new_get=resp.json().get('data')[0].get('nav')
        temp={'id':lis[i],'fund_house':temp2,'nav':new_get}
        l2.append(temp)
    return render_template("index.html",data=l2)




if __name__=="__main__":
    app.run(debug=True)