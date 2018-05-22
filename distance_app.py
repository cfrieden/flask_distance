from flask import Flask, abort, flash, redirect, render_template, request, url_for
from vincenty import vincenty
from service import distance_from

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'ghtyofewnh5678ngh3rt'

@app.route('/')
def show_form():
    return render_template('distance.html')

@app.route('/distance', methods=['POST','GET'])
def distance():

    #If post from form calculate from form values
    if request.method == 'POST':
        origin =(float(request.form['origin_longitude']), float(request.form['origin_latitude']))
        point = (float(request.form['longitude']), float(request.form['latitude']))
        flash('The point longitude : {0} and latitude : {1} is {2} km away'.format( request.form['longitude'], request.form['latitude'], distance_from(office,point)))
    #if get with query parameters
    elif request.method == 'GET':
        #make sure query parameters are provided
        if request.args.get('longitude') == None or request.args.get( 'latitude') == None or request.args.get('origin_longitude') == None or request.args.get( 'origin_latitude') == None:
            flash('Could not calculate please provide all logitude and latitude values')
            return redirect(url_for('show_form'))
        #make sure values are valid lat long
        elif not _valid_number(request.args.get('longitude'),-180,180,0.0000001) or not _valid_number(request.args.get('latitude'),-90,90,0.0000001) or not _valid_number(request.args.get('origin_longitude'),-180,180,0.0000001) or not _valid_number(request.args.get('origin_latitude'),-90,90,0.0000001):
            flash('Could not calculate please provide valid logitude and latitude values')
            return redirect(url_for('show_form'))
        origin = (float(request.args.get('origin_longitude')), float(request.args.get('origin_latitude')))
        point = (float(request.args.get('longitude')), float(request.args.get('latitude')))
        flash('The point longitude : {0} and latitude : {1} is {2} km away'.format( request.args.get('longitude'), request.args.get('latitude'), distance_from(office,point)))
    return redirect(url_for('show_form'))

def _valid_number(input,min,max,step):
    try:
        f = float(input)
        if f < min or f > max:
            return False
    except ValueError:
        print('bad value')
        return False
    return True


if __name__ == "__main__":
    app.run()
