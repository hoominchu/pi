import requests, json, sys, glob, mp3play
import datetime
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from datetime import timedelta
import pyaudio
import time

#import nltk
import speech_recognition as sr
import random
#from nltk import sent_tokenize, word_tokenize
#from nltk.stem import PorterStemmer
import serial
import pyttsx 

engine = pyttsx.init()

channelsDict = {'Z BANGLA CINEMA': 849, 'HBO': 345, 'STAR GOLD': 301, 'WB': 349, 'TARANG MUSIC': 975, 'ACTVE DOORDARSHAN': 700, 'ZEE TV HD': 118, 'SUDRSHAN NEWS': 477, 'Z KHANA KHAZANA': 582, 'MAA TV': 755, 'JAYA': 712, 'SHALOM TV': 889, 'DD PUNJABI': 961, 'SONY SIX HD': 420, 'VASANATH TV': 718, 'STAR WORLD': 201, 'CNN -IBN': 510, 'B4U MOVIES': 322, 'COLORS HD': 120, 'SUN TV': 702, 'AXN': 205, 'CHUTTI TV': 709, 'NDTV INDIA': 456, 'TV9 KANNADA': 815, 'ZEE SANGAM': 474, 'KIRAN TV': 863, 'STAR JALSHA': 842, 'GEMINI COMEDY': 750, 'HBO DEFINET HD': 358, 'UTV ACTION': 311, 'DD SAHYADRI': 785, 'IBN LOKMAT': 794, 'MURASU TV': 719, 'DD CHANDANA': 810, 'TEN CRICKET': 413, 'KANAK TV': 981, 'NDTV PROFIT-PRIME': 520, 'DD GIRNAR': 897, 'TEN ACTION': 415, 'DD NE': 985, 'ZEE 24 TASS': 795, 'NEWS X': 519, 'MAA GOLD': 766, 'Z PUNJAB HR HP': 953, 'CHARDIKLA TIME TV': 962, 'PROTIDIN TIME': 995, 'SUN MUSIC': 707, 'ETV ANDHRAPRADESH': 754, 'ISLAMIC DEVOTIO': 178, 'CNBC-TV18 HD': 523, 'ZEE CAF\xc9': 207, 'TV9 GUJARATI': 892, 'INDIA TV': 460, 'SONY MAX 2': 324, 'STAR PREMIERE HD': 213, 'SONY': 111, 'RANG TV': 991, 'STAR PRAVAH': 792, 'TIME NOW': 507, 'DISCOVERY  TAMIL': 727, 'ZEE KALINGA': 979, 'PEACE OF WIN': 192, 'BIINDASS PLAY': 661, 'ZEE NEWS': 459, 'POLIMER TV': 722, ' NEWS NATION': 472, 'ZEE BUSINESS': 490, 'ETV  up': 163, 'ZEE Q': 627, 'SUN TV HD': 703, 'DISCOVERY HD': 558, 'ROMEDY NOW': 357, 'STAR WORLD HD': 202, 'PRAG': 996, 'CARTOON NETWORK': 613, 'HBO HITS HD': 360, 'ZINDAGI': 137, 'IBN 7': 462, 'INDIAVISION': 877, 'DD KASHIR': 999, 'ABP NEWS': 454, 'MBC TV': 980, 'STAR GOLD HD': 302, 'MH ONE': 951, 'STAR SPORTS 4': 409, 'BABY TV': 621, 'DESNEY JUNIOR': 625, '9XM': 576, 'STAR SPORTS 1': 403, 'STAR SPORTS 2': 405, 'STAR SPORTS 3': 407, 'FILMY': 305, 'CNBC-TV18': 522, 'ZEE TALKIES': 796, 'DANGAL': 169, 'UDAYA MUSIC': 816, 'SONY KIX': 421, 'SUN LIFE': 730, 'ET NOW': 325, 'FOCUS NEWS': 473, 'AASTHA': 184, 'SRI SANKARA TV': 832, 'ETV bihar': 164, 'DISCOVERY': 557, 'Z RAJASHAN NEWS': 168, 'COLORS BANGLA': 837, 'ZEE STUDIO': 347, 'MATHRUBHUMI NEWS': 881, 'STAR MOVIES': 341, 'STAR MOVIES SEL HD': 351, 'ASIANET NEWS': 866, 'MH ONE SHRADDHA': 189, 'SUVARNA': 818, 'GEEMINI TV': 748, 'T  NEWS': 763, 'SURYA TV': 861, 'M TUNES': 665, '9X TASHAN': 960, 'MAZHAVIL MANOR': 871, 'ACTVE SMART GAMES': 601, 'KARAOKE': 651, 'UDAYA COMEDY': 824, 'AXN HD': 206, 'ADITHYE': 716, 'INDIA NEWS': 470, 'PARAS TV': 188, 'M TUNES HD': 666, 'RISHTEY': 129, 'MTV': 655, 'DD BANGLA': 835, 'ZEE TAMIZH': 725, 'PUTHIYA THALAIMURAI': 717, 'SADHANA TV': 191, 'KOLKATA TV': 850, 'SONY AATH': 845, 'Z ETC BOLLYWOOD': 669, 'WE TV': 874, 'ZEE CLASSIC': 313, 'DD SPORTS': 401, 'KASTHURI': 822, 'ASIANET': 864, 'AAKASH AATH': 841, 'ASIANET PLUS': 867, 'JEEVAN TV': 880, 'NATIONL GEOG HD': 552, 'MAA MOVIES': 760, 'MN+HD': 354, 'SVBC': 769, 'AL JAZEERA': 533, 'HISTORY TV 18': 563, 'TEN HD': 412, 'MGM': 361, 'ZEE CINEMA': 307, 'ABP MAJHA': 791, 'FOX LIFE HD': 554, 'CHENAL V': 109, 'NEWS 24': 461, 'OTV': 976, 'CNN INTL': 530, 'DISCOVERY KIDS': 617, 'MAA MUSIC': 761, 'IBC 24': 167, 'INDIA NEWS HARY': 476, 'DISCOVERY TURDO': 254, 'ZEE TV': 117, 'DD NEWS': 453, 'ANIMAL PLANET': 559, 'UDAYA TV': 811, 'DISHA TV': 186, 'JAIHAIND TV': 878, 'FX': 203, 'COLORS MARATHI': 786, 'ZEE ANMOL': 127, 'FOX LIFE': 553, 'COLORS': 119, 'BINDASS': 121, 'MAHUAA TV': 165, 'STAR UTSAV': 125, 'SUVARNA PLUS': 826, 'JALSHA MOVIES': 848, 'GEMINI TV HD': 749, 'RAJYA SABHA TV': 489, 'SANDESH NEWS': 895, 'SHUBHAVVAARTA TV': 771, 'ZEE CINEMA HD': 308, 'SHOWCASE': 281, 'VIJAY': 710, 'HOME SHOP 18': 151, 'PIX HD': 344, 'ZOOM': 659, 'ABN ANDHRaJYOTHY': 762, 'COMEDY CENTRAL': 212, 'DD ODIA': 971, 'COLORS GUJARATI': 890, 'ANGEL TV': 741, 'TV': 115, 'TOPPER': 590, 'FOOD FOOD': 581, '9X JHAKAAS': 798, 'RUPSSHI BANGLA': 852, 'UDAYA NEWS': 817, 'STAR MOVIES HD': 342, 'E24': 660, 'LIFE  OK HD': 108, 'TV9': 758, 'DD PODHIGAI': 701, 'TV5': 757, 'NDTV 24/7': 503, 'KALAIGNAR TV': 713, 'JAYA MAX': 720, 'NEWS LIVE': 988, 'SUN NEWS': 706, 'TLC': 250, 'PTC PUNJABI': 955, 'SONY PIX': 343, 'STAR SPORTS HD 4': 410, 'KAIRALITV': 873, 'ETV TELUGU': 752, 'ETV NEWS BANGLA': 851, 'STAR PLUS': 105, 'NICK JR.': 623, 'ETVrajashan': 162, 'ISAI ARUVI': 715, 'SONY PAL': 131, 'POGO': 615, 'NTV NEWS': 759, 'FOCUS NE': 993, 'MTV INDIES': 667, 'CHANNEL WIN': 179, 'MAKKAL TV': 724, 'ASEERVATHAN TV': 742, 'J MOVIE': 729, 'NEPAL 1': 990, 'RAJ TV': 714, 'PUBLIC TV': 825, 'SANGEET BANGLA': 846, 'VENDHAR TV': 731, 'E TV MP': 166, 'HUNGAMA': 605, 'LOK SABHA TV': 488, 'BLOOMBERG TV': 524, 'KOCHU TV': 875, 'ASIANET MOVIES': 868, 'CNBC BAJAR': 896, 'EPIC': 133, 'ETV URDU': 176, 'DY 365': 986, 'DISCOVERY SCIENCE': 561, 'JAI MAHARASHTRA': 799, 'REPORTER TV': 879, 'V6 TELUGU': 767, 'NAT GEO WILD': 555, 'LIFE OK': 107, 'PICHTURES': 317, 'SURYA MUSIC': 882, 'B4U MUSIC': 668, 'ADHYATAM TV': 190, 'DISNEY XD': 607, 'DD KISAN': 565, 'SONY SIX': 419, 'DD URDU': 175, 'UTV MOVIES': 309, 'BBC WORLD': 531, 'SHOP CJ': 150, 'COLORS KANNADA': 814, 'ZEE KANNADA': 820, 'DDBARATI': 161, 'SAKSHI TV': 746, 'SIRIPPOLI TV': 721, 'DD MALAYALAM': 870, 'ACTVE MUSIC': 650, 'ZEE ACTION': 319, 'TEN SPORTS': 411, 'THANTHI TV': 723, '24 GHANTA': 844, 'NDTV GOOD TINES': 252, 'BHAKTI TV': 770, 'ZEE BANGLA': 839, 'PTC  CHAKDE': 957, 'ZEE MARATHI': 788, 'SAHARA ONE': 139, 'SARTHAK TV': 977, 'ZEE TELUGU': 747, 'DISNEY CHANNEL': 609, 'ZEE STUDIO  HD': 348, 'STAR MOVIES ACTION': 355, 'GSTV': 894, 'DD NATIONAL': 104, 'MOVIES OK': 315, 'SONY MIX': 663, 'SONY HD': 112, 'COLORS ORIYA': 972, 'ZEE SALAAM': 177, 'GEMINI MOVIES': 745, 'KTV': 704, 'ABPANANDA': 836, 'PICHTURES HD': 318, 'JAYA PLUS': 726, 'UDAYA MOVIES': 813, 'TOLLYWOOD': 765, 'GOD TV': 888, 'AAJ TAK': 457, 'TARANG TV': 973, 'AMRITA TV': 869, 'ID': 135, 'SUVARNA NEWS 24': 823, 'MI MARATHI': 790, 'STAR PLUS HD': 106, 'SONY SAB': 113, 'Active Javed Akhtar': 102, 'STAR SPORTS HD 2': 406, 'STAR SPORTS HD 1': 404, 'SAAM TV': 797, 'PTC NEWS': 954, 'VH1': 675, 'TV HD': 116, 'SONIC NICKELODEON': 619, 'RAMDHENU TV': 994, 'NICK': 611, 'BIG MAGIC': 138, 'STUDIO ONE': 764, 'INDIA TODAY': 509, 'MANORAMA NEWS': 876, 'NAT GEO': 551, 'GEMINI MUSIC': 751, 'MOVIES NOW': 353, 'SONY MAX': 303, 'CNBC AWAAZ': 492, 'STAR SPORTS HD 3': 408, 'SANSKAR': 185, 'PRARTHANA TV': 978}

