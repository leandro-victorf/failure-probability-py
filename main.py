
from flask import Flask, render_template, request
from calculate import moment_of_inertia
from calculate import bending_moment
from calculate import calculate_the_permissible_voltage
from calculate import acting_tension
from calculate import performance_function
from calculate import failure_probability
app = Flask(__name__)


@app.route("/")
def input_values():
    return render_template('home.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    wingspan = float(request.form['Envergadura'])
    chord = float(request.form['Corda'])
    thickness = float(request.form['Espessura'])
    weight = float(request.form['Peso'])
    flow_limit = float(request.form['Limite'])
    force = float(request.form['Força'])
    inertia = moment_of_inertia(thickness, chord)
    moment = bending_moment(weight, force, wingspan)
    tensions_admissible = calculate_the_permissible_voltage(flow_limit)
    tension_acting = acting_tension(thickness, inertia, moment)
    performance_values = performance_function(tensions_admissible, tension_acting)
    return render_template('calculate.html', result=failure_probability(performance_values))
