.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 348dfc17fc5e66a0d68befd7a726d90b

Stops the movie. :sip:ref:`~PyQt6.QtGui.QMovie` enters :sip:ref:`~PyQt6.QtGui.QMovie.MovieState.NotRunning` state, and stops emitting :sip:ref:`~PyQt6.QtGui.QMovie.updated` and :sip:ref:`~PyQt6.QtGui.QMovie.resized`. If :sip:ref:`~PyQt6.QtGui.QMovie.start` is called again, the movie will restart from the beginning.

If :sip:ref:`~PyQt6.QtGui.QMovie` is already in the :sip:ref:`~PyQt6.QtGui.QMovie.MovieState.NotRunning` state, this function does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QMovie.start`, :sip:ref:`~PyQt6.QtGui.QMovie.setPaused`.
