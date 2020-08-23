# Coffee Counter

A static site rendered from Airtable that shows the coffees I have consumed.

Hosted at [coffee.jamesg.app](https://coffee.jamesg.app).

## Screenshot

![A photo of the Coffee Counter website](https://github.com/jamesgoca/coffee-counter/blob/master/screenshot.png?raw=true)

## Installation

First, clone this repository:

```
git clone https://github.com/jamesgoca/coffee-counter
cd jamesg-coffee
```

Next, set up a virtual environment and install this project's required dependencies:

```
python3 -m venv venv
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Create a file called .env and add in your Airtable information:

```
token=AIRTABLE_API_KEY
url=BASE_URL
```

Execute app.py to run this project:

```
python3 app.py
```

## License

This project is licensed under an MIT License. View the license in [LICENSE](https://github.com/jamesgoca/coffee-counter/blob/master/LICENSE).