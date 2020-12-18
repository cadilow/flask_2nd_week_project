from random import shuffle

from flask import Flask, render_template

from data import title, subtitle, description, departures, tours


app = Flask(__name__)


@app.route("/")
def index():
    random_card = [i for i in range(1, 17)]
    shuffle(random_card)                        # generator of tours for index.html
    output = render_template(
        "index.html",
        title_main = title,
        subtitle = subtitle,
        description = description,
        departures = departures,
        tours = tours,
        random_card = random_card
        )
    return output


@app.route("/departures/<departure>/")
def flights(departure):
    count_departures = 0                        # count of tours in one direction
    numbers_of_toures = []                      # keys of dictionary "tours"
    count_nights = []                           # count of nights in each tour
    price_dictionary = []                       # all prices in one direction
    name_tour = ""                              # the end of the word "тур"
    for i in tours:
        if tours[i]["departure"] == departure:
            count_departures += 1
            numbers_of_toures.append(i)
            price_dictionary.append(tours[i]["price"])
            count_nights.append(tours[i]["nights"])
    if count_departures % 10 == 0 or 5 <= count_departures % 10 <= 9 or 11 <= count_departures % 100 <= 19:
        name_tour = "туров"
    elif count_departures % 10 == 1:
        name_tour = "тур"
    elif 2 <= count_departures % 10 <= 4:
        name_tour = "тура"
    output = render_template(
        "departure.html",
        title_main = title,
        departures = departures,
        departure = departure,
        count_departures = count_departures,
        name_tour = name_tour,
        price_dictionary = price_dictionary,
        count_nights = count_nights,
        numbers_of_toures = numbers_of_toures,
        tours = tours
        )
    return output


@app.route("/tours/<id>/")
def travel(id):
    output = render_template(
        "tour.html",
        title_main = title,
        departures = departures,
        tour = tours[int(id)],
        )
    return output


if __name__ == "__main__":
    app.run()
