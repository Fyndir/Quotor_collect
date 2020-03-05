import moviepy.editor as mp
import pysrt



def Convert_SubRipTime_Seconde(sub):
    return sub.hours*60*60+sub.minutes*60+sub.seconds

if __name__ == "__main__":
    marge_erreur = 1
    i = 1

    subs = pysrt.open('./Data/PulpFiction.srt')
   
    for sub in subs :
        try:
            clip = mp.VideoFileClip("./Data/Pulp.Fiction.avi").subclip(Convert_SubRipTime_Seconde(sub.start)-marge_erreur,Convert_SubRipTime_Seconde(sub.end)+marge_erreur)
            clip.audio.write_audiofile('./Output/'+str(i)+"_"+str(sub.text)+".mp3")            
        except :
            print("Error :"+str(i)+"_"+str(sub.text))
        i=i+1