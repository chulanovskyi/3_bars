import json


def load_data(filepath):
    with open(filepath, encoding='utf8') as file:
        json_file = json.loads(file.read())
    return json_file
        

def get_biggest_bar(data):
    biggest_bar = dict()
    for bar in data:
        if biggest_bar:
            if bar['Cells']['SeatsCount'] > biggest_bar['Cells']['SeatsCount']:
                biggest_bar.clear()
                biggest_bar.update(bar)
        else:
            biggest_bar.update(bar)
    print('Biggest bar is:\n{bar}'.format(bar=biggest_bar['Cells']['Name']))
    print(biggest_bar['Cells']['Address']+'\n')
    return biggest_bar


def get_smallest_bar(data):
    smallest_bar = dict()
    for bar in data:
        if smallest_bar:
            if bar['Cells']['SeatsCount'] < smallest_bar['Cells']['SeatsCount']:
                smallest_bar.clear()
                smallest_bar.update(bar)
        else:
            smallest_bar.update(bar)
    print('Smallest bar is:\n{bar}'.format(bar=smallest_bar['Cells']['Name']))
    print(smallest_bar['Cells']['Address']+'\n')
    return smallest_bar


def get_closest_bar(data, longitude, latitude):
    closest_bar = dict()
    for bar in data:
        if closest_bar:
            bar_coords = bar['Cells']['geoData']['coordinates']
            closest_coords = closest_bar['Cells']['geoData']['coordinates']
            bar_delta = sum([abs(bar_coords[0] - longitude), abs(bar_coords[1] - latitude)])
            closest_delta = sum([abs(closest_coords[0] - longitude), abs(closest_coords[1] - latitude)])
            if bar_delta < closest_delta:
                closest_bar.clear()
                closest_bar.update(bar)
        else:
            closest_bar.update(bar)
    print('Closest bar to you is:\n%s' % closest_bar['Cells']['Name'])
    print(closest_bar['Cells']['Address'])
    return closest_bar

if __name__ == '__main__':
    data = load_data('Bars.json')
    get_biggest_bar(data)
    get_smallest_bar(data)
    get_closest_bar(data, 37.502862999552, 55.742721000053)