showChoices = []

channelsDictSky = {'test':100}
channelsDictSkyRev = {}
showTimeDict = {}
showTimeDictRev = {}
#channelsDict = {'Star Sports':401, 'Sony Max':303, 'Star Gold':302, 'Star Movies':342, 'Star Movies Action':355, 'Al Jazeera':533, 'Z ETC Bollywood':669, 'Discovery Science':561, 'Star Plus HD':105, 'Star Plus': 106, 'DD National':104}
channelsDictRev = {v: k for k, v in channelsDict.items()}
timeList = []

nowTime = datetime.datetime.now()
nowTime = nowTime.replace(hour = 18, minute = 0)
rightNow = datetime.datetime.now()
cNum = 107

playingNow = {}

def whatIsPlayingNow():
    #print('whatIsPlayingNow\n')
    for filename in glob.iglob('C:/Users/hoominchu/Desktop/pi/JSON/today/*.json'):
        try:
            with open(filename) as data_file:    
                data = json.load(data_file)
                cid = (data["cid"])
                cid = int(cid)
                num = (len(data["eventList"]))

                for i in range(0,num):

                    showTitle = (data["eventList"][i]["et"])
                    showTitleLower = showTitle.lower()
                    showTime = (data["eventList"][i]["st"])
                    showDuration = (data["eventList"][i]["ed"])

                    if ('movieX' in showTitleLower or 'newsX' in showTitleLower):
                        continue
                    else:
                        hourShowTime = showTime[0:2]
                        minuteShowTime = showTime[3:5]
                        showTimeX = timeObject.replace(hour = int(hourShowTime),minute = int(minuteShowTime), second = 0)
                        rightNow = datetime.datetime.now()
                        rightNow = rightNow.replace(second = 0)
                        duration = (timedelta(minutes=int(showDuration)))
                        timeDiff = rightNow-showTimeX
                        if ((timeDiff < duration) and timeDiff.days >= 0):
                            playingNow[showTitle] = cid
                            showChoices.append(showTitle)
                            #print(showTitle)
                        else:
                            continue
        except:
            pass

