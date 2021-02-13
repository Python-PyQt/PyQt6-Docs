.. sip:method-description::
    :status: todo
    :pysig: 508e645b907c0825f330e8aa2b764b5b
    :realsig: (const QString&,const QIcon&)
    :digest: d3a9e33cb7bd144626ac3244e775d6a7

This is an overloaded function.

Returns the :sip:ref:`~PyQt6.QtGui.QIcon` corresponding to *name* in the current icon theme. If no such icon is found in the current theme *fallback* is returned instead.

If you want to provide a guaranteed fallback for platforms that do not support theme icons, you can use the second argument:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qicon.py
    :lines: 103-103
