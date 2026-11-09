import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import speedtest


class NetworkMethods:
    @staticmethod
    def perform_speedtest():
        download_result = "512"
        upload_result = "122"
        ping_result = "7"

        return download_result, upload_result, ping_result


'''class ThemeManager:
    LIGHT_THEME = "vapor-light"
    DARK_THEME = "vapor-dark"

    @staticmethod
    def toggle_theme():
        style = ttk.Style()
        style.theme_use(ThemeManager.LIGHT_THEME if style.theme.name == ThemeManager.DARK_THEME else ThemeManager.DARK_THEME)'''


class MainWindow(ttk.Window):
    def __init__(self):
        super().__init__(title="NetworkHub", themename="vapor-dark", size=(700, 500))

        self.minsize(700, 500)
        self.columnconfigure(0, weight=1)

        self.style_ref = ttk.Style()

        heading_frame = HeadingFrame(self, style_ref=self.style_ref)
        heading_frame.grid(row=0, column=0, sticky=EW)

        self.speedtest_frame = SpeedtestFrame(self, on_start=self.on_start_button, style_ref=self.style_ref)
        self.speedtest_frame.grid(row=1, column=0, sticky=EW, pady=15)

        separator = ttk.Separator(self)
        separator.grid(row=2, column=0, columnspan=3, sticky=EW)

    def on_start_button(self):
        # run test
        results = NetworkMethods.perform_speedtest()

        # set values
        self.speedtest_frame.download_frame.value.set(results[0])
        self.speedtest_frame.upload_frame.value.set(results[1])
        self.speedtest_frame.ping_frame.value.set(results[2])


class HeadingFrame(ttk.Frame):
    def __init__(self, parent, style_ref):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)

        self.style = style_ref

        speed_label = ttk.Label(self, text="INTERNET SPEED", font=("Segoe UI Variable Text", 16, "bold"))
        speed_label.grid(row=0, column=0, sticky=W, padx=15, pady=15)

        # different button icons for both modes
        self.theme_icon_light = ttk.Icon("brightness-high-fill", size=27, color="#ffffff")
        self.theme_icon_dark = ttk.Icon("moon-fill", size=27, color="#190831")

        self.theme_button = ttk.Button(self, image=self.theme_icon_light, bootstyle="link", cursor="hand2",
                                       command=self.toggle_theme)
        self.theme_button.grid(row=0, column=1, sticky=E, padx=15, pady=15)

    def toggle_theme(self):
        if self.style.theme.name == "vapor-dark":
            self.style.theme_use("vapor-light")
            self.theme_button.configure(image=self.theme_icon_dark)

        else:
            self.style.theme_use("vapor-dark")
            self.theme_button.configure(image=self.theme_icon_light)


class SpeedtestFrame(ttk.Frame):
    def __init__(self, parent, on_start, style_ref):
        super().__init__(parent)

        for column in range(3):
            self.columnconfigure(column, weight=1)

        # implement all three main speedtest values from class MetricFrame to avoid redundancy
        self.download_frame = MetricFrame(self, title="Download", icon="download", color="#42f5a4", unit="Mbit/s")
        self.download_frame.grid(row=0, column=0, sticky=N)

        self.upload_frame = MetricFrame(self, title="Upload", icon="upload", color="#4251f5", unit="Mbit/s")
        self.upload_frame.grid(row=0, column=1, sticky=N)

        self.ping_frame = MetricFrame(self, title="Ping", icon="activity", color="#f55142", unit="ms")
        self.ping_frame.grid(row=0, column=2, sticky=N)

        self.action_frame = ActionFrame(self, on_start, style_ref)
        self.action_frame.grid(row=1, column=0, columnspan=3, pady=(35, 15))


class MetricFrame(ttk.Frame):
    def __init__(self, parent, title, icon, color, unit):
        super().__init__(parent)

        # data to be shown
        self.value = ttk.StringVar(value="-")

        # icon
        self.icon = ttk.Icon(icon, size=45, color=color)
        self.icon_label = ttk.Label(self, image=self.icon)
        self.icon_label.grid(row=0, column=0, pady=10)

        # measured value
        self.value_label = ttk.Label(self, textvariable=self.value, font=("Segoe UI Variable Text", 17))
        self.value_label.grid(row=1, column=0, sticky=W, pady=(0, 5))

        self.unit_label = ttk.Label(self, text=unit, font=("Segoe UI Variable Text", 12, "bold"), foreground="#a39f9e")
        self.unit_label.grid(row=2, column=0, sticky=W)

        # value description
        self.description_label = ttk.Label(self, text=title, font=("Segoe UI Variable Text", 12, "bold"))
        self.description_label.grid(row=3, column=0, sticky=W)


class ActionFrame(ttk.Frame):
    def __init__(self, parent, on_start, style_ref):
        super().__init__(parent)

        self.UNI_CODE = "\u25B6"
        self.SPACE = " " * 3

        '''self.style = style_ref
        self.style.configure("StartButton.TButton", font=("Segoe UI Variable Text", 12, "bold"))


        start_button = ttk.Button(self, text=f"{self.UNI_CODE}{self.SPACE}START SPEEDTEST", style="StartButton.TButton", cursor="hand2", command=on_start)'''
        start_button = ttk.Button(self, text=f"{self.UNI_CODE}{self.SPACE}START SPEEDTEST", bootstyle="link",
                                  cursor="hand2", command=on_start)
        start_button.grid(row=0, column=0, pady=(0, 5))


app = MainWindow()

app.mainloop()

