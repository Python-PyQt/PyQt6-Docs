.. sip:method-description::
    :status: todo
    :pysig: 93c65966a7252879a2fdbc87264c9da8
    :realsig: (int,int,int,int)
    :digest: 264d6c3756d73039e50854297b8e6a18

Sets the margins around the contents of the widget to have the sizes *left*, *top*, *right*, and *bottom*. The margins are used by the layout system, and may be used by subclasses to specify the area to draw in (e.g. excluding the frame).

Changing the margins will trigger a :sip:ref:`~PyQt6.QtWidgets.QWidget.resizeEvent`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.contentsRect`, :sip:ref:`~PyQt6.QtWidgets.QWidget.contentsMargins`.
