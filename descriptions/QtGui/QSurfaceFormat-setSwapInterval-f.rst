.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 379556681cfa94f4c951ea65f862a792

Sets the preferred swap interval. The swap interval specifies the minimum number of video frames that are displayed before a buffer swap occurs. This can be used to sync the GL drawing into a window to the vertical refresh of the screen.

Setting an *interval* value of 0 will turn the vertical refresh syncing off, any value higher than 0 will turn the vertical syncing on. Setting *interval* to a higher value, for example 10, results in having 10 vertical retraces between every buffer swap.

The default interval is 1.

Changing the swap interval may not be supported by the underlying platform. In this case, the request will be silently ignored.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.swapInterval`.
