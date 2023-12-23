import pickle 
from flask import Flask, render_template, request

app = Flask(__name__)       #creating an instance of the class

model = pickle.load(open('model_file.pkl','rb'))


# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['GET','POST'])
# def predict_func():
#     # prediction = model.predict([[63,1,3,145,233,1,0,150,0,2.3,0,0,1]])

#     print('hello')

#     values = ['age', 'sex', 'cp','trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
#     sample = []

#     for v in values:
#         val = float(request.form.get(v))
#         if(v=='fbs'):
#             val=1 if float(request.form.get(v))>120 else 0
            
#         sample.append(val)

#     prediction = model.predict([sample])

#     print('prediction:',prediction)

#     if(prediction==[1]):
#         return render_template('result.html', prediction_result = f'You may be at a risk of a heart disease')
#     else:
#         return render_template('result.html', prediction_result = f'You seem to be healthy')



# if __name__=='__main__':
#     app.run(debug=True)


prediction = model.predict([[47,1,0,110,275,0,0,118,1,1,1,1,2]])
print('prediction:',prediction)
