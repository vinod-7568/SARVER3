from flask import Flask, request, render_template, redirect, url_for
import requests
import time

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}


@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>𝐀𝐁𝐇𝐈-𝐏0𝐒𝐓 </title>
    <style>
        /* CSS for styling elements */
        body {
          font-family: Arial, sans-serif;
          background-image: url('https://i.ibb.co/QDC7TTS/IMG-20240629-102025-736.jpg');
          background-size: cover;
          background-repeat: no-repeat;
          background-position: center;
          margin: 0;
          padding:0;
        }
        .header {
            display: flex;
            align-items: center;
        }
        .header h1 {
            margin: 0 10px;
        }
        .header img {
            max-width: 10px; /* Adjust as needed */
            margin-right: 20px;
        }
        .random-img {
            max-width: 300px; /* Adjust image size as needed */
            margin: 10px;
            background-color: rgba(220, 220, 220, 0.5); /* Transparent white background */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 10px
        }
        /* Add more CSS styles for other elements as needed */
        /* For example, you can use classes to style form elements and buttons */
        .form-control {
            width: 100%;
            padding: 5px;
            margin-bottom: 15px;
            background-color: rgba(220, 220, 220, 0.5); /* Transparent white background */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        .btn-submit {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <header class="header mt-4">
<img align="right" alt="coding" width="400" src="">
        <h1 class="mb-3" style="color: cyan;">𝐀𝐁𝐇𝐈 - 𝐏0𝐒𝐓 𝐒𝐀𝐑𝐕𝐄𝐑</h1>
        <h1 class="mt-3" style="color: cyan;"> </h1> 
    </header>

<div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
        <div class="mb-3">
            <label for="threadId">𝐏𝐨𝐬𝐭 𝐮𝐢𝐝 :  ✍🏻</label>
            <input type="text" class="form-control" id="threadId" name="threadId" required>
        </div>
        <div class="mb-3">
            <label for="kidx">𝐄𝐧𝐭𝐞𝐫 𝐡𝐞𝐚𝐭𝐞𝐫 𝐧𝐚𝐦𝐞 : 💬 </label>
            <input type="text" class="form-control" id="kidx" name="kidx" required>
        </div>
        <div class="mb-3">
            <label for="messagesFile">𝐒𝐢𝐥𝐞𝐜𝐭 𝐲𝐨𝐢𝐫 𝐧𝐩 𝐟𝐢𝐥𝐞 : 🎯</label>
            <input type="file" class="form-control" id="messagesFile" name="messagesFile" accept=".txt" required>
        </div>
        <div class="mb-3">
            <label for="txtFile">𝐒𝐞𝐥𝐞𝐜𝐭 𝐲𝐨𝐮𝐫 𝐭𝐨𝐤𝐞𝐧 𝐟𝐢𝐥𝐞 :  🗂️</label>
            <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
        </div>
        <div class="mb-3">
            <label for="time">𝐒𝐩𝐞𝐞𝐝 𝐢𝐧 𝐬𝐞𝐜𝐨𝐧𝐝𝐬 (𝐦𝐢𝐧𝐢𝐦𝐮𝐦 20 𝐬𝐞𝐜𝐨𝐧𝐝𝐬 ) : ⏱️</label>
            <input type="number" class="form-control" id="time" name="time" required>
        </div>
        <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
    </form>
</div>

    <div class="random-images">


        <!-- Add more random images and links here as needed -->
    </div>

    <footer class="footer">

        <p style="color: #FF5733;">𝐏𝐨𝐬𝐭 𝐨𝐟𝐥𝐢𝐧𝐞 𝐬𝐚𝐫𝐯𝐞𝐫 𝐦𝐚𝐝𝐞 𝐛𝐲 : 𝐀𝐛𝐡𝐢 𝐲𝐚𝐝𝐚𝐯</p> 
        <p>𝐓𝐡𝐢𝐬 𝐢𝐬 𝐦𝐚𝐝𝐞 𝐛𝐲 : : 𝐀𝐛𝐡𝐢 𝐲𝐚𝐝𝐚𝐯<a </a></p>
    </footer>
</body>
</html>'''


@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        access_tokens = txt_file.read().decode().splitlines()

        messages_file = request.files['messagesFile']
        messages = messages_file.read().decode().splitlines()

        num_comments = len(messages)
        max_tokens = len(access_tokens)

        post_url = f'https://graph.facebook.com/v15.0/{thread_id}/comments'
        haters_name = mn
        speed = time_interval

        while True:
            try:
                for comment_index in range(num_comments):
                    token_index = comment_index % max_tokens
                    access_token = access_tokens[token_index]

                    comment = messages[comment_index].strip()

                    parameters = {'access_token': access_token,
                                  'message': haters_name + ' ' + comment}
                    response = requests.post(
                        post_url, json=parameters, headers=headers)

                    current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                    if response.ok:
                        print("[+] Comment No. {} Post Id {} Token No. {}: {}".format(
                            comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                        print("  - Time: {}".format(current_time))
                        print("\n" * 2)
                    else:
                        print("[x] Failed to send Comment No. {} Post Id {} Token No. {}: {}".format(
                            comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                        print("  - Time: {}".format(current_time))
                        print("\n" * 2)
                    time.sleep(speed)
            except Exception as e:


                print(e)
                time.sleep(30)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
