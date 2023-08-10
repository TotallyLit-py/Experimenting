import inspect


def get_calling_stackframe(
    starting_frame_index: int, max_search_frames: int = 100
) -> inspect.FrameInfo:
    stack = inspect.stack()
    for frame in range(starting_frame_index, starting_frame_index + max_search_frames):
        try:
            frame = stack[frame]
            if frame.filename and frame.filename.lower().endswith(".py"):
                return frame
        except IndexError:
            break
