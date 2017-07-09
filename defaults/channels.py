CHANNELS = {
    1 : [0, {
        'title': 'nxtv',
        'caspar_host': '192.168.32.185',
        'day_start': [6, 0],
        'send_action': 1,
        'rundown_accepts': "asset['id_folder'] <= 10 and asset['content_type'] == VIDEO",
        'scheduler_accepts': "asset['id_folder'] in [1, 2]",
        'caspar_port': 5250,
        'fps': 25,
        'plugins': [
                'logo',
                'music_label',
                'publish',
                'subtitle',
                'templates',
                'ticker',
                'breaking_news'
            ],
        'playout_spec': 'id_playout/1',
        'caspar_channel': 1,
        'feed_layer': 10
    }]
}
