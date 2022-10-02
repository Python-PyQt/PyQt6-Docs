.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 6bd55cd8993bf2e3397c7b2e97cc5b59

Returns the number of times the movie will loop before it finishes. If the movie will only play once (no looping), loopCount returns 0. If the movie loops forever, loopCount returns -1.

Note that, if the image data comes from a sequential device (e.g. a socket), :sip:ref:`~PyQt6.QtGui.QMovie` can only loop the movie if the :sip:ref:`~PyQt6.QtGui.QMovie.cacheMode` is set to :sip:ref:`~PyQt6.QtGui.QMovie.CacheMode.CacheAll`.
