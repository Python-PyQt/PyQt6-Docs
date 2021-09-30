.. sip:class-description::
    :status: todo
    :brief: Enables the detection of proximity changes for a specified set of coordinates
    :digest: 98e1dd2c6683eb4962aed9d7cff632eb

The :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorSource` class enables the detection of proximity changes for a specified set of coordinates.

A :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorSource` emits signals when the current position is in range, or has moved out of range, of a specified area. Each area is specified by a :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorInfo` object. For example:

.. literalinclude:: ../../../snippets/qtpositioning-src-positioning-doc-snippets-cpp-cppqml.py
    :lines: 84-118

``QGeoAreaMonitorSource`` follows a singleton pattern. Each instance of the class with the same :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorSource.sourceName` shares the same area monitoring backend. If a new :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorInfo` object is added via :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorSource.startMonitoring` or :sip:ref:`~PyQt6.QtPositioning.QGeoAreaMonitorSource.requestUpdate` it can be retrieved by another instance of this class (provided that they are sourced from the same area monitor provider plug-in). The same singleton pattern applies to the :sip:ref:`~PyQt6.QtPositioning.QGeoPositionInfoSource` instance used by this class. The following code snippet emphasizes the behavior:

::

    QGeoAreaMonitorSource *s1 = QGeoAreaMonitorSource::createSource("blah", this);
    QGeoAreaMonitorSource *s2 = QGeoAreaMonitorSource::createSource("blah", this);
    QVERIFY(s1->positionInfoSource() == s2->positionInfoSource);
