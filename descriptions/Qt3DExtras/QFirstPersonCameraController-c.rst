.. sip:class-description::
    :status: todo
    :brief: Allows controlling the scene camera from the first person perspective
    :realname: Qt3DExtras::QFirstPersonCameraController
    :digest: d158a8a5820ebd85feab0d3721c8acb7

The :sip:ref:`~PyQt6.Qt3DExtras.QFirstPersonCameraController` class allows controlling the scene camera from the first person perspective.

The controls are:

+----------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Input                      | Action                                                                                                                  |
+============================+=========================================================================================================================+
| Left mouse button          | While the left mouse button is pressed, mouse movement along x-axis pans the camera and movement along y-axis tilts it. |
+----------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Mouse scroll wheel         | Zooms the camera in and out without changing the view center.                                                           |
+----------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Shift key                  | Turns the fine motion control active while pressed. Makes mouse pan and tilt less sensitive.                            |
+----------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Arrow keys                 | Move the camera horizontally relative to camera viewport.                                                               |
+----------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Page up and page down keys | Move the camera vertically relative to camera viewport.                                                                 |
+----------------------------+-------------------------------------------------------------------------------------------------------------------------+
| Escape                     | Moves the camera so that entire scene is visible in the camera viewport.                                                |
+----------------------------+-------------------------------------------------------------------------------------------------------------------------+
