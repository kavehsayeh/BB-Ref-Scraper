from bs4 import *
import requests, re

def BBRef_Scraper(outputFile, yearStart, yearEnd):
    page = open(outputFile, 'w')
    page.write('Year,Win.Score,Lose.Score,Total.Score\n')
    page.close()

    years = list(range(yearStart, yearEnd))
    urlTemplate = 'https://www.baseball-reference.com/leagues/MLB/{}-schedule.shtml'
    
    for year in years:
        page = requests.get(urlTemplate.format(year))
        
        schedule = BeautifulSoup(page.content, "html.parser")
        games = schedule.find_all("p", class_="game")

        out = open(outputFile, 'a')
        for game in games:
            observation = str(year) + ","
            scores = re.findall('\([\d]+\)', game.get_text())
            scores = [i.strip("()") for i in scores]
            scores.sort()
            
            # handles occassions when no scores are avaliable for the game
            if type(scores) != list or len(scores) == 0:
                continue
            
            loseScore = scores[0]
            winScore = scores[1]
            
            observation += winScore + "," + loseScore + "," + str(int(winScore)+int(loseScore)) + "\n"
            out.write(observation)
        out.close()

if __name__ == "__main__":
    BBRef_Scraper("MLB-years.csv", 1871, 2018)