def playBeep():
    #print('playBeep\n')
    audiofilename = r'C:\Users\hoominchu\Desktop\pi\beep.mp3'
    clip = mp3play.load(audiofilename)

    clip.play()
    time.sleep(1)
    clip.stop()

for filename in glob.iglob('C:/Users/hoominchu/Desktop/pi/JSON/today/*.json'):
    #print(filename)
    try:
        with open(filename) as data_file: 
            j = json.load(data_file)
            timeObject = datetime.datetime.now()

            num = (len(j["eventList"]))

            cid = j["cid"]
            cid = int(cid)

            for i in range(0,num):

                showTitle = (j["eventList"][i]["et"])
                showTime = (j["eventList"][i]["st"])
                
                channelsDictSky[showTitle] = cid
                channelsDictSkyRev[cid] = showTitle
                showTimeDict[showTime] = showTitle
                showTimeDictRev[showTitle] = showTime

    except:
        pass

#####################################################################################

arduino = serial.Serial("COM4",9600)

allCommands = []

mydevices = ['tv','light','fan','settopbox']

greetWords = ['hey','hi','hello']

keyWords = ['theatermode', 'whatis', 'shuffle','mute','unmute','connect','goto','turnon','turnoff','watch','increasevolumebit','decreasevolumebit','increasevolumeby','decreasevolumeby','play','pause','stop','forward','favorite','change','howdy','goodmorning','afternoon','evening','morning','nextchannel','nextchannelchannel','prevchannel','next','back','entertainment', 'mute' , 'music' , 'news' ,'sports' , 'movie' , 'shuffle' , 'answertolife' , 'joke' , 'anotherjoke', 'watch']

