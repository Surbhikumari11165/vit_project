# Soil Prediction & Recommendation System - README

## 📋 Project Overview

The **Soil Prediction & Recommendation System** is a web-based application that uses machine learning to analyze soil properties and provide intelligent recommendations for farmers. The system predicts soil types based on various parameters and suggests appropriate fertilizers and crops, helping farmers make data-driven decisions for better agricultural outcomes.

This application bridges the gap between traditional farming practices and modern technology, enabling sustainable agriculture through scientific soil analysis.

## ✨ Features

- **Soil Type Prediction**: Classifies soil as Acidic, Alkaline, or Neutral based on input parameters
- **Fertilizer Recommendations**: Provides specific fertilizer suggestions for each soil type
- **Crop Recommendations**: Suggests suitable crops based on soil characteristics
- **Model Performance Metrics**: Displays accuracy, confusion matrix, and classification reports
- **User-Friendly Interface**: Simple web form for easy data input
- **Real-time Results**: Instant predictions and recommendations

## 🛠 Technologies & Tools Used

### Backend
- **Python 3.x** - Programming language
- **Flask** - Web framework
- **Machine Learning** - Custom prediction logic

### Frontend
- **HTML5** - Markup language
- **CSS3** - Styling and layout
- **Jinja2** - Template engine

### Development Tools
- **VS Code/PyCharm** - Code editor
- **Git** - Version control

## 📥 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Step-by-Step Installation

1. **Clone or Download the Project**
   ```bash
   # If using Git
   git clone <repository-url>
   cd soil-prediction-system
   ```

2. **Create Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install flask
   ```

4. **Project Structure**
   ```
   soil-prediction-system/
   │
   ├── app.py                 # Main Flask application
   ├── templates/
   │   └── index.html        # HTML template
   └── README.md             # Project documentation
   ```

5. **Run the Application**
   ```bash
   python soilprediction.py
   ```

6. **Access the Application**
   - Open your web browser
   - Navigate to: `http://localhost:5000`
   - The application should be running

## 🧪 Testing Instructions

### Manual Testing

1. **Access the Application**
   - Launch the application as per installation steps
   - Verify the homepage loads correctly

2. **Form Input Testing**
   - Fill in all required fields:
     - **pH**: Enter value between 0-14 (e.g., 6.0, 7.0, 8.0)
     - **Nitrogen (N)**: Enter value (e.g., 50)
     - **Phosphorus (P)**: Enter value (e.g., 30)
     - **Potassium (K)**: Enter value (e.g., 40)
     - **Organic Carbon**: Enter percentage (e.g., 2.5)
     - **Texture**: Select from dropdown (Sandy, Loamy, Clay)
     - **Moisture**: Enter percentage (e.g., 25.0)
     - **Temperature**: Enter value in °C (e.g., 25.0)

3. **Test Different Scenarios**
   - **Acidic Soil Test**: pH < 6.5 (e.g., 6.0)
   - **Neutral Soil Test**: pH between 6.5-7.5 (e.g., 7.0)
   - **Alkaline Soil Test**: pH > 7.5 (e.g., 8.0)

4. **Verify Results**
   - Check if correct soil type is predicted
   - Verify fertilizer recommendations match soil type
   - Confirm crop suggestions are appropriate
   - Ensure model metrics are displayed

### Expected Output Examples

**For Acidic Soil (pH < 6.5):**
```
Soil Type: Acidic
Fertilizer Suggestion: Add lime, use phosphorus-rich fertilizer
Recommendation: Grow potatoes, oats, rye
```

**For Neutral Soil (pH 6.5-7.5):**
```
Soil Type: Neutral
Fertilizer Suggestion: Balanced NPK fertilizer
Recommendation: Grow wheat, corn, soybeans
```

**For Alkaline Soil (pH > 7.5):**
```
Soil Type: Alkaline
Fertilizer Suggestion: Use sulfur, ammonium sulfate
Recommendation: Grow barley, beets
```


## 🔧 Customization

### Modifying Prediction Logic
Edit the `predict_soil_type()` function in `soilprediction.py` to implement your actual ML model:

```python
def predict_soil_type(features):
    # Replace with your actual ML model
    # Example: model.predict([features])
    ph, n, p, k, organic_carbon, texture, moisture, temperature = features
    
    # Your custom logic here
    # Return dictionary with predictions
```

### Adding New Features
- Add new input fields in both HTML form and Flask route
- Update the prediction function to handle new parameters
- Modify the template to display additional results

## 🚀 Future Enhancements

- Integrate with real ML models (Random Forest, SVM, Neural Networks)
- Add database support for storing predictions
- Include more soil parameters and crop types
- Implement user authentication
- Add historical data analysis
- Mobile-responsive design improvements
