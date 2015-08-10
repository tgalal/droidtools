import os
import sys
import mkbootimg

if sys.version_info >= (3,0):
    unicode = str

class BootImg(object):

    def __init__(self,
                 board=None, base=None, cmdline=None, page_size=None,
                 kernel_offset=None, ramdisk_offset=None, second_offset=None,
                 tags_offset=None, kernel=None, ramdisk=None, second=None, dt=None,
                 signature=None):

        self.board = board
        self.base = base
        self.cmdline = cmdline
        self.page_size = page_size
        self.kernel_offset = kernel_offset
        self.ramdisk_offset = ramdisk_offset
        self.second_offset = second_offset
        self.tags_offset = tags_offset
        self.kernel = kernel
        self.ramdisk = ramdisk
        self.second = second
        self.dt = dt
        self.signature = signature

    def __int_address(self, addr):
        if addr is None:
            return None

        return int(addr, 16) if type(addr) in (str, unicode) else addr

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, value):
        self._board = value

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        self._base = self.__int_address(value)

    @property
    def cmdline(self):
        return self._cmdline

    @cmdline.setter
    def cmdline(self, value):
        self._cmdline = value

    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = int(value) if value is not None else None

    @property
    def kernel_offset(self):
        return self._kernel_offset

    @kernel_offset.setter
    def kernel_offset(self, value):
        self._kernel_offset = self.__int_address(value)

    @property
    def ramdisk_offset(self):
        return self._ramdisk_offset

    @ramdisk_offset.setter
    def ramdisk_offset(self, value):
        self._ramdisk_offset = self.__int_address(value)

    @property
    def second_offset(self):
        return self._second_offset

    @second_offset.setter
    def second_offset(self, value):
        self._second_offset = self.__int_address(value)

    @property
    def tags_offset(self):
        return self._tags_offset

    @tags_offset.setter
    def tags_offset(self, value):
        self._tags_offset = self.__int_address(value)

    @property
    def kernel(self):
        return self._kernel

    @kernel.setter
    def kernel(self, value):
        self._kernel = value

    @property
    def ramdisk(self):
        return self._ramdisk

    @ramdisk.setter
    def ramdisk(self, value):
        self._ramdisk = value

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, value):
        self._second = value

    @property
    def second_size(self):
        return os.path.getsize(self._second) if self._second and os.path.exists(self._second) else 0

    @property
    def dt(self):
        return self._dt

    @property
    def dt_size(self):
        return os.path.getsize(self._dt) if self._dt and os.path.exists(self._dt) else 0

    @dt.setter
    def dt(self, value):
        self._dt = value

    @property
    def signature(self):
        return self._signature

    @signature.setter
    def signature(self, value):
        self._signature = value

    def build(self, filename, mode=mkbootimg.MODE_STANDARD):
        import mkbootimg
        mkbootimg.build(
            filename,
            self.board,
            self.base,
            self.cmdline,
            self.page_size,
            self.kernel_offset,
            self.ramdisk_offset,
            self.second_offset,
            self.tags_offset,
            self.kernel,
            self.ramdisk,
            self.second,
            self.dt,
            self.signature
        )

    def __str__(self):
        out = "BOARD_KERNEL_CMDLINE %s\n" % self.cmdline
        out += "BOARD_KERNEL_BASE %08x\n" % self.base
        out += "BOARD_RAMDISK_OFFSET %08x\n" % self.ramdisk_offset
        out += "BOARD_SECOND_OFFSET %08x\n" % self.second_offset
        out += "BOARD_TAGS_OFFSET %08x\n" % self.tags_offset
        out += "BOARD_PAGE_SIZE %s\n" % self.page_size
        out += "BOARD_SECOND_SIZE %s\n" % self.second_size
        out += "BOARD_DT_SIZE %s" % self.dt_size

        return out