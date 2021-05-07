.. sip:class-description::
    :status: todo
    :brief: Basic wheel mouse based input handler
    :digest: 4c48bf85f370887609ef6b8dabc761fc

Basic wheel mouse based input handler.

:sip:ref:`~PyQt6.QtDataVisualization.Q3DInputHandler` is the basic input handler for wheel mouse type of input devices.

Default input handler has the following functionalty:

+-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Mouse action                                                      | Action                                                                                                                                                                   |
+===================================================================+==========================================================================================================================================================================+
| Drag with right button pressed                                    | Rotate graph within limits set for :sip:ref:`~PyQt6.QtDataVisualization.Q3DCamera`.                                                                                      |
+-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Left click                                                        | Select item under cursor or remove selection if none. May open the secondary view depending on the :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.selectionMode`. |
+-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Mouse wheel                                                       | Zoom in/out within the allowable zoom range set for :sip:ref:`~PyQt6.QtDataVisualization.Q3DCamera`.                                                                     |
+-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Left click on the primary view when the secondary view is visible | Closes the secondary view.                                                                                                                                               |
|                                                                   |                                                                                                                                                                          |
|                                                                   | **Note:** Secondary view is available only for :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars` and :sip:ref:`~PyQt6.QtDataVisualization.Q3DSurface` graphs.                |
+-------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Rotation, zoom, and selection can each be individually disabled using corresponding properties of this class.
