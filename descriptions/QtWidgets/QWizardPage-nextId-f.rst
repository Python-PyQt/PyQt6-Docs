.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: b0935191ecbbda0036751b95f893f1f0

This virtual function is called by :sip:ref:`~PyQt6.QtWidgets.QWizard.nextId` to find out which page to show when the user clicks the Next button.

The return value is the ID of the next page, or -1 if no page follows.

By default, this function returns the lowest ID greater than the ID of the current page, or -1 if there is no such ID.

By reimplementing this function, you can specify a dynamic page order. For example:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-licensewizard-licensewizard.py
    :lines: 175-183

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizard.nextId`.
