.. sip:enum-description::
    :status: todo
    :digest: 83e3e586b7c421cefff63c7b813e97dd

Defines the attributes for positional information.

NMEA protocol also suggests another type of accuracy - PositionAccuracy, which is a 3D accuracy value. Qt does not provide a separate attribute for it. If you need this value, you can calculate it based on the following formula:

``PositionAccuracy`` :sup:`2` ``= HorizontalAccuracy`` :sup:`2` ``+ VerticalAccuracy`` :sup:`2`
