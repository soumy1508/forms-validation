from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <body>
        <form action="/hello" method="post">
            <lable for="firstname">Firstname</lable>
            <input id="firstname" type="text" name="firstname" />
            <input type="submit" />
        </form>
    </body>
</html>
"""


@app.route("/")
def index():
    return form


@app.route("/hello", methods=['GET','POST'])
def hello():
    firstname = request.form['firstname']
    return '<h1>Hello,' + firstname + '<h1>'


time_form = """
<style>
.error {{ color:red; }}
</style>
<h1>Validate time</h1>
<form method="POST">
    <ladel>Hours (24 hour format)
    <input name="hours" type="text" value="{hours}" />

    </label>
    <p class="error">{hours_error}</p>
    <ladel>Minutes
    <input name="minutes" type="text" value="{minutes}" />

    </label>
    <p class="error">{minutes_error}</p>
    <input type="submit" value="convert" />
    
</form>
"""
@app.route('/validate-time')
def display_time_form():
    return time_form.format(hours="",hours_error="",
                    minutes="",minutes_error="")

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False



@app.route('/validate-time', methods=['POST'])
def validate_time():
    hours = request.form['hours']
    minutes = request.form['minutes']

    hours_error = ''
    minutes_error = ''

    if not is_integer(hours):
        hours_error = "Not a valid integer"
        hours = ''
    else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = 'Hour value out of range(0-23)'
            hours = ''


    if not is_integer(minutes):
        minutes_error = "Not a valid integer"  
        minutes = ''
    else:
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = 'minute value out of range(0-59)' 
            minutes = ''


    if not minutes_error and not hours_error:
        return "Success"
    else:
        return time_form.format(hours_error=hours_error,hours=hours,
                           minutes_error=minutes_error,minutes=minutes)       

app.run()