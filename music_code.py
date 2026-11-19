print('this is your music app playlist recomendor')
mood = input('enter your mood happy,sad or relaxed ')
weather = input ('enter the waether sunny or rainy ')
if mood == 'happy':
    if weather == 'sunny':
        print ('top hits playlist')
if mood == 'happy':
    if weather == 'rainy':
        print ('top charts playlist')
if mood == 'sad':
    if weather == 'rainy':
        print ('sad acoustic playlist')
if mood == 'sad':
    if weather == 'sunny':
        print ('top charts playlists')
if mood == 'relaxed':
        print ('chill vibes playlist')
if mood != 'happy''sad''relaxed':
    print('top charts')