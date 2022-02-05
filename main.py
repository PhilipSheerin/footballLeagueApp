from website import create_app

app = create_app()

#Run web server
if __name__ == '__main__':
    #rerun when changes are made
    app.run(debug=True)