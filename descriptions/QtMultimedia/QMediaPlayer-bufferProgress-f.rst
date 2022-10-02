.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: 433524f5a69e5cd43cd211a32ff29219

Returns a number betwee 0 and 1 when buffering data.

0 means that there is no buffered data available, playback is usually stalled in this case. Playback will resume once the buffer reaches 1, meaning enough data has been buffered to be able to resume playback.

bufferProgress() will always return 1 for local files.
