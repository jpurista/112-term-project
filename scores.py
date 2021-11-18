def show(app, canvas, w, h):
        print('scores')
        canvas.create_text(w // 2, h // 4, text='Scoreboard', font='PressStart2P 25', fill='black')
        scores = sortScores(readScores())
        spacing = 40

        for i in range(min(10, len(scores))):
                canvas.create_text((w // 2) - 65, (h // 4) + spacing, text = shortenText(scores[i][0]), font='PressStart2P 20', fill='#424242')
                canvas.create_text((w // 2) + 100, (h // 4) + spacing, text = scores[i][1], font='PressStart2P 20', fill='green')
                spacing += 30

def shortenText(s):
        result = ''
        for letter in s:
                letter.strip()
        length = min(len(s), 5)
        result = s[:length]
        if length != len(s):
                result += '...'
        else:
                result += '   '
        return result

def sortScores(L):
        for i in range (0, len(L)):
                for j in range (i,  len(L)):
                        if L[i][1]< L[j][1]: 
                                L[i], L[j] = L[j], L[i]
        return L

def writeScores(app):
        pass

def readScores():
        # from https://stackoverflow.com/questions/32327936/how-to-load-data-from-a-csv-file-without-importing-the-csv-module-library
        with open('scores.csv', 'r') as f:
                results = []
                for line in f:
                        words = line.split(',')
                        results.append((words[0], int(words[1][:len(words[1])])))
                return results