from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/movie/search")
def movie_search():

    if request.args.get('query'):
        query = request.args.get('query')
    else:
        query = '20230930'    

    URL = f"http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt={query}"

    res = requests.get(URL)

    rjson = res.json()
    movie_list = rjson.get("boxOfficeResult").get("weeklyBoxOfficeList")

    return render_template("movie_search.html", data=movie_list)

if __name__ == '__main__':
    app.run(debug=True)