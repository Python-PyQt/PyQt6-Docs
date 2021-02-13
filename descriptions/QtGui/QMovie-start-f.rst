.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 70ca2fa41d82305603b9e60442a76ffa

Starts the movie. :sip:ref:`~PyQt6.QtGui.QMovie` will enter :sip:ref:`~PyQt6.QtGui.QMovie.MovieState.Running` state, and start emitting :sip:ref:`~PyQt6.QtGui.QMovie.updated` and :sip:ref:`~PyQt6.QtGui.QMovie.resized` as the movie progresses.

If :sip:ref:`~PyQt6.QtGui.QMovie` is in the :sip:ref:`~PyQt6.QtGui.QMovie.MovieState.Paused` state, this function is equivalent to calling :sip:ref:`~PyQt6.QtGui.QMovie.setPaused`\ (false). If :sip:ref:`~PyQt6.QtGui.QMovie` is already in the :sip:ref:`~PyQt6.QtGui.QMovie.MovieState.Running` state, this function does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QMovie.stop`, :sip:ref:`~PyQt6.QtGui.QMovie.setPaused`.
