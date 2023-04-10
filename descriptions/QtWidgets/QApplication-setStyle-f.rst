.. sip:method-description::
    :status: todo
    :pysig: 81c2c045afaaf2ef39885ece474078f0
    :realsig: (QStyle*)
    :digest: 37dbdea1c0519c00f7f0bf5916c704f5

Sets the application's GUI style to *style*. Ownership of the style object is transferred to :sip:ref:`~PyQt6.QtWidgets.QApplication`, so :sip:ref:`~PyQt6.QtWidgets.QApplication` will delete the style object on application exit or when a new style is set and the old style is still the parent of the application object.

Example usage:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_kernel_qapplication.py
    :lines: 79-79

When switching application styles, the color palette is set back to the initial colors or the system defaults. This is necessary since certain styles have to adapt the color palette to be fully style-guide compliant.

Setting the style before a palette has been set, i.e., before creating :sip:ref:`~PyQt6.QtWidgets.QApplication`, will cause the application to use :sip:ref:`~PyQt6.QtWidgets.QStyle.standardPalette` for the palette.

**Warning:** Qt style sheets are currently not supported for custom :sip:ref:`~PyQt6.QtWidgets.QStyle` subclasses. We plan to address this in some future release.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QApplication.style`, :sip:ref:`~PyQt6.QtWidgets.QStyle`, :sip:ref:`~PyQt6.QtWidgets.QApplication.setPalette`.
