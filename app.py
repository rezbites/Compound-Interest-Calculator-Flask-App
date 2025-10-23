from flask import Flask, render_template, request

app = Flask(_name_)

# Two solved example problems
problem_examples = [
    {
        "principal": 8000,
        "rate": 10,
        "years": 2,
        "amount": round(8000 * (1 + 10/100) ** 2, 2)
    },
    {
        "principal": 10000,
        "rate": 12,
        "years": 3,
        "amount": round(10000 * (1 + 12/100) ** 3, 2)
    }
]

@app.route("/")
def index():
    # Show two solved examples (no form)
    return render_template(
        "interestcompounded.html",
        examples=problem_examples,
        user_input=False
    )
    
@app.route("/user", methods=["GET", "POST"])
def user():
    if request.method == "POST":
        principal = float(request.form["principal"])
        rate = float(request.form["rate"])
        years = float(request.form["years"])
        amount = round(principal * (1 + rate/100) ** years, 2)
        return render_template(
            "interestcompounded.html",
            principal=principal,
            rate=rate,
            years=years,
            amount=amount,
            user_input=False,
            result=f"{amount}"
        )
    
    # GET: Show input form only
    return render_template(
        "interestcompounded.html",
        principal='',
        rate='',
        years='',
        amount='',
        user_input=True,
        result=None
    )

if _name_ == "_main_":
    app.run(debug=True)
