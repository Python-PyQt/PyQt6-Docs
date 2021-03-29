.. sip:class-description::
    :status: todo
    :brief: Defines an interface for how QPrinter interacts with a given printing subsystem
    :digest: a29957f50e3cc9467522741e56a5cef5

The :sip:ref:`~PyQt6.QtPrintSupport.QPrintEngine` class defines an interface for how :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` interacts with a given printing subsystem.

The common case when creating your own print engine is to derive from both :sip:ref:`~PyQt6.QtGui.QPaintEngine` and :sip:ref:`~PyQt6.QtPrintSupport.QPrintEngine`. Various properties of a print engine are given with :sip:ref:`~PyQt6.QtPrintSupport.QPrintEngine.property` and set with :sip:ref:`~PyQt6.QtPrintSupport.QPrintEngine.setProperty`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPaintEngine`.
