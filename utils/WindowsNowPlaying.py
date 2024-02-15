import winsdk.windows.media.control as media_control
import winsdk.windows.storage.streams as streams
import asyncio

async def get_current_playing_song():
    sessions = await media_control.GlobalSystemMediaTransportControlsSessionManager.request_async()

    current_session = sessions.get_current_session()
    if current_session:
        media_info = await current_session.try_get_media_properties_async()
        thumbnail_ref = media_info.thumbnail
        if thumbnail_ref:
            stream_with_content = await thumbnail_ref.open_read_async()
            size = stream_with_content.size
            if size:
                reader = streams.DataReader(stream_with_content)
                await reader.load_async(size)
                data = reader.read_buffer(size)
                # Save the image data to a file
                file_name = f"thumb.png".replace('/', '_').replace('\\', '_')
                with open(file_name, "wb") as file:
                    file.write(data)
            else:
                print("No album cover available.")
        else:
            print("No album cover available.")
    else:
        print("No song is currently playing.")

asyncio.run(get_current_playing_song())