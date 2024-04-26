.. sip:method-description::
    :status: todo
    :pysig: 0ac588f24c06cea5b065ba516eab44ac
    :realsig: (bool)
    :digest: 5729483a27f9e875555a090bc799d609

This convenience function can be used to create a custom surface format suitable for use by Qt Data Visualization graphs.

The *antialias* parameter specifies whether or not antialiasing is activated.

Give the surface format returned by this function to the graph constructor (C++) or set it as the window format for :sip:ref:`~PyQt6.QtQuick.QQuickView` (QML) before calling ``show()`` on it.

For example, disable antialiasing on C++ application:

::

    #include <QtDataVisualization/qutils.h>

    // ...

    Q3DBars *graph = new Q3DBars(qDefaultSurfaceFormat(false));

For example, enable antialiasing for direct rendering modes on QML application:

::

    #include <QtDataVisualization/qutils.h>

    // ...

    QQuickView viewer;
    viewer.setFormat(qDefaultSurfaceFormat(true));

**Note:** Antialiasing is not supported in OpenGL ES2 environments.
