from playsound import playsound
print("no. of available songs\n1.besharam rang\n2.beliver\n3.kesariya\n4.maan meri jaan\n5.who says\n6.apana bana lena")
order = input('enter the music which you want to play:')
if "besharam rang" in order:
    playsound('C:\\Users\\varsh\\Music\\besharam rang.mp3')
elif "beliver" in order:
     playsound('C:\\Users\\varsh\\Music\\beliver.mp3')
elif "kesariya" in order:
     playsound('C:\\Users\\varsh\\Music\\kesariya.mp3')
elif "maan meri jaan" in order:
     playsound('C:\\Users\\varsh\\Music\\maan meri jaan.mp3')
elif " who says" in order:
     playsound('C:\\Users\\varsh\\Music\\who says.mp3')
elif " apana bana lena" in order:
     playsound('C:\\Users\\varsh\\Music\\apana bana lena.mp3')
     