.. sip:method-description::
    :status: todo
    :pysig: f7dba2c0411c0ef6af4394e6fc1d3906
    :realsig: (const QBitmap&)
    :digest: d30bd6560b3a2cc5b037d107f9479a0f

Causes only the pixels of the widget for which *bitmap* has a corresponding 1 bit to be visible. If the region includes pixels outside the :sip:ref:`~PyQt6.QtWidgets.QWidget.rect` of the widget, window system controls in that area may or may not be visible, depending on the platform.

Note that this effect can be slow if the region is particularly complex.

The following code shows how an image with an alpha channel can be used to generate a mask for a widget:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-widget-mask-main.py
    :lines: 59-62

The label shown by this code is masked using the image it contains, giving the appearance that an irregularly-shaped image is being drawn directly onto the screen.

Masked widgets receive mouse events only on their visible portions.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.mask`, :sip:ref:`~PyQt6.QtWidgets.QWidget.clearMask`, :sip:ref:`~PyQt6.QtWidgets.QWidget.windowOpacity`.
