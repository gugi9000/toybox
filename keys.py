import keyboard

while True:
    try: 
        if keyboard.is_pressed('w'):
            print('up')
        if keyboard.is_pressed('a'):
            print('left')
        if keyboard.is_pressed('s'):
            print('down')
        if keyboard.is_pressed('d'):
            print('right')
        if keyboard.is_pressed('q'):
            break
        else:
            pass
    except:
        break
