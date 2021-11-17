import math, random

def show(app, canvas, w, h):
        canvas.create_text(w // 2, h // 4, text='Scoreboard', font='PressStart2P 25', fill='black')
        scores = read()
        print(scores)
        spacing = 40

        for i in range(min(10, len(scores))):
                canvas.create_text((w // 2) - 40, (h // 4) + spacing, text = scores[i][0], font='PressStart2P 20', fill='#424242')
                canvas.create_text((w // 2) + 40, (h // 4) + spacing, text = scores[i][1], font='PressStart2P 20', fill='green')
                spacing += 30

def write():
        pass

def read():
        # from https://stackoverflow.com/questions/32327936/how-to-load-data-from-a-csv-file-without-importing-the-csv-module-library
        with open('scores.csv', 'r') as f:
                results = []
                for line in f:
                        words = line.split(',')
                        results.append((words[0], int(words[1][:len(words[1])-1])))
                return results