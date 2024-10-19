from flask import Flask, redirect
import subprocess
import time
import os

app = Flask(__name__)

@app.route('/')
def redirect_to_htop():
    return redirect('/htop')

@app.route('/htop')
def display_htop():
    user_name = os.getenv('USER') or os.getenv('USERNAME')
    server_time_ist = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time() + 5.5 * 3600))
    system_info = subprocess.getoutput('top -b -n 1')
    
    return f"""
    <html>
    <body>
        <h1>System Information</h1>
        <p>Name: Dibya Jyoti Mahanta</p>
        <p>Username: {user_name}</p>
        <p>Server Time (IST): {server_time_ist}</p>
        <pre>{system_info}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)