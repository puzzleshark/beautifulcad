from beautifulcad.context import Context

from cadquery.occ_impl.shapes import Solid as CQSolid
from cadquery.occ_impl.shapes import Face as CQFace
import jupyter_cadquery

class Box:

    def __init__(self, l, w, h):
        self.ctx = Context.current()
        self._box = CQSolid.makeBox(l, w, h)
    
    def faces(self):
        return [Face(f) for f in self._box.Faces()]
    
    def _ipython_display_(self):
        return jupyter_cadquery.Part(self._box).show()


class Face:

    def __init__(self, cq_face):
        self.ctx = Context.current()
        self._face = cq_face

    def _ipython_display_(self):
        return jupyter_cadquery.Part(self._face).show()