tvKeyWords = ['theatermode', 'whatis','shuffle','mute','unmute','connect','goto','watch','increasevolumebit','decreasevolumebit','increasevolumeby','decreasevolumeby','play','pause','stop','forward','favorite','change','howdy','goodmorning','afternoon','evening','morning','nextchannel','nextchannelchannel','prevchannel','next','back','entertainment', 'mute' , 'music' , 'news' ,'sports' , 'movie' , 'shuffle' , 'answertolife' , 'joke' , 'anotherjoke', 'watch']

endWords = ['bye']

negativeWords = ['dont']

guide = {'wimbledon':401, 'tennis':402,'hindimovie':303, 'movie':302, 'englishmovie':342, 'actionmovie':'starmoviesaction', 'news':120, 'businessnews':'ET Now','internationalnews':'Al Jazeera', 'music':'MTV', 'bollywoodmusic': 'Z ETC Bollywood', 'indiemusic':'MTV indies', 'science':'Discovery Science','cartoon':'hungama'}
#channelsDict = {'channelName':'number','Starsports 1':401, 'Starsports 2':406,  'Sony Max':303, 'Star Gold':302, 'movie':302, 'Star Movies':342, 'Star Movies Action':355, 'indiatv':460, 'ET Now':525, 'Al Jazeera':533, 'mtv':655, 'Z ETC Bollywood':669, 'MTV indies':667, 'Discovery Science':561}

#channelsList = ['starsports','espn','smax','stargold','starmovies','moviesnow']

def text2int(textnum, numwords={}):
    #print('text2int\n')
    if not numwords:
        units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):  numwords[word] = (1, idx)
        for idx, word in enumerate(tens):       numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

    ordinal_words = {'first':1, 'second':2, 'third':3, 'fifth':5, 'eighth':8, 'ninth':9, 'twelfth':12}
    ordinal_endings = [('ieth', 'y'), ('th', '')]

    textnum = textnum.replace('-', ' ')

    current = result = 0
    for word in textnum.split():
        if word in ordinal_words:
            scale, increment = (1, ordinal_words[word])
        else:
            for ending, replacement in ordinal_endings:
                if word.endswith(ending):
                    word = "%s%s" % (word[:-len(ending)], replacement)

            if word not in numwords:
                #raise Exception("Illegal word: " + word)
                continue

            scale, increment = numwords[word]

        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

def greetcheck(command):
    #print('greetcheck\n')
    global userName
    for word in wordsList:
        for greetWord in greetWords:
            if (word == greetWord):
                print((random.choice(greetWords)).capitalize())
                print('Good to see you!')
                print('Here are the things you can do')
                engine.say("Hi, Good to see you, Here are a few things you can do" )
                print('You can turn on/off the TV, Increase/Decrease its volume, Play/Pause, ask your TV to put on a particular genre of channels, And do a lot more!')
                print('You can say things like "switch on TV" or "increase volume"')
                engine.say("You can turn on/off the TV, Increase/Decrease its volume, Play/Pause, ask your TV to put on a particular genre of channels, And do a lot more")
                engine.runAndWait()
                return 1
                        
    for word in wordsList:
        for keyWord in keyWords:
            if (word == keyWord):
                print ('Please wait...\n')
                action(word,command)
                return 2   
    print('I can\'t do that right now. But I will learn soon!\n')

