.. sip:class-description::
    :status: todo
    :brief: Basic touch display based input handler
    :digest: b933a584a2d8493ba3094acc63eac18e

Basic touch display based input handler.

:sip:ref:`~PyQt6.QtDataVisualization.QTouch3DInputHandler` is the basic input handler for touch screen devices.

Default touch input handler has the following functionalty:

+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Gesture                                                    | Action                                                                                                                                                                 |
+============================================================+========================================================================================================================================================================+
| Touch-And-Move                                             | Rotate graph within limits set for :sip:ref:`~PyQt6.QtDataVisualization.Q3DCamera`                                                                                     |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Tap                                                        | Select the item tapped or remove selection if none. May open the secondary view depending on the :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.selectionMode`. |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Tap-And-Hold                                               | Same as tap.                                                                                                                                                           |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pinch                                                      | Zoom in/out within the allowable zoom range set for :sip:ref:`~PyQt6.QtDataVisualization.Q3DCamera`.                                                                   |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Tap on the primary view when the secondary view is visible | Closes the secondary view.                                                                                                                                             |
|                                                            |                                                                                                                                                                        |
|                                                            | **Note:** Secondary view is available only for :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars` and :sip:ref:`~PyQt6.QtDataVisualization.Q3DSurface` graphs.              |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Rotation, zoom, and selection can each be individually disabled using corresponding :sip:ref:`~PyQt6.QtDataVisualization.Q3DInputHandler` properties.
