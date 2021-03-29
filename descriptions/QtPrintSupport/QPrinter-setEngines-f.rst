.. sip:method-description::
    :status: todo
    :pysig: 87f0a6391ae88ac6f2999cfb123060fa
    :realsig: (QPrintEngine*,QPaintEngine*)
    :digest: eba88f64cab0e403bca515d52e36130e

This function is used by subclasses of :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` to specify custom print and paint engines (\ *printEngine* and *paintEngine*, respectively).

:sip:ref:`~PyQt6.QtPrintSupport.QPrinter` does not take ownership of the engines, so you need to manage these engine instances yourself.

Note that changing the engines will reset the printer state and all its properties.

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.printEngine`, :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.paintEngine`, :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.setOutputFormat`.
