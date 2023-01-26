from flask import Flask, render_template, flash, request, redirect 
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes


app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


c = CurrencyRates(force_decimal=False)
cc = CurrencyCodes()

@app.route("/")
def homepage():
    """show homepage"""

    return render_template('home.html')


@app.route("/result", methods=["POST"])
def display_result():
    """ displays form for input"""

    input_currency = request.form["inputcurrency"]
    output_currency = request.form["outputcurrency"]

    try:
        input_amount = float(request.form["amount"])

        input_symbol = cc.get_symbol(input_currency)
        output_symbol = cc.get_symbol(output_currency)
        input_name = cc.get_currency_name(input_currency)
        output_name = cc.get_currency_name(output_currency)

        converted = c.convert(input_currency, output_currency, input_amount)
        converted = format(converted, ".2f")
        amount = format(input_amount, ".2f")

    
        return render_template('results.html', amount=amount,
            converted=converted,
            input_symbol=input_symbol,
            output_symbol=output_symbol,
            input_name=input_name,
            output_name=output_name,)

    except ValueError:
        flash("Error: Please input a number or decimal for the amount", "error")
        return redirect("/")
    except Exception as err:
        print(err)
        err = str(err)
        if err == "Currency Rates Source Not Ready":
            flash("Error: Not an acceptable currency! Please try again", "error")
        return redirect("/")

   