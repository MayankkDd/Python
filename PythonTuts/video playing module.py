# import vlc
# import pafy
#
# youtube_video_url = "https://www.youtube.com/watch?v=YcTCIMKeiNQ"
#
# # creating a pafy object of the video
# video_pafy_object = pafy.new(youtube_video_url)
#
# # getting best stream
# stream_gotten = video_pafy_object.getbest()
#
# # creating vlc media player object
# media_player_object = vlc.MediaPlayer(stream_gotten.youtube_video_url)
#
# # starting playing video
# media_player_object.play()


# importing vlc module
import vlc

# # importing pafy module
# import pafy
#
# # url of the video
# url = "https://www.youtube.com/watch?v = vG2PNdI8axo"
#
# # creating pafy object of the video
# video = pafy.new(url)
#
# # getting best stream
# best = video.getbest()

# creating vlc media player object
media = vlc.MediaPlayer("Compiler design tutorial hindi for gate lectures important topics knowledge gate syllabus prepration.mp4")

# start playing video
media.play()