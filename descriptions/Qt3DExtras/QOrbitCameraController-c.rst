.. sip:class-description::
    :status: todo
    :brief: Allows controlling the scene camera along orbital path
    :realname: Qt3DExtras::QOrbitCameraController
    :digest: 1cd76341160ad76948762e8d08b85419

The :sip:ref:`~PyQt6.Qt3DExtras.QOrbitCameraController` class allows controlling the scene camera along orbital path.

The controls are:

+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Input                            | Action                                                                                                                                                                               |
+==================================+======================================================================================================================================================================================+
| Left mouse button                | While the left mouse button is pressed, mouse movement along x-axis moves the camera left and right and movement along y-axis moves it up and down.                                  |
+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Right mouse button               | While the right mouse button is pressed, mouse movement along x-axis pans the camera around the camera view center and movement along y-axis tilts it around the camera view center. |
+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Both left and right mouse button | While both the left and the right mouse button are pressed, mouse movement along y-axis zooms the camera in and out without changing the view center.                                |
+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Mouse scroll wheel               | Zooms the camera in and out without changing the view center.                                                                                                                        |
+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Arrow keys                       | Move the camera vertically and horizontally relative to camera viewport.                                                                                                             |
+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Page up and page down keys       | Move the camera forwards and backwards.                                                                                                                                              |
+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Shift key                        | Changes the behavior of the up and down arrow keys to zoom the camera in and out without changing the view center. The other movement keys are disabled.                             |
+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Alt key                          | Changes the behovior of the arrow keys to pan and tilt the camera around the view center. Disables the page up and page down keys.                                                   |
+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Escape                           | Moves the camera so that entire scene is visible in the camera viewport.                                                                                                             |
+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
