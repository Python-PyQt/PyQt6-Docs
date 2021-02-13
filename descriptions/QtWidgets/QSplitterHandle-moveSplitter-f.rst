.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: c1f3b9beabac45cc57fcead27a2f4500

Tells the splitter to move this handle to position *pos*, which is the distance from the left or top edge of the widget.

Note that *pos* is also measured from the left (or top) for right-to-left languages. This function will map *pos* to the appropriate position before calling :sip:ref:`~PyQt6.QtWidgets.QSplitter.moveSplitter`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSplitter.moveSplitter`, :sip:ref:`~PyQt6.QtWidgets.QSplitterHandle.closestLegalPosition`.
