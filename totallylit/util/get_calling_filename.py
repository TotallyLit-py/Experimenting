from .get_calling_stackframe import get_calling_stackframe


def get_calling_filename(starting_frame_index: int, max_search_frames: int = 100):
    return get_calling_stackframe(starting_frame_index, max_search_frames).filename
