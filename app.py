from flask import Flask, request, jsonify, render_template
# from model import career
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

def career(pred): 
  careers = ['BBA- Bachelor of Business Administration',
       'BEM- Bachelor of Event Management',
       'Integrated Law Course- BA + LL.B',
       'BJMC- Bachelor of Journalism and Mass Communication',
       'BFD- Bachelor of Fashion Designing',
       'BBS- Bachelor of Business Studies',
       'BTTM- Bachelor of Travel and Tourism Management',
       'BVA- Bachelor of Visual Arts', 'BA in History',
       'B.Arch- Bachelor of Architecture',
       'BCA- Bachelor of Computer Applications',
       'B.Sc.- Information Technology', 'B.Sc- Nursing',
       'BPharma- Bachelor of Pharmacy', 'BDS- Bachelor of Dental Surgery',
       'Animation, Graphics and Multimedia', 'B.Sc- Applied Geology',
       'B.Sc.- Physics', 'B.Sc. Chemistry', 'B.Sc. Mathematics',
       'B.Tech.-Civil Engineering',
       'B.Tech.-Computer Science and Engineering',
       'B.Tech.-Electronics and Communication Engineering',
       'B.Tech.-Electrical and Electronics Engineering',
       'B.Tech.-Mechanical Engineering', 'B.Com- Bachelor of Commerce',
       'BA in Economics', 'CA- Chartered Accountancy',
       'CS- Company Secretary', 'Diploma in Dramatic Arts', 'MBBS',
       'Civil Services', 'BA in English', 'BA in Hindi', 'B.Ed.']
  result = []
  for i in list(pred):
       result.append(careers[i])

       return result
  
@app.route('/')
def home():
    return '''
    <h1>Welcome to the Career Recommendation System</h1>
    <form action="/predict" method="post">
        Do you like drawing? (yes = 1, no = 0) <input type="number" name="drawing"> <br>
        Do you like sport? (yes = 1, no = 0) <input type="number" name="sport"> <br>
        Do you like coding? (yes = 1, no = 0) <input type="number" name="coding"> <br>
        Do you like physics? (yes = 1, no = 0) <input type="number" name="physics"> <br>
        Do you like economics? (yes = 1, no = 0) <input type="number" name="economics"> <br>
        Do you like geography? (yes = 1, no = 0) <input type="number" name="geography"> <br>
        Do you like science? (yes = 1, no = 0) <input type="number" name="science"> <br>
        <input type="submit" value="Submit"> <br>
    </form>
    '''

# Define API endpoint for career prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Load the saved model
    model = joblib.load('career_prediction_model.joblib')

    # Input data (use request.form for POST requests)
    drawing = int(request.form.get('drawing'))
    sport = int(request.form.get('sport'))
    coding = int(request.form.get('coding'))
    physics = int(request.form.get('physics'))
    economics = int(request.form.get('economics'))
    geography = int(request.form.get('geography'))
    science = int(request.form.get('science'))

    # Inputs
    input_data = {
        'Drawing': drawing,
        'Singing': 0,
        'Sports': sport, 
        'Video Game': 0, 
        'Acting': 0, 
        'Travelling': 0,
        'Gardening': 0, 
        'Animals': 0, 
        'Photography': 0, 
        'Teaching': 0, 
        'Coding': coding,
        'Electricity Components': 0, 
        'Mechanic Parts': 0, 
        'Computer Parts': 0,
        'Researching': 0, 
        'Architecture': 0, 
        'Historic Collection': 0, 
        'Botany': 0,
        'Physics': physics, 
        'Accounting': 0, 
        'Economics': economics, 
        'Sociology': 0, 
        'Geography': geography,
        'Psycology': 0, 
        'History': 0, 
        'Science': science, 
        'Chemistry': 0,
        'Mathematics': 0 , 
        'Biology': 0, 
        'Designing': 0, 
        'Content writing': 0,
        'Crafting': 0, 
        'Literature': 0, 
        'Reading': 0, 
        'Cartooning': 0, 
        'Debating': 0,
        'Asrtology': 0, 
        'English': 0, 
        'Solving Puzzles': 0, 
        'Pharmisist': 0, 
        'Knitting': 0, 
        'Director': 0, 
        'Journalism': 0, 
        'Bussiness': 0,
        'Listening Music': 0, 
        'Languages': 0
    }

        # Convert the input data into a DataFrame
    input_df = pd.DataFrame([input_data])

    # Perform prediction using the loaded model
    prediction = model.predict(input_df)
    
    # Get the career result based on the prediction
    career_result = career(prediction)

    # Return the result as a JSON response
    return f'''
    <h1>Your Career Recommendation</h1>
    <p>Based on your inputs, we recommend the following career:</p>
    <h3>{career_result[0]}</h3>
    <a href="/">Go back to the form</a>
    '''

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
