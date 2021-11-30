import copy
def show(app, canvas, w, h):
        #this font from: https://fonts.google.com/specimen/Press+Start+2P
        canvas.create_text(w // 2, h // 4, text='Scoreboard', font='PressStart2P 25', fill='black')
        canvas.create_text(w // 2, h // 4 + 30, text='golf scoring', font='PressStart2P 15', fill='black')
        scores = sortScores(app.results)
        spacing = 60

        for i in range(min(10, len(scores))):
                #this font from: https://fonts.google.com/specimen/Press+Start+2P
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
        result = copy.deepcopy(L)
        for i in range (0, len(result)):
                for j in range (i,  len(result)):
                        if result[i][1] > L[j][1]: 
                                (result[i], result[j]) = (result[j], result[i])
        return result

#got help from https://www.w3schools.com/python/python_file_write.asp for read/write functions
def writeScores(app, username, score):
        app.results.append((username, score))
        csvFile = open('scores.csv', 'w')
        for element in app.results:
                csvFile.write(f'{element[0]},{str(element[1])}\n')
        csvFile.close()

def readScores():
        csv =  open('scores.csv', 'r')
        results = []
        for line in csv:
                words = line.split(',')
                results.append((words[0], int(words[1][:len(words[1])])))
        return results