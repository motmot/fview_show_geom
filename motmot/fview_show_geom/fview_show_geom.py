from __future__ import with_statement, division

import pkg_resources
import warnings, threading

import numpy as np

from motmot.fview.traited_plugin import *
from motmot.fview.utils import lineseg_circle, lineseg_box

class FviewShowGeom(HasTraits_FViewPlugin):
    plugin_name = 'show geom'

    enabled = traits.Bool(False)

    traits_view = View(Group(
                        Group(
                            Item(name='enabled'),
                        ),
    ))

    def __init__(self,wx_parent,fview_options):
        super(FviewShowGeom, self).__init__(wx_parent)

        self._wx_parent = wx_parent

        self._pts = None
        self._subpts = None

        if fview_options.get('have_ros'):

            import roslib;
            roslib.load_manifest('rospy')
            roslib.load_manifest('geometry_msgs')
            import rospy
            import geometry_msgs.msg

            self._subpts = rospy.Publisher('/flymad/geom_poly',
                                        geometry_msgs.msg.Polygon,
                                        self._on_geom_poly)

    def _on_geom_poly(self, msg):
        self._pts = msg.points

    def _show_linesegs(self):
        show_linesegs = []

        if self.enabled:
            if self._pts is not None:
                show_linesegs.extend( [(pt.x,pt.y) for pt in self._pts] )

        return show_linesegs

    def camera_starting_notification(self,cam_id,
                                     pixel_format=None,
                                     max_width=None,
                                     max_height=None):
        pass


    def process_frame(self, cam_id, buf, buf_offset, timestamp, framenumber):
        return [], [(14,18),(69,87)]#self._show_linesegs()

