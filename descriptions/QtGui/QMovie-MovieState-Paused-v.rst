.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: f572505594b697c9a116b0e250a4fcfe

The movie is paused, and :sip:ref:`~PyQt6.QtGui.QMovie` stops emitting :sip:ref:`~PyQt6.QtGui.QMovie.updated` or :sip:ref:`~PyQt6.QtGui.QMovie.resized`. This state is entered after calling pause() or :sip:ref:`~PyQt6.QtGui.QMovie.setPaused`\ (true). The current frame number it kept, and the movie will continue with the next frame when unpause() or :sip:ref:`~PyQt6.QtGui.QMovie.setPaused`\ (false) is called.
