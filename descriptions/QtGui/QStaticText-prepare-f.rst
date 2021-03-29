.. sip:method-description::
    :status: todo
    :pysig: 477237377973065823b128404fd07510
    :realsig: (const QTransform&,const QFont&)
    :digest: 6dd64a290ee45529777f9e85df1f3e4b

Prepares the :sip:ref:`~PyQt6.QtGui.QStaticText` object for being painted with the given *matrix* and the given *font* to avoid overhead when the actual drawStaticText() call is made.

When drawStaticText() is called, the layout of the :sip:ref:`~PyQt6.QtGui.QStaticText` will be recalculated if any part of the :sip:ref:`~PyQt6.QtGui.QStaticText` object has changed since the last time it was drawn. It will also be recalculated if the painter's font is not the same as when the :sip:ref:`~PyQt6.QtGui.QStaticText` was last drawn, or, on any other paint engine than the OpenGL2 engine, if the painter's matrix has been altered since the static text was last drawn.

To avoid the overhead of creating the layout the first time you draw the :sip:ref:`~PyQt6.QtGui.QStaticText` after making changes, you can use the  function and pass in the *matrix* and *font* you expect to use when drawing the text.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.setFont`, :sip:ref:`~PyQt6.QtGui.QPainter.setWorldTransform`.
