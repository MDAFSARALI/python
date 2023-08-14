from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello,World !'

if __name__=="__main__":
    app.run(debug=True)
# The above line has created a server which write (contain)------->Hello, World !
# After running the code a link will be created ctrl+click on the link then a server will be start
# Where we acn see the Hello,World !