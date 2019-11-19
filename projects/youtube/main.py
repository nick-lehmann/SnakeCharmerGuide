from pytube import YouTube as yt


def show_progress_bar(stream, chunk, file_handle, bytes_remaining):
    print(bytes_remaining)


yt.register_on_progress_callback(show_progress_bar)

print(
    yt('https://www.youtube.com/watch?v=v2xf9KOQVkM')
    .streams.get_by_itag(140).download()
)
