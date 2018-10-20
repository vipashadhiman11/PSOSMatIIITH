from highcharts import Highchart

chart = Highchart()

options = {
    'chart': {
        'type': 'bar',
        'zoomType': 'xy'
    },

    'title': {
        'text': 'Highchart Bar'
    },

    'legend': {
        'enabled': True
    },

   'xAxis': {
        'categories': ['User 1', 'User 2', 'User 3', 'User 4', 'User 5'],
        },

    'yAxis': {
        'title': {
            'text': 'Number of posts (thousands)'
        }  
    },

}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

var allProductsArray = db.restaurants.find().toArray();


data1 = [1070, 301, 6035, 2003, 200]
data2 = [1330, 0156, 9047, 4008, 600]
data3 = [9703, 9140, 40504, 7302, 340]
data4 = [105002, 9504, 40250, 7040, 308]

chart.set_dict_options(options)

chart.add_data_set(data1, 'bar', 'Day 1')
chart.add_data_set(data2, 'bar', 'Day 2')
chart.add_data_set(data3, 'bar', 'Day 3')
chart.add_data_set(data4, 'bar', 'Day 4')

chart.save_file('./highcharts-bar')
