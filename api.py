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


# l=[148921,148920,148918,148919,149383,149384,149382,149387,148404,148406,148405,148407]
l2=[]
@app.route("/",methods=['GET'])
def link_api():
    url="https://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?frmdt=02-Jan-2023"
    resp=requests.get(url)
    code=requests.get("code")
    name=requests.get("name")
    date=requests.get("date")
    temp={'code':code,'name':name,'date':date}
    # print(resp.json().get('data')[0].get("nav"))
    l2.append(temp)
    print(l2)
    return render_template("index.html",data=resp.json().get('code')[0].get("name")[0].get("date")[0])










if __name__=="__main__":
    app.run(debug=True)