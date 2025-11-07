import os
import random
from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/')
def redirect_to_site():
    sites = [
        "https://experiment-site-1j72.onrender.com",  # サイト1のURL
        "https://control-site.onrender.com"   # サイト2のURL
    ]
    chosen_site = random.choices(sites, weights=[0.4, 0.6], k=1)[0]
    return redirect(f"{chosen_site}/?from_redirect=1")

# ローカルテスト用（Renderでは不要）
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
