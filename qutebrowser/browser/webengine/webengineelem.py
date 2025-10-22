# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:

# Copyright 2016 Florian Bruhin (The Compiler) <mail@qutebrowser.org>
#
# This file is part of qutebrowser.
#
# qutebrowser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# qutebrowser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with qutebrowser.  If not, see <http://www.gnu.org/licenses/>.

# FIXME:qtwebengine remove this once the stubs are gone
# pylint: disable=unused-variable

"""QtWebEngine specific part of the web element API."""

from PyQt5.QtCore import QRect

from qutebrowser.utils import log
from qutebrowser.browser import webelem


class WebEngineElement(webelem.AbstractWebElement):

    """A web element for QtWebEngine, using JS under the hood."""

    def __init__(self, js_dict):
        self._id = js_dict['id']
        self._js_dict = js_dict

    def __eq__(self, other):
        if not isinstance(other, WebEngineElement):
            return NotImplemented
        return self._id == other._id  # pylint: disable=protected-access

    def __getitem__(self, key):
        attrs = self._js_dict['attributes']
        return attrs[key]

    def __setitem__(self, key, val):
        log.stub()

    def __delitem__(self, key):
        log.stub()

    def __iter__(self):
        return iter(self._js_dict['attributes'])

    def __len__(self):
        return len(self._js_dict['attributes'])

    def frame(self):
        log.stub()
        return None

    def geometry(self):
        log.stub()
        return QRect()

    def document_element(self):
        log.stub()
        return None

    def create_inside(self, tagname):
        log.stub()
        return None

    def find_first(self, selector):
        log.stub()
        return None

    def style_property(self, name, *, strategy):
        log.stub()
        return ''

    def classes(self):
        """Get a list of classes assigned to this element."""
        log.stub()
        return []

    def tag_name(self):
        """Get the tag name of this element.

        The returned name will always be lower-case.
        """
        return self._js_dict['tag_name']

    def outer_xml(self):
        """Get the full HTML representation of this element."""
        return self._js_dict['outer_xml']

    def text(self, *, use_js=False):
        """Get the plain text content for this element.

        Args:
            use_js: Whether to use javascript if the element isn't
                    content-editable.
        """
        if use_js:
            # FIXME:qtwebengine what to do about use_js with WebEngine?
            log.stub('with use_js=True')
        return self._js_dict.get('text', '')

    def set_text(self, text, *, use_js=False):
        """Set the given plain text.

        Args:
            use_js: Whether to use javascript if the element isn't
                    content-editable.
        """
        # FIXME:qtwebengine what to do about use_js with WebEngine?
        log.stub()

    def set_inner_xml(self, xml):
        """Set the given inner XML."""
        # FIXME:qtwebengine get rid of this?
        log.stub()

    def remove_from_document(self):
        """Remove the node from the document."""
        # FIXME:qtwebengine get rid of this?
        log.stub()

    def set_style_property(self, name, value):
        """Set the element style."""
        # FIXME:qtwebengine get rid of this?
        log.stub()

    def run_js_async(self, code, callback=None):
        """Run the given JS snippet async on the element."""
        # FIXME:qtwebengine get rid of this?
        log.stub()

    def parent(self):
        """Get the parent element of this element."""
        # FIXME:qtwebengine get rid of this?
        log.stub()
        return None

    def rect_on_view(self, *, elem_geometry=None, adjust_zoom=True,
                     no_js=False):
        """Get the geometry of the element relative to the webview.

        Uses the getClientRects() JavaScript method to obtain the collection of
        rectangles containing the element and returns the first rectangle which
        is large enough (larger than 1px times 1px). If all rectangles returned
        by getClientRects() are too small, falls back to elem.rect_on_view().

        Skipping of small rectangles is due to <a> elements containing other
        elements with "display:block" style, see
        https://github.com/The-Compiler/qutebrowser/issues/1298

        Args:
            elem_geometry: The geometry of the element, or None.
                           Calling QWebElement::geometry is rather expensive so
                           we want to avoid doing it twice.
            adjust_zoom: Whether to adjust the element position based on the
                         current zoom level.
            no_js: Fall back to the Python implementation
        """
        log.stub()
        return QRect()

    def is_visible(self, mainframe):
        """Check if the given element is visible in the given frame."""
        # FIXME:qtwebengine get rid of this?
        log.stub()
        return True
