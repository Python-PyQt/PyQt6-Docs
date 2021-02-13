.. sip:signal-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,int)
    :digest: 8d1b5664f251e75ee8698236083179ff

This signal is emitted when the splitter handle at a particular *index* has been moved to position *pos*.

For right-to-left languages such as Arabic and Hebrew, the layout of horizontal splitters is reversed. *pos* is then the distance from the right edge of the widget.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSplitter.moveSplitter`.
