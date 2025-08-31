from flask import Flask,render_template, request
import pickle
import numpy as np
popular_DF=pickle.load(open('popularDF.pkl','rb'))
Books=pickle.load(open('Books.pkl','rb'))
Our_Data_Table=pickle.load(open('Our_Data_Table.pkl','rb'))
Similarity_score=pickle.load(open('Similarity_score.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')




@app.route('/home')

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

@app.route('/recommendedBooks', methods=['post'])
def recommend():
    UserInput= request.form.get('UserInput')
    index=np.where(Our_Data_Table.index==UserInput)[0][0]
    similar_items=sorted(list(enumerate(Similarity_score[index])), key=lambda x: x[1], reverse=True)[1:11]
    data=[]
    for i in similar_items:
        item=[]
        temp_DF=Books [ Books['Book-Title']==Our_Data_Table.index[i[0]]]
        item.extend(list(temp_DF.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_DF.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_DF.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        data.append(item)
    print(data)
    return render_template('recommend.html' , data=data)
    
  

if __name__ =='__main__':
    app.run(debug=True) 