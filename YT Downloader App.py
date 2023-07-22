from tkinter import *
import tkinter.messagebox as mbox
from pytube import YouTube

#Trial Link: 
#https://youtu.be/N4Ilw97aKn0

root = Tk()

root.configure(bg='white')
root.geometry('800x1550')
root.title('YT Downloader ~ By Sanskar Shimpi')
input = Entry(root, width=26)
input.place(x=250, y=109)

Label(text='Enter Link:', bg='white', fg='black', font=('Times New Roman', 10, 'italic')).place(x=20, y=104)


download_options = [
	('720p', '720p'),
    ('360p', '360p'),
    ('144p', '144p'),
    ('Audio Only', 'Audio')]

video_quality = StringVar()

y_axis = 274

for option, quality in download_options:
		video_radio = Radiobutton(text=option, bg='white', relief=SUNKEN, borderwidth=3, padx=20, pady=20, value=quality, variable=video_quality)
		video_radio.place(x=280, y=y_axis)
			

		y_axis += 100

def download():
	'''Logic For Downloading Videos/Audios'''
	try:
		
		vOption = video_quality.get()
		
		link_text = input.get()
		path = '/storage/emulated/10'
		video_data = YouTube(link_text)
		
		#TODO: Print Title of video in Console or in GUI
		
		if vOption == '720p':
			
			downloading_video = video_data.streams.filter(res='720p').first()
			downloading_video.download(path)
			
			mbox.showinfo('Download Complete', 'Video downloaded successfully!')
		
		elif vOption == '360p':
			
			downloading_video = video_data.streams.filter(res='360p').first()
			downloading_video.download(path)
			
			mbox.showinfo('Download Complete', 'Video downloaded successfully!')
		
		elif vOption == '144p':
			
			downloading_video = video_data.streams.filter(res='144p').first()
			downloading_video.download(path)
			
			mbox.showinfo('Download Complete', 'Video downloaded successfully!')
			
		elif vOption == 'Audio':
			
			downloading_video = video_data.streams.filter(only_audio=True).first()
			downloading_video.download(path, filename=video_data.title.split('.')[0]+'.mp3')	
			
			mbox.showinfo('Download Complete', 'Audio downloaded successfully!')
			
		else:		
			pass
	
	except Exception as e:
		mbox.showerror('Error', f'Error Raised!\n{type(e).__name__}')

download_button = Button(text='Download Now', bg='white', relief=SUNKEN, padx=15, pady=15, borderwidth=5, command=download)

download_button.place(x=250, y=774)	

root.mainloop()