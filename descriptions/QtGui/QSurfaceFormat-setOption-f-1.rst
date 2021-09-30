.. sip:method-description::
    :status: todo
    :pysig: 7011b48ec9397c37aec33c514bb306f1
    :realsig: (QSurfaceFormat::FormatOption,bool)
    :digest: 4f41ee6cc8e8003751a1a03ce4848fa5

Sets the format option *option* if *on* is true; otherwise, clears the option.

To verify that an option was respected, compare the actual format to the requested format after surface/context creation.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.setOptions`, :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.options`, :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.testOption`.
