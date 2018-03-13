builds = [('Rhino','link1'),('Loki','link2'),('Banshee','link3'),('Vauban','link4')]


if str(message.content).startswith('!build'):
        segunda=str(message.content).split()[1]
        if segunda in builds:
            print('ediajd')