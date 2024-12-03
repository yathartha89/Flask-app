from flask import Flask, render_template, request, jsonify

import os

import json

import subprocess

app = Flask(__name__)

@app.route('/')

def index():

  return  render_template('index.html')

@app.route('/run_script', methods=["POST"])

def run_script():

   org_dir = os.getcwd()

   script_name = request.form.get('script_name')

   os.chdir('scripts')

   if not  os.path.isfile(script_name):

      return jsonify({'Status': 'Error', 'output': script_name})

   else:

      try:


         script_path = os.path.join('scripts', script_name)

         os.chdir(org_dir)

         result = subprocess.check_output(['python3', script_path],text=True)

         if not result:

            result = "The code is executed successfully but no output is produced"

         return jsonify({'Status': 'Success', 'Output': result})

      except subprocess.CalledProcessError as e:

         error_output = e.output.decode('utf-8') if isinstance(e.output, bytes) else str(e.output)

         return jsonify({'Status': 'Failed', 'result': error_output})

      except Exception as e:

         return jsonify({'Status': 'Error', 'output': str(e)})

if __name__ == '__main__':

   app.run(debug=True)

         

  

   


