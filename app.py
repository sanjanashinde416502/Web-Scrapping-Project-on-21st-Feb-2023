from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import logging
logging.basicConfig(filename="scrapper.log" , level=logging.INFO)
import pymongo

app = Flask(__name__)

@app.route("/", methods = ['GET'])  # here we are creating a homepage which will run 'index.txt' file and take a text i.e
def homepage():                            # product's name as input and submit that by clicking on search.
    return render_template("index.html")

@app.route("/review" , methods = ['POST' , 'GET']) # '/review' route is called when we click on search button as we have return 
def index():                                      # from class that we called action that automatically call '/review' route then
    if request.method == 'POST':                  # it will exceute the function written in that. 
        try:                                      # here we have done exception handling
            searchString = request.form['content'].replace(" ","")   # here we are replacing space given in searching string with
                                                                      # non space to get searching string.
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString # here we are appending flipcart url with 
                                                                               #  this serarching  string 
            uClient = uReq(flipkart_url)  # bellow this all code is same that we have done in web scraping class
            flipkartPage = uClient.read()
            uClient.close()
            flipkart_html = bs(flipkartPage, "html.parser")
            bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
            del bigboxes[0:3]
            box = bigboxes[0]
            productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
            prodRes = requests.get(productLink)
            prodRes.encoding='utf-8'
            prod_html = bs(prodRes.text, "html.parser")
            print(prod_html)
            commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})

            filename = searchString + ".csv"
            fw = open(filename, "w")
            headers = "Product, Customer Name, Rating, Heading, Comment \n"
            fw.write(headers)
            reviews = []
            for commentbox in commentboxes:
                try:
                    #name.encode(encoding='utf-8')
                    name = commentbox.div.div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text # to get name of review writer

                except:
                    logging.info("name")

                try:
                    #rating.encode(encoding='utf-8')
                    rating = commentbox.div.div.div.div.text          # to get ratings


                except:
                    rating = 'No Rating'
                    logging.info("rating")

                try:
                    #commentHead.encode(encoding='utf-8')
                    commentHead = commentbox.div.div.div.p.text  # to get comment heading in reviews

                except:
                    commentHead = 'No Comment Heading'
                    logging.info(commentHead)
                try:
                    comtag = commentbox.div.div.find_all('div', {'class': ''})
                    #custComment.encode(encoding='utf-8')
                    custComment = comtag[0].div.text     # to get actual comments
                except Exception as e:
                    logging.info(e)

                mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
                          "Comment": custComment} # here we are creating a dict and keeping all data in that dict .we are
                                                 # we are creating everytime new dict .
                reviews.append(mydict)   # and apending that dict to a list called reviews.
            logging.info("log my final result {}".format(reviews))

            # for estabulushing connection to mongoDB copy url from mongoDB and paste it .and chnage its passward with your mongoDB 
            # passward.i.e ('shindesanjana2003')
            
            client = pymongo.MongoClient("mongodb+srv://shindesanjana2003:shindesanjana2003@cluster0.ecq9kjk.mongodb.net/?retryWrites=true&w=majority")
            # cut this 'db = client.test'
            db=client['review_scrapper'] # here we are creating data base and giving it's name as 'review-scrapper'
            review_coll=db['review_scrapper_data']  # here we are creating collections.
            review_coll.insert_many(reviews) # here we are inserting reviews .in reviews all reviews are stored . for running 
                                         # just go in terminal and write python app.py



            return render_template('result.html', reviews=reviews[0:(len(reviews)-1)])  # here we are calling 'result.html' & 
                                                                  # separating each reviews and appending it 
        except Exception as e:
            logging.info(e)
            return 'something is wrong'  # it will return this if you entered somthing that product does'nt exists
    # return render_template('results.html')

    else:
        return render_template('index.html') # if 'if statement' fells to excecute means method is not 'post' then it will return
                                           # 'index.html'


if __name__=="__main__":
    app.run(host="0.0.0.0" ,port=8000)

    