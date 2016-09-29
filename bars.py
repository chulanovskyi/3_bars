import json
import operator


def load_data(filepath):
    with open(filepath, encoding='utf8') as json_file:
        data = json.load(json_file)
    return data


def get_biggest_bar(data):
    bars_ids_and_seats = {bar['Id']: bar['Cells']['SeatsCount'] for bar in data}
    big_bar_id, big_bar_seats = max(bars_ids_and_seats.items(), key=operator.itemgetter(1))
    biggest_bar = next(bar for bar in data if bar['Id'] == big_bar_id)
    return biggest_bar


def get_smallest_bar(data):
    bars_ids_and_seats = {bar['Id']: bar['Cells']['SeatsCount'] for bar in data}
    small_bar_id, small_bar_seats = min(bars_ids_and_seats.items(), key=operator.itemgetter(1))
    smallest_bar = next(bar for bar in data if bar['Id'] == small_bar_id)
    return smallest_bar


def get_closest_bar(data):
    user_location = get_user_coordinates()
    if not user_location:
        return
    closest_bar = dict()
    for bar in data:
        if closest_bar:
            bar_location = bar['Cells']['geoData']['coordinates']
            closest_bar_location = closest_bar['Cells']['geoData']['coordinates']
            bar_distance = find_distance_between_points(bar_location, user_location)
            closest_bar_distance = find_distance_between_points(closest_bar_location, user_location)
            if bar_distance < closest_bar_distance:
                closest_bar = bar
        else:
            closest_bar = bar
    return closest_bar


def get_user_coordinates():
    longitude = input('Enter longitude: ')
    latitude = input('Enter latitude: ')
    try:
        coordinates = (float(longitude),float(latitude))
        return coordinates
    except ValueError:
        print('Enter digits only')


def find_distance_between_points(point_1, point_2):
    point_1_x, point_1_y = point_1
    point_2_x, point_2_y = point_2
    return sum([abs(point_1_x - point_2_x), abs(point_1_y - point_2_y)])


def print_bar_info(bar, head=None):
    if head:
        print(head)
    if bar:
        print('Name: %s' % bar['Cells']['Name'])
        print('Address: %s' % bar['Cells']['Address'])
        print('Location: %s\n' % bar['Cells']['geoData']['coordinates'])


if __name__ == '__main__':
    data = load_data('Bars.json')

    print_bar_info(get_biggest_bar(data), 'Biggest bar is:')
    print_bar_info(get_smallest_bar(data), 'Smallest bar is')
    print_bar_info(get_closest_bar(data), 'Closest bar to you is:')
