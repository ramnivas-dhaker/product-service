import setup

app = setup.create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5558)
    # app.run(debug=True, host='0.0.0.0')
