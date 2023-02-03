from django.shortcuts import render

def game_view(request, game_id):
    context = {
        'round': 1,
        'players': [
            {   
                'name': 'Cactus',
                'avatar': 'images/cactus.jpg',
                'score': 10,
                'status': 'waiting',
                'tricks': '2/3',
            },
            {   
                'name': 'Cat',
                'avatar': 'images/cat.png',
                'score': 6,
                'status': 'waiting',
                'tricks': '1/4',
            },
            {
                'name': 'Rabbit',
                'avatar': 'images/rabbit.jpg',
                'score': 8,
                'status': 'active',
                'tricks': '4/5',
            },
            {
                'name': 'Me',
                'avatar': 'images/parrot.jpeg',
                'score': 12,
                'status': 'waiting',
                'tricks': '1/5',
            }
        ],
        'hand': [
            {   
                'value': '7 of spades',
                'image': 'images/cards/7 of spades.jpg',
            },
            {
                'value': 'Ace of clubs',
                'image': 'images/cards/Ace of clubs.jpg',
            },
            {   
                'value': 'Queen of clubs',
                'image': 'images/cards/Queen of clubs.jpg',
            },
            {
                'value': 'Ace of diamonds',
                'image': 'images/cards/Ace of diamonds.jpg',
            },
            {
                'value': 'Ace of diamonds',
                'image': 'images/cards/Ace of diamonds.jpg',
            }
        ],
        'pile': [
            {   
                'player': 'Cactus',
                'image': 'images/cards/7 of spades.jpg',
            },
            {   
                'player': 'Cat',
                'image': 'images/cards/Queen of clubs.jpg',
            }, None, None
        ]
    }
    return render(request, 'visual/base.html', context=context)