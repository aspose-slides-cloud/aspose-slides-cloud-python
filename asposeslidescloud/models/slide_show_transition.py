# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose">
#   Copyright (c) 2018 Aspose.Slides for Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------

import pprint
import re  # noqa: F401

import six


class SlideShowTransition(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'advance_after': 'bool',
        'advance_after_time': 'int',
        'advance_on_click': 'bool',
        'sound_is_built_in': 'bool',
        'sound_loop': 'bool',
        'sound_mode': 'str',
        'sound_name': 'str',
        'speed': 'str',
        'corner_direction': 'str',
        'eight_direction': 'str',
        'in_out_direction': 'str',
        'has_bounce': 'bool',
        'side_direction': 'str',
        'pattern': 'str',
        'left_right_direction': 'str',
        'morph_type': 'str',
        'from_black': 'bool',
        'orientation_direction': 'str',
        'through_black': 'bool',
        'corner_and_center_direction': 'str',
        'shred_pattern': 'str',
        'orientation': 'str',
        'spokes': 'int'
    }

    attribute_map = {
        'type': 'type',
        'advance_after': 'advanceAfter',
        'advance_after_time': 'advanceAfterTime',
        'advance_on_click': 'advanceOnClick',
        'sound_is_built_in': 'soundIsBuiltIn',
        'sound_loop': 'soundLoop',
        'sound_mode': 'soundMode',
        'sound_name': 'soundName',
        'speed': 'speed',
        'corner_direction': 'cornerDirection',
        'eight_direction': 'eightDirection',
        'in_out_direction': 'inOutDirection',
        'has_bounce': 'hasBounce',
        'side_direction': 'sideDirection',
        'pattern': 'pattern',
        'left_right_direction': 'leftRightDirection',
        'morph_type': 'morphType',
        'from_black': 'fromBlack',
        'orientation_direction': 'orientationDirection',
        'through_black': 'throughBlack',
        'corner_and_center_direction': 'cornerAndCenterDirection',
        'shred_pattern': 'shredPattern',
        'orientation': 'orientation',
        'spokes': 'spokes'
    }

    type_determiners = {
    }

    def __init__(self, type=None, advance_after=None, advance_after_time=None, advance_on_click=None, sound_is_built_in=None, sound_loop=None, sound_mode=None, sound_name=None, speed=None, corner_direction=None, eight_direction=None, in_out_direction=None, has_bounce=None, side_direction=None, pattern=None, left_right_direction=None, morph_type=None, from_black=None, orientation_direction=None, through_black=None, corner_and_center_direction=None, shred_pattern=None, orientation=None, spokes=None):  # noqa: E501
        """SlideShowTransition - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._advance_after = None
        self._advance_after_time = None
        self._advance_on_click = None
        self._sound_is_built_in = None
        self._sound_loop = None
        self._sound_mode = None
        self._sound_name = None
        self._speed = None
        self._corner_direction = None
        self._eight_direction = None
        self._in_out_direction = None
        self._has_bounce = None
        self._side_direction = None
        self._pattern = None
        self._left_right_direction = None
        self._morph_type = None
        self._from_black = None
        self._orientation_direction = None
        self._through_black = None
        self._corner_and_center_direction = None
        self._shred_pattern = None
        self._orientation = None
        self._spokes = None

        if type is not None:
            self.type = type
        if advance_after is not None:
            self.advance_after = advance_after
        if advance_after_time is not None:
            self.advance_after_time = advance_after_time
        if advance_on_click is not None:
            self.advance_on_click = advance_on_click
        if sound_is_built_in is not None:
            self.sound_is_built_in = sound_is_built_in
        if sound_loop is not None:
            self.sound_loop = sound_loop
        if sound_mode is not None:
            self.sound_mode = sound_mode
        if sound_name is not None:
            self.sound_name = sound_name
        if speed is not None:
            self.speed = speed
        if corner_direction is not None:
            self.corner_direction = corner_direction
        if eight_direction is not None:
            self.eight_direction = eight_direction
        if in_out_direction is not None:
            self.in_out_direction = in_out_direction
        if has_bounce is not None:
            self.has_bounce = has_bounce
        if side_direction is not None:
            self.side_direction = side_direction
        if pattern is not None:
            self.pattern = pattern
        if left_right_direction is not None:
            self.left_right_direction = left_right_direction
        if morph_type is not None:
            self.morph_type = morph_type
        if from_black is not None:
            self.from_black = from_black
        if orientation_direction is not None:
            self.orientation_direction = orientation_direction
        if through_black is not None:
            self.through_black = through_black
        if corner_and_center_direction is not None:
            self.corner_and_center_direction = corner_and_center_direction
        if shred_pattern is not None:
            self.shred_pattern = shred_pattern
        if orientation is not None:
            self.orientation = orientation
        if spokes is not None:
            self.spokes = spokes

    @property
    def type(self):
        """Gets the type of this SlideShowTransition.  # noqa: E501

        Transition Type  # noqa: E501

        :return: The type of this SlideShowTransition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SlideShowTransition.

        Transition Type  # noqa: E501

        :param type: The type of this SlideShowTransition.  # noqa: E501
        :type: str
        """
        if type is not None:
            allowed_values = ["None", "Blinds", "Checker", "Circle", "Comb", "Cover", "Cut", "Diamond", "Dissolve", "Fade", "Newsflash", "Plus", "Pull", "Push", "Random", "RandomBar", "Split", "Strips", "Wedge", "Wheel", "Wipe", "Zoom", "Vortex", "Switch", "Flip", "Ripple", "Honeycomb", "Cube", "Box", "Rotate", "Orbit", "Doors", "Window", "Ferris", "Gallery", "Conveyor", "Pan", "Glitter", "Warp", "Flythrough", "Flash", "Shred", "Reveal", "WheelReverse", "FallOver", "Drape", "Curtains", "Wind", "Prestige", "Fracture", "Crush", "PeelOff", "PageCurlDouble", "PageCurlSingle", "Airplane", "Origami", "Morph"]  # noqa: E501
            if type.isdigit():
                int_type = int(type)
                if int_type < 0 or int_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                        .format(type, allowed_values)
                    )
                self._type = allowed_values[int_type]
                return
            if type not in allowed_values:
                raise ValueError(
                    "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                    .format(type, allowed_values)
                )
        self._type = type

    @property
    def advance_after(self):
        """Gets the advance_after of this SlideShowTransition.  # noqa: E501

        Advance After  # noqa: E501

        :return: The advance_after of this SlideShowTransition.  # noqa: E501
        :rtype: bool
        """
        return self._advance_after

    @advance_after.setter
    def advance_after(self, advance_after):
        """Sets the advance_after of this SlideShowTransition.

        Advance After  # noqa: E501

        :param advance_after: The advance_after of this SlideShowTransition.  # noqa: E501
        :type: bool
        """
        self._advance_after = advance_after

    @property
    def advance_after_time(self):
        """Gets the advance_after_time of this SlideShowTransition.  # noqa: E501

        Advance After Time  # noqa: E501

        :return: The advance_after_time of this SlideShowTransition.  # noqa: E501
        :rtype: int
        """
        return self._advance_after_time

    @advance_after_time.setter
    def advance_after_time(self, advance_after_time):
        """Sets the advance_after_time of this SlideShowTransition.

        Advance After Time  # noqa: E501

        :param advance_after_time: The advance_after_time of this SlideShowTransition.  # noqa: E501
        :type: int
        """
        self._advance_after_time = advance_after_time

    @property
    def advance_on_click(self):
        """Gets the advance_on_click of this SlideShowTransition.  # noqa: E501

        Advance On Click  # noqa: E501

        :return: The advance_on_click of this SlideShowTransition.  # noqa: E501
        :rtype: bool
        """
        return self._advance_on_click

    @advance_on_click.setter
    def advance_on_click(self, advance_on_click):
        """Sets the advance_on_click of this SlideShowTransition.

        Advance On Click  # noqa: E501

        :param advance_on_click: The advance_on_click of this SlideShowTransition.  # noqa: E501
        :type: bool
        """
        self._advance_on_click = advance_on_click

    @property
    def sound_is_built_in(self):
        """Gets the sound_is_built_in of this SlideShowTransition.  # noqa: E501

        Sound Is Built In  # noqa: E501

        :return: The sound_is_built_in of this SlideShowTransition.  # noqa: E501
        :rtype: bool
        """
        return self._sound_is_built_in

    @sound_is_built_in.setter
    def sound_is_built_in(self, sound_is_built_in):
        """Sets the sound_is_built_in of this SlideShowTransition.

        Sound Is Built In  # noqa: E501

        :param sound_is_built_in: The sound_is_built_in of this SlideShowTransition.  # noqa: E501
        :type: bool
        """
        self._sound_is_built_in = sound_is_built_in

    @property
    def sound_loop(self):
        """Gets the sound_loop of this SlideShowTransition.  # noqa: E501

        Sound Loop  # noqa: E501

        :return: The sound_loop of this SlideShowTransition.  # noqa: E501
        :rtype: bool
        """
        return self._sound_loop

    @sound_loop.setter
    def sound_loop(self, sound_loop):
        """Sets the sound_loop of this SlideShowTransition.

        Sound Loop  # noqa: E501

        :param sound_loop: The sound_loop of this SlideShowTransition.  # noqa: E501
        :type: bool
        """
        self._sound_loop = sound_loop

    @property
    def sound_mode(self):
        """Gets the sound_mode of this SlideShowTransition.  # noqa: E501

        Sound Mode  # noqa: E501

        :return: The sound_mode of this SlideShowTransition.  # noqa: E501
        :rtype: str
        """
        return self._sound_mode

    @sound_mode.setter
    def sound_mode(self, sound_mode):
        """Sets the sound_mode of this SlideShowTransition.

        Sound Mode  # noqa: E501

        :param sound_mode: The sound_mode of this SlideShowTransition.  # noqa: E501
        :type: str
        """
        if sound_mode is not None:
            allowed_values = ["StartSound", "StopPrevoiusSound", "NotDefined"]  # noqa: E501
            if sound_mode.isdigit():
                int_sound_mode = int(sound_mode)
                if int_sound_mode < 0 or int_sound_mode >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `sound_mode` ({0}), must be one of {1}"  # noqa: E501
                        .format(sound_mode, allowed_values)
                    )
                self._sound_mode = allowed_values[int_sound_mode]
                return
            if sound_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `sound_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(sound_mode, allowed_values)
                )
        self._sound_mode = sound_mode

    @property
    def sound_name(self):
        """Gets the sound_name of this SlideShowTransition.  # noqa: E501

        Sound Name  # noqa: E501

        :return: The sound_name of this SlideShowTransition.  # noqa: E501
        :rtype: str
        """
        return self._sound_name

    @sound_name.setter
    def sound_name(self, sound_name):
        """Sets the sound_name of this SlideShowTransition.

        Sound Name  # noqa: E501

        :param sound_name: The sound_name of this SlideShowTransition.  # noqa: E501
        :type: str
        """
        self._sound_name = sound_name

    @property
    def speed(self):
        """Gets the speed of this SlideShowTransition.  # noqa: E501

        Speed  # noqa: E501

        :return: The speed of this SlideShowTransition.  # noqa: E501
        :rtype: str
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this SlideShowTransition.

        Speed  # noqa: E501

        :param speed: The speed of this SlideShowTransition.  # noqa: E501
        :type: str
        """
        if speed is not None:
            allowed_values = ["Fast", "Medium", "Slow"]  # noqa: E501
            if speed.isdigit():
                int_speed = int(speed)
                if int_speed < 0 or int_speed >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `speed` ({0}), must be one of {1}"  # noqa: E501
                        .format(speed, allowed_values)
                    )
                self._speed = allowed_values[int_speed]
                return
            if speed not in allowed_values:
                raise ValueError(
                    "Invalid value for `speed` ({0}), must be one of {1}"  # noqa: E501
                    .format(speed, allowed_values)
                )
        self._speed = speed

    @property
    def corner_direction(self):
        """Gets the corner_direction of this SlideShowTransition.  # noqa: E501

        Corner Direction.  # noqa: E501

        :return: The corner_direction of this SlideShowTransition.  # noqa: E501
        :rtype: str
        """
        return self._corner_direction

    @corner_direction.setter
    def corner_direction(self, corner_direction):
        """Sets the corner_direction of this SlideShowTransition.

        Corner Direction.  # noqa: E501

        :param corner_direction: The corner_direction of this SlideShowTransition.  # noqa: E501
        :type: str
        """
        if corner_direction is not None:
            allowed_values = ["LeftDown", "LeftUp", "RightDown", "RightUp"]  # noqa: E501
            if corner_direction.isdigit():
                int_corner_direction = int(corner_direction)
                if int_corner_direction < 0 or int_corner_direction >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `corner_direction` ({0}), must be one of {1}"  # noqa: E501
                        .format(corner_direction, allowed_values)
                    )
                self._corner_direction = allowed_values[int_corner_direction]
                return
            if corner_direction not in allowed_values:
                raise ValueError(
                    "Invalid value for `corner_direction` ({0}), must be one of {1}"  # noqa: E501
                    .format(corner_direction, allowed_values)
                )
        self._corner_direction = corner_direction

    @property
    def eight_direction(self):
        """Gets the eight_direction of this SlideShowTransition.  # noqa: E501

        Eight Direction.  # noqa: E501

        :return: The eight_direction of this SlideShowTransition.  # noqa: E501
        :rtype: str
        """
        return self._eight_direction

    @eight_direction.setter
    def eight_direction(self, eight_direction):
        """Sets the eight_direction of this SlideShowTransition.

        Eight Direction.  # noqa: E501

        :param eight_direction: The eight_direction of this SlideShowTransition.  # noqa: E501
        :type: str
        """
        if eight_direction is not None:
            allowed_values = ["LeftDown", "LeftUp", "RightDown", "RightUp", "Left", "Up", "Down", "Right"]  # noqa: E501
            if eight_direction.isdigit():
                int_eight_direction = int(eight_direction)
                if int_eight_direction < 0 or int_eight_direction >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `eight_direction` ({0}), must be one of {1}"  # noqa: E501
                        .format(eight_direction, allowed_values)
                    )
                self._eight_direction = allowed_values[int_eight_direction]
                return
            if eight_direction not in allowed_values:
                raise ValueError(
                    "Invalid value for `eight_direction` ({0}), must be one of {1}"  # noqa: E501
                    .format(eight_direction, allowed_values)
                )
        self._eight_direction = eight_direction

    @property
    def in_out_direction(self):
        """Gets the in_out_direction of this SlideShowTransition.  # noqa: E501

        In/Out Direction.  # noqa: E501

        :return: The in_out_direction of this SlideShowTransition.  # noqa: E501
        :rtype: str
        """
        return self._in_out_direction

    @in_out_direction.setter
    def in_out_direction(self, in_out_direction):
        """Sets the in_out_direction of this SlideShowTransition.

        In/Out Direction.  # noqa: E501

        :param in_out_direction: The in_out_direction of this SlideShowTransition.  # noqa: E501
        :type: str
        """
        if in_out_direction is not None:
            allowed_values = ["In", "Out"]  # noqa: E501
            if in_out_direction.isdigit():
                int_in_out_direction = int(in_out_direction)
                if int_in_out_direction < 0 or int_in_out_direction >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `in_out_direction` ({0}), must be one of {1}"  # noqa: E501
                        .format(in_out_direction, allowed_values)
                    )
                self._in_out_direction = allowed_values[int_in_out_direction]
                return
            if in_out_direction not in allowed_values:
                raise ValueError(
                    "Invalid value for `in_out_direction` ({0}), must be one of {1}"  # noqa: E501
                    .format(in_out_direction, allowed_values)
                )
        self._in_out_direction = in_out_direction

    @property
    def has_bounce(self):
        """Gets the has_bounce of this SlideShowTransition.  # noqa: E501

        Has Bounce.  # noqa: E501

        :return: The has_bounce of this SlideShowTransition.  # noqa: E501
        :rtype: bool
        """
        return self._has_bounce

    @has_bounce.setter
    def has_bounce(self, has_bounce):
        """Sets the has_bounce of this SlideShowTransition.

        Has Bounce.  # noqa: E501

        :param has_bounce: The has_bounce of this SlideShowTransition.  # noqa: E501
        :type: bool
        """
        self._has_bounce = has_bounce

    @property
    def side_direction(self):
        """Gets the side_direction of this SlideShowTransition.  # noqa: E501

        Side Direction.  # noqa: E501

        :return: The side_direction of this SlideShowTransition.  # noqa: E501
        :rtype: str
        """
        return self._side_direction

    @side_direction.setter
    def side_direction(self, side_direction):
        """Sets the side_direction of this SlideShowTransition.

        Side Direction.  # noqa: E501

        :param side_direction: The side_direction of this SlideShowTransition.  # noqa: E501
        :type: str
        """
        if side_direction is not None:
            allowed_values = ["Left", "Up", "Down", "Right"]  # noqa: E501
            if side_direction.isdigit():
                int_side_direction = int(side_direction)
                if int_side_direction < 0 or int_side_direction >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `side_direction` ({0}), must be one of {1}"  # noqa: E501
                        .format(side_direction, allowed_values)
                    )
                self._side_direction = allowed_values[int_side_direction]
                return
            if side_direction not in allowed_values:
                raise ValueError(
                    "Invalid value for `side_direction` ({0}), must be one of {1}"  # noqa: E501
                    .format(side_direction, allowed_values)
                )
        self._side_direction = side_direction

    @property
    def pattern(self):
        """Gets the pattern of this SlideShowTransition.  # noqa: E501

        Pattern.  # noqa: E501

        :return: The pattern of this SlideShowTransition.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this SlideShowTransition.

        Pattern.  # noqa: E501

        :param pattern: The pattern of this SlideShowTransition.  # noqa: E501
        :type: str
        """
        if pattern is not None:
            allowed_values = ["Diamond", "Hexagon"]  # noqa: E501
            if pattern.isdigit():
                int_pattern = int(pattern)
                if int_pattern < 0 or int_pattern >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `pattern` ({0}), must be one of {1}"  # noqa: E501
                        .format(pattern, allowed_values)
                    )
                self._pattern = allowed_values[int_pattern]
                return
            if pattern not in allowed_values:
                raise ValueError(
                    "Invalid value for `pattern` ({0}), must be one of {1}"  # noqa: E501
                    .format(pattern, allowed_values)
                )
        self._pattern = pattern

    @property
    def left_right_direction(self):
        """Gets the left_right_direction of this SlideShowTransition.  # noqa: E501

        Left/Right Direction.  # noqa: E501

        :return: The left_right_direction of this SlideShowTransition.  # noqa: E501
        :rtype: str
        """
        return self._left_right_direction

    @left_right_direction.setter
    def left_right_direction(self, left_right_direction):
        """Sets the left_right_direction of this SlideShowTransition.

        Left/Right Direction.  # noqa: E501

        :param left_right_direction: The left_right_direction of this SlideShowTransition.  # noqa: E501
        :type: str
        """
        if left_right_direction is not None:
            allowed_values = ["Left", "Right"]  # noqa: E501
            if left_right_direction.isdigit():
                int_left_right_direction = int(left_right_direction)
                if int_left_right_direction < 0 or int_left_right_direction >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `left_right_direction` ({0}), must be one of {1}"  # noqa: E501
                        .format(left_right_direction, allowed_values)
                    )
                self._left_right_direction = allowed_values[int_left_right_direction]
                return
            if left_right_direction not in allowed_values:
                raise ValueError(
                    "Invalid value for `left_right_direction` ({0}), must be one of {1}"  # noqa: E501
                    .format(left_right_direction, allowed_values)
                )
        self._left_right_direction = left_right_direction

    @property
    def morph_type(self):
        """Gets the morph_type of this SlideShowTransition.  # noqa: E501

        Morph Type.  # noqa: E501

        :return: The morph_type of this SlideShowTransition.  # noqa: E501
        :rtype: str
        """
        return self._morph_type

    @morph_type.setter
    def morph_type(self, morph_type):
        """Sets the morph_type of this SlideShowTransition.

        Morph Type.  # noqa: E501

        :param morph_type: The morph_type of this SlideShowTransition.  # noqa: E501
        :type: str
        """
        if morph_type is not None:
            allowed_values = ["ByObject", "ByWord", "ByChar"]  # noqa: E501
            if morph_type.isdigit():
                int_morph_type = int(morph_type)
                if int_morph_type < 0 or int_morph_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `morph_type` ({0}), must be one of {1}"  # noqa: E501
                        .format(morph_type, allowed_values)
                    )
                self._morph_type = allowed_values[int_morph_type]
                return
            if morph_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `morph_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(morph_type, allowed_values)
                )
        self._morph_type = morph_type

    @property
    def from_black(self):
        """Gets the from_black of this SlideShowTransition.  # noqa: E501

        From Black.  # noqa: E501

        :return: The from_black of this SlideShowTransition.  # noqa: E501
        :rtype: bool
        """
        return self._from_black

    @from_black.setter
    def from_black(self, from_black):
        """Sets the from_black of this SlideShowTransition.

        From Black.  # noqa: E501

        :param from_black: The from_black of this SlideShowTransition.  # noqa: E501
        :type: bool
        """
        self._from_black = from_black

    @property
    def orientation_direction(self):
        """Gets the orientation_direction of this SlideShowTransition.  # noqa: E501

        Orientation Direction.  # noqa: E501

        :return: The orientation_direction of this SlideShowTransition.  # noqa: E501
        :rtype: str
        """
        return self._orientation_direction

    @orientation_direction.setter
    def orientation_direction(self, orientation_direction):
        """Sets the orientation_direction of this SlideShowTransition.

        Orientation Direction.  # noqa: E501

        :param orientation_direction: The orientation_direction of this SlideShowTransition.  # noqa: E501
        :type: str
        """
        if orientation_direction is not None:
            allowed_values = ["Horizontal", "Vertical"]  # noqa: E501
            if orientation_direction.isdigit():
                int_orientation_direction = int(orientation_direction)
                if int_orientation_direction < 0 or int_orientation_direction >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `orientation_direction` ({0}), must be one of {1}"  # noqa: E501
                        .format(orientation_direction, allowed_values)
                    )
                self._orientation_direction = allowed_values[int_orientation_direction]
                return
            if orientation_direction not in allowed_values:
                raise ValueError(
                    "Invalid value for `orientation_direction` ({0}), must be one of {1}"  # noqa: E501
                    .format(orientation_direction, allowed_values)
                )
        self._orientation_direction = orientation_direction

    @property
    def through_black(self):
        """Gets the through_black of this SlideShowTransition.  # noqa: E501

        Through Black.  # noqa: E501

        :return: The through_black of this SlideShowTransition.  # noqa: E501
        :rtype: bool
        """
        return self._through_black

    @through_black.setter
    def through_black(self, through_black):
        """Sets the through_black of this SlideShowTransition.

        Through Black.  # noqa: E501

        :param through_black: The through_black of this SlideShowTransition.  # noqa: E501
        :type: bool
        """
        self._through_black = through_black

    @property
    def corner_and_center_direction(self):
        """Gets the corner_and_center_direction of this SlideShowTransition.  # noqa: E501

        Orientation.  # noqa: E501

        :return: The corner_and_center_direction of this SlideShowTransition.  # noqa: E501
        :rtype: str
        """
        return self._corner_and_center_direction

    @corner_and_center_direction.setter
    def corner_and_center_direction(self, corner_and_center_direction):
        """Sets the corner_and_center_direction of this SlideShowTransition.

        Orientation.  # noqa: E501

        :param corner_and_center_direction: The corner_and_center_direction of this SlideShowTransition.  # noqa: E501
        :type: str
        """
        if corner_and_center_direction is not None:
            allowed_values = ["LeftDown", "LeftUp", "RightDown", "RightUp", "Center"]  # noqa: E501
            if corner_and_center_direction.isdigit():
                int_corner_and_center_direction = int(corner_and_center_direction)
                if int_corner_and_center_direction < 0 or int_corner_and_center_direction >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `corner_and_center_direction` ({0}), must be one of {1}"  # noqa: E501
                        .format(corner_and_center_direction, allowed_values)
                    )
                self._corner_and_center_direction = allowed_values[int_corner_and_center_direction]
                return
            if corner_and_center_direction not in allowed_values:
                raise ValueError(
                    "Invalid value for `corner_and_center_direction` ({0}), must be one of {1}"  # noqa: E501
                    .format(corner_and_center_direction, allowed_values)
                )
        self._corner_and_center_direction = corner_and_center_direction

    @property
    def shred_pattern(self):
        """Gets the shred_pattern of this SlideShowTransition.  # noqa: E501

        Shred Pattern.  # noqa: E501

        :return: The shred_pattern of this SlideShowTransition.  # noqa: E501
        :rtype: str
        """
        return self._shred_pattern

    @shred_pattern.setter
    def shred_pattern(self, shred_pattern):
        """Sets the shred_pattern of this SlideShowTransition.

        Shred Pattern.  # noqa: E501

        :param shred_pattern: The shred_pattern of this SlideShowTransition.  # noqa: E501
        :type: str
        """
        if shred_pattern is not None:
            allowed_values = ["Strip", "Rectangle"]  # noqa: E501
            if shred_pattern.isdigit():
                int_shred_pattern = int(shred_pattern)
                if int_shred_pattern < 0 or int_shred_pattern >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `shred_pattern` ({0}), must be one of {1}"  # noqa: E501
                        .format(shred_pattern, allowed_values)
                    )
                self._shred_pattern = allowed_values[int_shred_pattern]
                return
            if shred_pattern not in allowed_values:
                raise ValueError(
                    "Invalid value for `shred_pattern` ({0}), must be one of {1}"  # noqa: E501
                    .format(shred_pattern, allowed_values)
                )
        self._shred_pattern = shred_pattern

    @property
    def orientation(self):
        """Gets the orientation of this SlideShowTransition.  # noqa: E501

        Orientation.  # noqa: E501

        :return: The orientation of this SlideShowTransition.  # noqa: E501
        :rtype: str
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this SlideShowTransition.

        Orientation.  # noqa: E501

        :param orientation: The orientation of this SlideShowTransition.  # noqa: E501
        :type: str
        """
        if orientation is not None:
            allowed_values = ["Horizontal", "Vertical"]  # noqa: E501
            if orientation.isdigit():
                int_orientation = int(orientation)
                if int_orientation < 0 or int_orientation >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `orientation` ({0}), must be one of {1}"  # noqa: E501
                        .format(orientation, allowed_values)
                    )
                self._orientation = allowed_values[int_orientation]
                return
            if orientation not in allowed_values:
                raise ValueError(
                    "Invalid value for `orientation` ({0}), must be one of {1}"  # noqa: E501
                    .format(orientation, allowed_values)
                )
        self._orientation = orientation

    @property
    def spokes(self):
        """Gets the spokes of this SlideShowTransition.  # noqa: E501

        Spokes.  # noqa: E501

        :return: The spokes of this SlideShowTransition.  # noqa: E501
        :rtype: int
        """
        return self._spokes

    @spokes.setter
    def spokes(self, spokes):
        """Sets the spokes of this SlideShowTransition.

        Spokes.  # noqa: E501

        :param spokes: The spokes of this SlideShowTransition.  # noqa: E501
        :type: int
        """
        self._spokes = spokes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SlideShowTransition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
