from tkinter import *
from tkinter import ttk

from windows import Ledger
from windows import JournalEntry
from windows import TransferSlip


class App(Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Widgets
        # Button to create a ledger window
        self.btn_ledger = ttk.Button(self, text="元帳", command=lambda: Ledger(self))
        # Button to create a journal entry window
        self.btn_jentry = ttk.Button(self, text="仕訳帳", command=lambda: JournalEntry(self))
        # Button to create a transfer slip window
        self.btn_tslip = ttk.Button(self, text="振替伝票", command=lambda: TransferSlip(self))

        # Geometry management
        self.btn_ledger.grid(padx=10, pady=5)
        self.btn_jentry.grid(padx=10, pady=5)
        self.btn_tslip.grid(padx=10, pady=5)


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
