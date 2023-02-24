from datetime import date
from tkinter import *
from tkinter import ttk

from commons.const import *


class Ledger(Toplevel):
    """元帳
    Attributes:

    """

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        # Set title of the window
        self.title("元帳")

        # >>>>>DEBUG>>>>>
        ttk.Label(self, text="Ledger(元帳ウィンドウ)", padding=40, font=FONT_FIXED_24).grid()
        # <<<<<DEBUG<<<<<


class JournalEntry(Toplevel):
    """仕訳帳ウィンドウ
    Attributes:

    """

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        # Set title of the window
        self.title("仕訳帳原簿")

        # >>>>>DEBUG>>>>>
        ttk.Label(self, text="JournalEntry(仕訳帳ウィンドウ)", padding=40, font=FONT_FIXED_24).grid()
        # <<<<<DEBUG<<<<<


class TransferSlip(Toplevel):
    """振替伝票ウィンドウ
    Attributes:

    """

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        # Variables
        self.var_date = StringVar()  # variable for date label
        self.var_date.set(date.today())  # initial value

        # Set title of the window
        self.title("振替伝票")

        # Widgets
        fr_outer = ttk.Frame(self)
        fr_title = ttk.Frame(fr_outer, width=630, height=105, borderwidth=2, relief=SOLID)
        lbl_title = ttk.Label(fr_title, text="振 替 伝 票", font=FONT_FIXED_30, anchor=CENTER)
        fr_date = ttk.Frame(fr_outer, width=500, borderwidth=2, relief=SOLID)
        self.lbl_date = ttk.Label(fr_date, textvariable=self.var_date, font=FONT_FIXED_24, anchor=CENTER)
        fr_pic = ttk.Frame(fr_outer, width=150, borderwidth=2, relief=SOLID)

        # Geometry management
        self.geometry("1280x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        fr_outer.grid(column=0, row=0)
        fr_title.grid(column=0, row=0, columnspan=3, rowspan=2)
        lbl_title.grid()
        fr_date.grid(column=3, row=0, columnspan=3, rowspan=2)
        self.lbl_date.grid()
        fr_pic.grid(column=6, row=0, rowspan=2)
