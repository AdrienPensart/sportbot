from colorama import Fore


class Exercice:
    def __init__(self, label, duration, silence=False, intensity=10, color=Fore.RESET):
        self.intensity = intensity
        self.label = label
        self.duration = duration
        self.stopwatch = duration
        self.color = color
        self.silence = silence

    def __repr__(self):
        return f"{self.color}{self.label} : {self.stopwatch} / {self.duration}{Fore.RESET}"
