.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: cd0b3e8b89d3a9f0e56804877ddd6dcd

Repaints the widget directly by calling :sip:ref:`~PyQt6.QtWidgets.QWidget.paintEvent` immediately, unless updates are disabled or the widget is hidden.

We suggest only using repaint() if you need an immediate repaint, for example during animation. In almost all circumstances :sip:ref:`~PyQt6.QtWidgets.QWidget.update` is better, as it permits Qt to optimize for speed and minimize flicker.

**Warning:** If you call repaint() in a function which may itself be called from :sip:ref:`~PyQt6.QtWidgets.QWidget.paintEvent`, you may get infinite recursion. The :sip:ref:`~PyQt6.QtWidgets.QWidget.update` function never causes recursion.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.update`, :sip:ref:`~PyQt6.QtWidgets.QWidget.paintEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.setUpdatesEnabled`.
