.. sip:method-description::
    :status: todo
    :pysig: c5d6e3115e754b395283dc1c09f54493
    :realsig: () const
    :digest: 8722d364e063d75033c9bc280ae96501

Returns the definition size of the page size.

For a standard page size this will be the size as defined in the relevant standard, i.e. ISO A4 will be defined in millimeters while ANSI Letter will be defined in inches.

For a custom page size this will be the original size used to create the page size object.

If the :sip:ref:`~PyQt6.QtGui.QPageSize` is invalid then the :sip:ref:`~PyQt6.QtCore.QSizeF` will be invalid.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPageSize.definitionUnits`.
