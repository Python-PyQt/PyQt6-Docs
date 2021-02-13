.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,int)
    :digest: 79b5e421ff27fc93e35ee5c8672248f2

Moves the left or top edge of the splitter handle at *index* as close as possible to position *pos*, which is the distance from the left or top edge of the widget.

For right-to-left languages such as Arabic and Hebrew, the layout of horizontal splitters is reversed. *pos* is then the distance from the right edge of the widget.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSplitter.splitterMoved`, :sip:ref:`~PyQt6.QtWidgets.QSplitter.closestLegalPosition`, :sip:ref:`~PyQt6.QtWidgets.QSplitter.getRange`.
