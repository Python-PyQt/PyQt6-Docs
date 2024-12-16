.. sip:method-description::
    :status: todo
    :pysig: 0ac588f24c06cea5b065ba516eab44ac
    :realsig: (bool)
    :digest: 53dd83e2271adf2acbb77b5e747c3a9f

This convenience function can be used to create a custom surface format suitable for use by Qt Graphs graphs.

The *antialias* parameter specifies whether or not antialiasing is activated.

Give the surface format returned by this function to the graph constructor (C++) or set it as the window format for :sip:ref:`~PyQt6.QtQuick.QQuickView` (QML) before calling ``show()`` on it.

For example, disable antialiasing on C++ application:

::

    #include <QtGraphs/qutils.h>

    // ...

    Q3DBars *graph = new Q3DBars(qDefaultSurfaceFormat(false));

For example, enable antialiasing for direct rendering modes on QML application:

::

    #include <QtGraphs/qutils.h>

    // ...

    QQuickView viewer;
    viewer.setFormat(qDefaultSurfaceFormat(true));
