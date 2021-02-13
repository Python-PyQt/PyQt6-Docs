.. sip:method-description::
    :status: todo
    :pysig: 67c8f8ac61708663646cfffecd59cbae
    :realsig: () const
    :digest: 5050f62fea1fd15ddf3b9e0a336eb77b

Returns the style's standard palette.

Note that on systems that support system colors, the style's standard palette is not used. In particular, the Windows Vista and Mac styles do not use the standard palette, but make use of native theme engines. With these styles, you should not set the palette with :sip:ref:`~PyQt6.QtWidgets.QApplication.setPalette`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QApplication.setPalette`.