def shuffle():

    movieslist=[303, 302, 342, 355];    

    hdlist=[1,2,3,4,5,6,7];

    specialslist=[];

    sportslist=[401, 406];

    entertainmentlist=[];

    newslist=[];

    knowledgekidslist=[];

    musicaudiolist=[655, 669, 667];

    regionallist=[];

    favouraitelist=[];

    allchannelslist=[655, 669, 667,401, 406,303, 302, 342, 355];

    global m
    
    x = checkNextWord('shuffle', command.split())
    if (x=='null'):
        random.shuffle(allchannelslist)
        for i in allchannelslist:
            print i
            gotoNumber(i)
            s=stop()
            if (s=='stop'):
                print ('stop')
                break
        time.sleep(1)                    

    elif(x=='movies'):
        random.shuffle(movieslist)
        for i in movieslist:
            print i
            gotoNumber(i);
            s=stop()
            if (s=='stop'):
                print ('stop')
                break
            time.sleep(1)
            

    elif(x=='sports'):
        random.shuffle(sportslist)
        for i in sportslist:
            print i
            gotoNumber(i);
            s=stop()
            if (s=='stop'):
                print ('stop')
                break
            time.sleep(1)
        
    elif(x=='hd'):
        random.shuffle(hdlist)
        for i in hdlist:
            print i
            gotoNumber(i);
            s=stop()
            if (s=='stop'):
                print ('stop')
                break
            time.sleep(1)
            

    elif(x=='entertainment'):
        random.shuffle(entertainmentlist)
        for i in entertainmentlist:
            print i
            gotoNumber(i);
            s=stop()
            if (s=='stop'):
                print ('stop')
                break
            time.sleep(1)    
    elif(x=='news'):
        random.shuffle(newslist)
        for i in newslist:
            print i
            gotoNumber(i);
            s=stop()
            if (s=='stop'):
                print ('stop')
                break
            time.sleep(1)       
    elif(x=='knowledge and kids'):
        random.shuffle(knowledgekidslist)
        for i in knowledgekidslist:
            print i
            gotoNumber(i)
            s=stop()
            if (s=='stop'):
                print ('stop')
                break
            time.sleep(1)
    elif(x=='music'):
        random.shuffle(musicaudiolist)
        for i in musicaudiolist:
            print (i)
            gotoNumber(i)
            s=stop()
            if (s=='stop'):
                print ('stop')
                break
            time.sleep(1)               
    elif(x=='regional'):
        random.shuffle(regionallist)
        for i in regionallist:
            print i
            gotoNumber(i)
            s=stop()
            if (s=='stop'):
                print ('stop')
                break
            time.sleep(1)       
    elif(x=='favorite'):
        random.shuffle(favouraitelist)
        for i in favouraitelist:
            print i
            gotoNumber(i);
            s=stop()
            if (s=='stop'):
                print ('stop')
                break
            time.sleep(1)       

def stop ():
    timeout = 5
    s=raw_input('enter')
    #rlist, _, _ = select([sys.stdin], [], [], timeout)
    if s=='stop':
            #m = sys.stdin.readline()
            print s
            return 'stop'
    else:
            print 'No input. Moving on..'
        
def gotoNumber(channelNumber):
    #print('gotoNumber\n')
    global channelsDictRev
    print(channelsDictRev[channelNumber])
    channelNameTemp = channelsDictRev[channelNumber]
    channelNameTemp = channelNameTemp.lower()
    engine.say("Putting on"+channelNameTemp)
    engine.say(channelsDictRev[channelNumber],"done")
    engine.runAndWait()
    channelNumberString = str(channelNumber)
    for digit in channelNumberString:
        #print(digit)
        arduino.write(('DIG_'+digit).encode())
        time.sleep(2.0)
    engine.say("Done")
    engine.runAndWait()
    
def checkNextWord(keyWord, listName):
    #print('checkNextWord\n')
    index = listName.index(keyWord)
    #indexNext = index + 1

    if len(listName) > index+1:
        y = listName[index+1]
        #genre = doIt(y)
        return y
    else:
        return 'null'

def commandNotClear(errorMessage):
    #print('commandNotClear\n')
    response = raw_input(errorMessage)
    #response = getVoiceCommand(errorMessage)
    print(response)
    return response

def isDeviceClear():
    #print('isDeviceClear\n')
    global mydevices, commandOriginal, tvKeyWords, theDevice
    #print(mydevices)                                                    #commentout
    commandWords = command.split()+commandOriginal.split()
    #print(commandWords)                                                 #commentout
    for i in commandWords:
        for h in tvKeyWords:
            if (i == h):
                return 'tv'
                break
               
    for word in mydevices:
        for k in commandWords:
            if (word == k):
                theDevice = word
                return word
                break
    for b in commandWords:
        for c in keyWords:
            if (b==c):
                #whichDevice = input('Please tell me which device (type)\n')
                engine.say("Please tell me which device")
                engine.runAndWait()
                whichDevice = getVoiceCommand('Please tell me which device\n')
                
                try:
                    whichDevice = whichDevice.lower()
                except:
                    pass
            
                whichDevice = whichDevice.replace('tata sky','settopbox')
                whichDevice = whichDevice.replace('tatasky','settopbox')
                whichDevice = whichDevice.replace('set top box','settopbox')
                
                whichDeviceWords = whichDevice.split()
                for x in whichDeviceWords:
                    for y in mydevices:
                        if (x == y):
                            print (x)
                            return x
                print (whichDevice)
                break

