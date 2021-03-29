.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,int)
    :digest: e875d49062262bc3c09a030eaac5a290

Updates the size policy of the widget at position *index* to have a stretch factor of *stretch*.

*stretch* is not the effective stretch factor; the effective stretch factor is calculated by taking the initial size of the widget and multiplying it with *stretch*.

This function is provided for convenience. It is equivalent to

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qsplitter.py
    :lines: 54-58

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSplitter.setSizes`, :sip:ref:`~PyQt6.QtWidgets.QSplitter.widget`.
