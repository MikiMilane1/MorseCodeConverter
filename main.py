from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from code_form import UserInput
from morsecode_dict import dict_morse, tuples_morse
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
Bootstrap5(app)


# CREATE FUNCTION
def converter(user_input):
    character_list = list(dict_morse.keys())
    # CHECK IF TEXT OR MORSE CODE
    if user_input == '':
        return ''
    elif user_input[0].upper() in character_list:

        # CONVERT TEXT TO MORSE CODE
        converted_text = ''
        for character in user_input:
            if character == ' ':
                converted_character = '/'
            else:

                converted_character = [item2 for (item1, item2) in tuples_morse if character.upper() == item1][0]
            converted_text += converted_character + ' '

        # REMOVE THE UNNECESARY SPACE ADDED AFTER THE LAST CHARACTER
        converted_text = converted_text[:-1]
        return converted_text

    # CONVERT MORSE CODE TO TEXT
    elif user_input[0] in ['.', '-', '_']:
        user_input = user_input.replace('_', '-')
        # CONVERT MORSE CODE TO TEXT
        converted_code = ''

        # SPLIT INPUT INTO WORDS
        user_input_separated = user_input.split('/')
        for word in user_input_separated:
            # SPLIT WORD INTO LETTERS
            for letter in word.split(' '):
                try:
                    letter_converted = [item1 for (item1, item2) in tuples_morse if item2 == letter][0]
                except IndexError:
                    letter_converted = ' '
                converted_code += letter_converted
        converted_code = converted_code.replace('  ', ' ')
        return converted_code


@app.route('/', methods=["POST", "GET"])
def index():
    form = UserInput()
    if request.method == "POST" and form.validate_on_submit():
        user_input = form.userinput.data
        result = converter(user_input=user_input)
        if len(result) > 1:
            flash(result)
        elif result == '':
            flash('Please enter text or Morse Code you want converted')
        print(result)
        return redirect(url_for("index", result=result))

    else:
        return render_template('index.html', form=form, result='rgrgrg')


@app.route('/testing')
def testing():
    return render_template('testing.html')


if __name__ == "__main__":
    app.run(debug=True, port=5002)
