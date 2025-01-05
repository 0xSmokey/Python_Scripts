# Youtube video and audio download
# by mr blue

from pytube import YouTube


class Ytdownload:

  def downloadhighres(yt):
    try:
      print("Channel:", yt.author)
      print("Title:", yt.title)

      # get_highest_resolution() returns highest res video ("720p")

      dwnlditm = yt.streams.get_highest_resolution()
      print("Downloading...")
      dwnlditm.download()
      print("Download complete!")
    except Exception as e:
      print("Error occurred:", str(e))

  def downloadlowres(yt):
    try:
        print("Channel:", yt.author)
        print("Title:", yt.title)

        # get_by_resolution() method should be given a specified parameter so used '360p' res for low resolution video

        lowresvideo = yt.streams.get_by_resolution('360p')  # or yt.streams.get_by_resolution('144p')
        if lowresvideo:
            print("Downloading...")
            try:
                lowresvideo.download()
                print("Download complete!")
            except Exception as e:
                print("Error occurred during download:", str(e))
        else:
            print("Low-resolution video not available.")
    except Exception as e:
        print("Error occurred:", str(e))


  # audio file method need to filter out
  def downloadaudio(yt):
    try:
      print("Channel:", yt.author)
      print("Title:", yt.title)

      # To filter audio need filter method from streams 'only_audio - gives audio, '
      audio_streams = yt.streams.filter(only_audio=True,
                                        file_extension='mp4',
                                        abr="128kbps")
      dwnlditm = audio_streams.first()
      print("Downloading...")
      # converting mp4 to mp3 with string interpolation
      try:
        dwnlditm.download(filename=f"{yt.title}.mp3")
      except:
        print("audio stream is not available")
      print("Download complete!")
    except Exception as e:
      print("Error occurred:", str(e))


if __name__ == "__main__":
  link = input("\nEnter link here: ")

  if link:
    # crearting youtube object
    yt = YouTube(link)

    options = input("""
    highres - h
    lowres  - l
    audio   - a

>> """)

    if options == "h":
      Ytdownload.downloadhighres(yt)
    elif options == "l":
      Ytdownload.downloadlowres(yt)
    elif options == "a":
      Ytdownload.downloadaudio(yt)

    else:
      print("Invalid option. Please choose 'h', 'l', or 'a'.")
  else:
    print("Invalid YouTube link. Please provide a valid link.")