.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 7f8761fe40e3472630070d69f726178b

Returns ``true`` if this layout's preferred height depends on its width; otherwise returns ``false``. The default implementation returns false.

Reimplement this function in layout managers that support height for width.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QLayoutItem.heightForWidth`, :sip:ref:`~PyQt6.QtWidgets.QWidget.heightForWidth`.
