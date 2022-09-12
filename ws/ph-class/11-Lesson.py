
def func01():
    import pytube
    from pytube.cli import on_progress as op

    url = 'https://www.youtube.com/watch?v=SiBw7os-_zI'

    video = pytube.YouTube(url, on_progress_callback=op)

    for stream in video.streams:
        print(stream)

def func02():
    import pytube
    from pytube.cli import on_progress as op

    url = 'https://www.youtube.com/watch?v=SiBw7os-_zI'

    video = pytube.YouTube(url, on_progress_callback=op)

    stream = video.streams.get_by_itag(18)

    stream.download(filename='youtubefile.mp4')
    print('done')


def func03():
    import pytube
    from pytube.cli import on_progress as op

    url_list = []
    input_flag = 1
    while input_flag == 1:
        try:
            inp = str(input('Enter a youtube url or press 0 to start downloads:'))
            if inp == '0':
                break
            url_list.append(inp)
        except:
            break
    counter = 0
    for url in url_list:
        counter += 1
        video = pytube.YouTube(url, on_progress_callback=op)

        stream = video.streams.get_by_itag(18)

        stream.download(filename=f'youtubefile{counter}.mp4')
        print('done')

#https://www.youtube.com/watch?v=E39a7kQfjSg
#https://www.youtube.com/watch?v=vJwcW2gCCE4
#https://www.youtube.com/watch?v=lTypMlVBFM4

def func04():
    import pytube
    from pytube.cli import on_progress as op

    playlist_url = 'https://www.youtube.com/watch?v=WcPNlnsNZyY&list=PLRzwgpycm-FiPfuP-bKOJTJRkQH-F8brg'

    play_list = pytube.Playlist(playlist_url)
    print(play_list)

    counter = 0

    for url in play_list:
        counter += 1
        video = pytube.YouTube(url, on_progress_callback=op)

        stream = video.streams.get_by_itag(18)

        stream.download(filename=f'youtubefile{counter}.mp4')
        print('done')


#---------------Main----------------
func04()