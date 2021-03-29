.. sip:method-description::
    :status: todo
    :pysig: a353b4c474d5186a8e05e6a56fd80e81
    :realsig: (QWidget*,const QString&,const QString&)
    :digest: c1aaadfd43372836bd749fa24716ef48

Displays a simple about box with title *title* and text *text*. The about box's parent is *parent*.

looks for a suitable icon in four locations:

#. It prefers :sip:ref:`~PyQt6.QtWidgets.QWidget.windowIcon` if that exists.

#. If not, it tries the top-level widget containing *parent*.

#. If that fails, it tries the :sip:ref:`~PyQt6.QtWidgets.QApplication.activeWindow`

#. As a last resort it uses the Information icon.

The about box has a single button labelled "OK". On macOS, the about box is popped up as a modeless window; on other platforms, it is currently application modal.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.windowIcon`, :sip:ref:`~PyQt6.QtWidgets.QApplication.activeWindow`.