def doIt():
    #print('doIt\n')
    global keyWords, greetWords, wordsList, commandWords, command, theDevice, mydevices, commandOriginal
    engine.say("What can I do for you?")
    engine.runAndWait()
    #commandOriginal = getVoiceCommand('I am listening')

    commandOriginal = raw_input('Tell me\n')

    try:
        #commandOriginal = commandOriginal.lower()
        command = commandOriginal.lower()

        command = command.replace(' the ',' ')
        command = command.replace(' a ',' ')
        command = command.replace(' an ',' ')
        command = command.replace(' some ',' ')
        command = command.replace(' any ',' ')
        command = command.replace(' with ',' ')

        #Replacements

        command = command.replace('go to','goto')
        command = command.replace('put on','goto')
        command = command.replace('quote on','goto')
        command = command.replace('play','goto')
        command = command.replace('show','goto')
        command = command.replace('catch up','goto')
        command = command.replace('watch','goto')

        command = command.replace('switch on','turnon')
        command = command.replace('turn on','turnon')
        command = command.replace('start tv','turnon')
        command = command.replace('tv on','turnon')

        command = command.replace('switch off','turnoff')
        command = command.replace('turn off','turnoff')

        command = command.replace('volume up','increasevolumebit')
        command = command.replace('volume down','decreasevolumebit')

        command = command.replace('raise','increasevolumebit')
        command = command.replace('lower','decreasevolumebit')

        command = command.replace('increase volume bit','increasevolumebit')
        command = command.replace('decrease volume bit','increasevolumebit')

        command = command.replace('increase volume little','increasevolumebit')
        command = command.replace('decrease volume little','decreasevolumebit')

        command = command.replace('increase volume by','increasevolumeby')
        command = command.replace('decrease volume by','decreasevolumeby')

        command = command.replace('next channel','nextchannel')
        command = command.replace('previous channel','prevchannel')

        command = command.replace('next program','nextchannel')
        command = command.replace('previous program','prevchannel')

        command = command.replace('channel up','nextchannel')
        command = command.replace('channel down','prevchannel')

        command = command.replace('next','nextchannel')
        command = command.replace('back','prevchannel')

        command = command.replace('increase volume','increasevolumebit')
        command = command.replace('decrease volume','decreasevolumebit')

        command = command.replace('hindi movie','hindimovie')
        command = command.replace('action movie','actionmovie')

        command = command.replace('international news','internationalnews')
        command = command.replace('business news','businessnews')
        command = command.replace('bollywood music','bollywoodmusic')
        command = command.replace('indie music','indiemusic')

        command = command.replace('what is', 'whatis')
        command = command.replace('what\'s', 'whatis') 
 
    ##    command = command.replace('movie' , 'movie')
        command = command.replace('nude','mute') 
    #wisecracks
        command = command.replace('answer to life', 'answertolife')
        command = command.replace('another joke' , 'anotherjoke')

        ##repeat commands
        command = command.replace('show me something' , 'turnon')
        command = command.replace('volume up','increasevolumebit')
        command = command.replace('decrease volume bit','decreasevolumebit')
        command = command.replace('volume high','increasevolumebit')
        command = command.replace('volume low' , 'decreasevolumebit')
        command = command.replace('change to' , 'goto')
        command = command.replace('shut up' , 'mute')
        command = command.replace('play song' , 'music')
        command = command.replace('change' , 'goto')
        command = command.replace('picture', 'movie')
        #command = command.replace('next', 'nextchannel')
        command = command.replace('up', 'increasevolumebit')
        command = command.replace('down' , 'decreasevolumebit')

        command = command.replace('good morning','goodmorning')
        ## repeat for similar commands
        
        ##Hindi

        command = command.replace('chalu karo' , 'turnon')
        command = command.replace('chalo karo' , 'turnon')
        #command = command.replace('khul ja sim sim' , 'turnon')
        command = command.replace('shuru' , 'turnon')
        command = command.replace('jalao' , 'turnon')
        command = command.replace('band karo' , 'turnoff')                      #checkthis
        command = command.replace('volume badhao' , 'increasevolumebit')
        command = command.replace('volume do' , 'increasevolumebit')
        command = command.replace('volume kam' , 'decreasevolumebit')
        command = command.replace('kuch aur' , 'nextchannelchannel')
        command = command.replace('agla channel' , 'nextchannelchannel')
        command = command.replace('gaana' , 'music')
        command = command.replace('gana' , 'music')
       
        """ 
        commandOriginal = commandOriginal.replace('gaana','music')
        commandOriginal = commandOriginal.replace('gana','music')
        commandOriginal = commandOriginal.replace('agla channel','nextchannel')
        commandOriginal = commandOriginal.replace('kuch aur','nextchannel')

        """
        
        command = command.replace('lagado','goto')
        command = command.replace('lagao','goto')
        command = command.replace('dekh',' goto ')

        command = command.replace('tata sky','settopbox')
        command = command.replace('tatasky','settopbox')
        command = command.replace('set top box','settopbox')

        #print (wordsList)
        theDevice = isDeviceClear()
        #command = command.replace(theDevice,'')
        print(theDevice)

        for word in mydevices:
            command = command.replace(' ' + word,'')

        
        command = command.replace('switch on','turnon')
        command = command.replace('turn on','turnon')
        command = command.replace('start tv','turnon')

        command = command.replace('switch off','turnoff')
        command = command.replace('turn off','turnoff')
        command = command.replace ('let there be', 'turnon')

        ####################################

        #####################

        command = command.replace('theater mode', 'theatermode')

        commandWords = command.split()

        wordsList = commandWords
        
        wordsList.append('endOfCommand')

        suggestions = process.extract(command, showChoices, limit = 8)
        #print suggestions

        #print(command)
        #print(commandOriginal)

        state = greetcheck(command)

    except:
        pass
        #print('I couldn\'t get that, Can you please say that again?')
        #engine.say("I couldn't get that, Can you please say that again?")
        #engine.runAndWait()

