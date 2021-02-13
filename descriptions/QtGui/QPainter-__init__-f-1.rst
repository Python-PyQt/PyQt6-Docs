.. sip:method-description::
    :status: todo
    :pysig: 5b29482105442ab8f18835c84bd0b907
    :realsig: (QPaintDevice*)
    :digest: c140a7d540c5312337ed84d404573719

Constructs a painter that begins painting the paint *device* immediately.

This constructor is convenient for short-lived painters, e.g. in a :sip:ref:`~PyQt6.QtWidgets.QWidget.paintEvent` and should be used only once. The constructor calls :sip:ref:`~PyQt6.QtGui.QPainter.begin` for you and the :sip:ref:`~PyQt6.QtGui.QPainter` destructor automatically calls :sip:ref:`~PyQt6.QtGui.QPainter.end`.

Here's an example using :sip:ref:`~PyQt6.QtGui.QPainter.begin` and :sip:ref:`~PyQt6.QtGui.QPainter.end`:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainter.py
    :lines: 85-91

The same example using this constructor:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainter.py
    :lines: 119-123

Since the constructor cannot provide feedback when the initialization of the painter failed you should rather use :sip:ref:`~PyQt6.QtGui.QPainter.begin` and :sip:ref:`~PyQt6.QtGui.QPainter.end` to paint on external devices, e.g. printers.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.begin`, :sip:ref:`~PyQt6.QtGui.QPainter.end`.
