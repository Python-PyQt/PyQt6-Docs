.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: be80c3a9a0a249ea8d663e79e19c3f66

Enables caching of the complete layout information if *enable* is true; otherwise disables layout caching. Usually :sip:ref:`~PyQt6.QtGui.QTextLayout` throws most of the layouting information away after a call to :sip:ref:`~PyQt6.QtGui.QTextLayout.endLayout` to reduce memory consumption. If you however want to draw the laid out text directly afterwards enabling caching might speed up drawing significantly.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextLayout.cacheEnabled`.
