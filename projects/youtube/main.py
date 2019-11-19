from pytube import YouTube as YT


def show_progress_bar(stream, chunk, file_handle, bytes_remaining):
    print(bytes_remaining)


yt = YT('https://www.youtube.com/watch?v=v2xf9KOQVkM')
yt.register_on_progress_callback(func=show_progress_bar)
yt.streams.get_by_itag(140).download()
