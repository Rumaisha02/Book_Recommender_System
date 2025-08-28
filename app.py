from flask import Flask,render_template
import pickle
popular_DF=pickle.load(open('popularDF.pkl','rb'))

app=Flask(__name__)
@app.route('/')

def index():
    return render_template('index.html',
                           book_Name=list(popular_DF['Book-Title'].values),
                           book_Author=list(popular_DF['Book-Author'].values),
                          yearOfPublication=list(popular_DF['Year-Of-Publication'].values),
                          imageURLM=list(popular_DF['Image-URL-M'].values),
                         noOfRating=list(popular_DF['No of Rating'].values),
                          avg_Rating=list(popular_DF['Avg_Rating'].values),
                           )

@app.route('/recommendations')
def recommendUI():
    return render_template('recommend.html')
  

if __name__ =='__main__':
    app.run(debug=True)