def checkWordInDict(dictionaryName):
    #print('checkWordInDict\n')
    global commandOriginal, showChoices,command
    commandTemp = command.split('goto',1)
    nearestChoice = process.extractOne(commandTemp,showChoices)
    if (nearestChoice[1]>87):
        #print(nearestChoice[1])
        return nearestChoice[0], nearestChoice[1]
    else:
        return 'none'

def oldDictFunc(dictionaryName):
    #print('oldDictFunc\n')
    global commandOriginal
    #print(dictionaryName)
    for key in dictionaryName.keys():
        keylower = key.lower()
        #print(key)
        if keylower in commandOriginal.lower():
            return key
        else:
            continue
  
def action(keyWord,command):
    global theDevice,commandWords, playingNow, channelsDict, channelsDictSky, guide
    #print(channelsDictSky)
    #print(command)
    #print(keyWord)

    #print('action\n')

    if (keyWord == 'increasevolumebit'):
            print('Increase the volume by 5')
            engine.say("increasing the volume")
            engine.runAndWait()
            for x in range(0,5):            
                arduino.write('VOL_UP'.encode())
                time.sleep(2.0)

    if (keyWord == 'decreasevolumebit'):
            print('Decrease the volume by 5')
            engine.say("decreasing the volume")
            engine.runAndWait()
            for i in range(0,5):
                arduino.write('VOL_DOWN'.encode())
                time.sleep(2.0)

    if (keyWord == 'whatis'):
            print('Getting the list ready...')
            whatIsPlayingNow()
            print('Here are the things playing right now')
            for key in playingNow.keys():
                try:
                    chnum = playingNow[key]
                    print (key + ' : ' + channelsDictRev[chnum])
                except:
                    pass

    if (theDevice == 'tv'):
        number = text2int (command, numwords={})
        if (keyWord == 'nextchannel'):
                print('OK')
                arduino.write('SKY_CH_UP'.encode())
        if (keyWord == 'prevchannel'):
                print('OK')

        if (keyWord == 'nextchannelchannel'):
                print('OK')
                arduino.write('SKY_CH_UP'.encode())
        if (keyWord == 'prevchannelchannel'):
                print('OK')
                arduino.write('SKY_CH_DOWN'.encode())

        if (keyWord == 'goto'):
            if (number == 0):
                flagX = 0
                if (flagX==0):
                #check if it is a channel name
                    try:
                        if (flagX == 0):
                            dest = oldDictFunc(channelsDict)
                            #print(channelsDict)
                            print(channelsDict[dest])
                            gotoNumber(channelsDict[dest])
                            flagX = 1
                            #print ('The channel name is : ' + dest) 
                            return
                    except:
                        try:
                            if (flagX == 0):
                                dest,conf = checkWordInDict(playingNow)
                                print(playingNow[dest])
                                print ('The program name is : ' + dest) 
                                print ('Confidence level : ' + str(conf)) 
                                gotoNumber(playingNow[dest])
                                flagX = 1
                                return
                                
                        except:
                            pass
                
                else:
                    if flagX == 0:
                        response = commandNotClear('Please say a number or the name of a channel\n')
                        number = text2int (response, numwords={})
                        if (number == 0):
                            print('Go to channel ' + response)
                        else:
                            print('Go to channel ' + str(number))

            else:
                print ('Going to ' + str(number))
                gotoNumber(number)
            #Add action for commands with channel names. Right now this works only for numbers.

        if (keyWord == 'turnon'):
            print('Turning the tv on')
            engine.say("Turning the tv on")
            arduino.write('TV_ON'.encode())
            engine.runAndWait()

        if (keyWord == 'turnoff'):
            print('Turning the tv off')
            engine.say("Turning off")
            engine.runAndWait()
            arduino.write('TV_ON'.encode())

        if (keyWord == 'increasevolumebit'):
            print('Increase the volume by 5')
            engine.say("increasing the volume")
            engine.runAndWait()
            for x in range(0,5):            
                arduino.write('VOL_UP'.encode())
                time.sleep(2.0)

        if (keyWord == 'decreasevolumebit'):
            print('Decrease the volume by 5')
            engine.say("decreasing the volume")
            engine.runAndWait()
            for i in range(0,5):
                arduino.write('VOL_DOWN'.encode())
                time.sleep(2.0)

        if (keyWord == 'increasevolumeby'):
            if (number == 0):
                response = commandNotClear('Please tell me how much')
                number = text2int (response, numwords={})
            print('Increase the volume by ' + str(number))
            for i in range(0,number):
                arduino.write('VOL_UP'.encode())
                print('+1')
                time.sleep(2.0)
                
        if (keyWord == 'decreasevolumeby'):
            if (number == 0):
                response = commandNotClear('Please tell me how much')
                number = text2int (response, numwords={})
            print('Decrease the volume by ' + str(number))
            for i in range(0,number):
                arduino.write('VOL_DOWN'.encode())
                time.sleep(2.0)

        if (keyWord == 'goodmorning'):
            print('Good morning ' + userName)

        # Add all the other possible greet commands like Good night, afternoon etc.

        if (keyWord == 'mute'):
            print('Mute')
            #engine.say("okay keeping my mouth shut")
            #engine.runAndWait()
            arduino.write('MUTE'.encode())

        if (keyWord == 'unmute'):
            print('Unmute')
            engine.say("unmute")
            engine.runAndWait()
            arduino.write('MUTE'.encode())

        if (keyWord == 'music'):
            print('Playing a Music Channel')
            engine.say("Music Channel For You")
            engine.runAndWait()
            temp = 655
            gotoNumber(temp)

        if (keyWord == 'news'):
            print('Showing you today\'s News')
            engine.say("Here are the headlines to keep you updated")
            engine.runAndWait()
            temp = 503
            gotoNumber(temp)

        if (keyWord == 'sports'):
            print('Sports channel for you')
            engine.say("Sports channel")
            engine.runAndWait()
            temp = 401
            gotoNumber(temp)
                

        if (keyWord == 'movie'):
            print('Grab some popcorn!')
            engine.say("Grab some popcorn")
            engine.runAndWait()
            gotoNumber(302)
                 
        if (keyWord == 'entertainment'):
            print('I love to entertain you!')
            engine.say("why don't you call your friends over? ")
            engine.runAndWait
            gotoNumber(105)
         
        if (keyWord == 'shuffle'):
            shuffle()
            print('Shuffle channels for you, Let me know when to stop.')
                
        if (keyWord == 'favorite'):
            print('Got it, added this channel to your favorites!')

        if (keyWord == 'answertolife'):
            print('Mr. Adams suggests that the answer to everything in life is 42')

        if (keyWord == 'joke'):
            print('I met my soulmate. She didn\'t.')
            engine.say("I met my soulmate. She didn't")
            engine.runAndWait()

        if (keyWord == 'anotherjoke'):
            print('I saw the cricket ball getting bigger. Then it hit me')
            engine.say("I saw the cricket ball getting bigger. Then it hit me" )
            engine.runAndWait()
                
        if (keyWord == 'theatermode'):
            print('Theatre mode on')
            arduino.write('LIGHT_ON'.encode())
            movieNumber = 342
            gotoNumber(movieNumber)

    if (theDevice == 'light'):
        if (keyWord == 'turnon'):
            print('Turning the light on')
            engine.say("Lights on for you")
            engine.runAndWait()
            arduino.write('LIGHT_ON'.encode())

        if (keyWord == 'turnoff'):
            print('Turning the light off')
            engine.say("Turn the lights off")
            engine.runAndWait()
            arduino.write('LIGHT_ON'.encode())
            
    if (theDevice == 'fan'):
        if (keyWord == 'turnon'):
            print('Turning fan on')
            arduino.write('FAN_ON'.encode())

        if (keyWord == 'turnoff'):
            print('Turning the light off')
        
            arduino.write('FAN_ON'.encode())

    if (theDevice == 'settopbox'):
        if (keyWord == 'turnon'):
            print('Turning the set top box on')
            arduino.write('SKY_ON'.encode())

        if (keyWord == 'turnoff'):
            print('Turning the set top box off')
            arduino.write('SKY_ON'.encode())
    
def getVoiceCommand(whatToPrint):
    #print('getvoicecommand\n')
    # obtain audio from the microphone
    r = sr.Recognizer()
    r.energy_threshold = 6000
    with sr.Microphone() as source:
        print(whatToPrint)
        playBeep()
        audio = r.listen(source)
        #audio = r.listen_in_background(source)
        

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print(r.recognize_google(audio))
        return r.recognize_google(audio)

    except sr.UnknownValueError:
        #print("Google Speech Recognition could not understand audio")
        getVoiceCommand(whatToPrint)

flag = 0

wordsList=[]

#theDevice = 'dontknow'    

currentChannel = 10

myName = 'pi'

#userName = input('What is your name?\n')
#userName = getVoiceCommand('What is your name?')

userName = 'Minchu'

whatIsPlayingNow()

while (flag == 0):
    doIt()
    #print(playingNow)
    
    #print (command)
    
f.close()
    
