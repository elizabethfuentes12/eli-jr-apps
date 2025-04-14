# Unicorn Calculator: A Magical Web-Based Calculator with a Whimsical Theme

The Unicorn Calculator is a delightful web application that transforms basic arithmetic operations into a magical experience. Built with Flask, this calculator combines functional mathematics with an enchanting unicorn-themed interface, making calculations more enjoyable through its playful design and intuitive user experience.

The application features a responsive web interface with a colorful gradient background, animated buttons, and decorative unicorn elements. It supports four fundamental arithmetic operations (addition, subtraction, multiplication, and division) while handling edge cases like division by zero with user-friendly error messages. The calculator's design implements modern CSS features including gradients, transitions, and flexible layouts to create an engaging user interface.

## Repository Structure
```
calculadora_unicornio/          # Main application directory
├── app.py                      # Flask application entry point with calculator logic
├── requirements.txt            # Project dependencies (Flask 2.0.1)
├── static/                     # Static assets directory
│   └── estilo.css             # CSS styles for the unicorn theme
└── templates/                  # HTML templates directory
    └── calculadora.html        # Main calculator interface template
```

## Usage Instructions
### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd calculadora_unicornio
```

2. Create and activate a virtual environment:

**For MacOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**For Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Quick Start
1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

### More Detailed Examples

**Basic Arithmetic Operations:**
1. Addition:
   - Enter first number: 5
   - Enter second number: 3
   - Click the ➕ button
   - Result: 8

2. Division with Error Handling:
   - Enter first number: 10
   - Enter second number: 0
   - Click the ➗ button
   - Result: "¡No se puede dividir por cero!" (Cannot divide by zero!)

### Troubleshooting

**Common Issues:**

1. Application Won't Start
   - Error: `Address already in use`
   - Solution: 
     ```bash
     # Find and kill the process using the port
     lsof -i :5000  # On MacOS/Linux
     taskkill /F /PID <PID>  # On Windows
     ```

2. Static Files Not Loading
   - Check if the static folder is in the correct location
   - Verify file permissions
   - Clear browser cache
   - Debug using Flask's debug mode:
     ```python
     app.run(debug=True)
     ```

## Data Flow
The calculator processes user input through a simple request-response cycle, transforming numerical inputs into calculated results through Flask routes.

```ascii
[User Input] -> [Flask Route] -> [Calculation Logic] -> [Template Rendering] -> [Display Result]
   (Form)         (app.py)        (Operations)          (calculadora.html)      (Browser)
```

Key component interactions:
1. User submits form with two numbers and operation choice
2. Flask route captures POST request with form data
3. Application performs requested arithmetic operation
4. Error handling catches division by zero
5. Result is passed to template for rendering
6. Template displays result with unicorn-themed styling
7. Static assets (CSS, images) enhance visual presentation