## Compound Interest Calculator Flask App
This is a Flask web application that demonstrates calculating compound interest with both example problems and an interactive user input form.

## Features
Displays multiple solved example problems with principal, rate, time, and computed amount.

Provides a user-friendly web form where users can input their own principal, interest rate, and time to compute compound interest dynamically.

Uses a clear mathematical formula presentation format while preserving the CSS styling in the separate interestcompounded.html template.

Separates backend logic (Flask + Python) from frontend layout (HTML + CSS) for easy customization and extension.

Getting Started


## Prerequisites

Python 3.x installed

Flask installed (pip install flask)

Running the Application
Clone or download this repository.

## Ensure the directory structure is:

project/
│
├── app.py
└── templates/
    └── interestcompounded.html

## Run the Flask server with:

bash
python app.py
Open your browser and navigate to:

http://127.0.0.1:5000/ to view pre-solved examples.

http://127.0.0.1:5000/user to enter custom values and calculate compound interest interactively.

## How to Use
Viewing Examples: The root page shows example compound interest calculations with fixed principals, rates, and times.

## Interactive Form: Use the /user page to input your own numbers. Fill out principal, rate (%), and years, then click "Calculate" to see your result.

## Technologies Used
Flask (Python web framework)

Jinja2 (HTML templating engine)

HTML5 and CSS3 (for clean layout and styling)

## Extend and Customize
Modify interestcompounded.html to change the look or add more steps in the calculation display.

Enhance app.py to add extra financial formulas, input validation, or database storage.

##License
This project is open source and free to use for educational or demonstration purposes.