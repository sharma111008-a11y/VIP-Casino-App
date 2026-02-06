# --- VIP CASINO MASTER CODE ---
ADMIN_ID = "3603236032"
ADMIN_PASS = "J1a2y3a4"

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import random

class VIPCasino(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Header
        self.lbl = Label(text="🎰 VIP CASINO AUTO-MODE", font_size='24sp', color=(1, 0.8, 0, 1))
        self.layout.add_widget(self.lbl)
        
        # Game Table
        self.table = Label(text="Dragon vs Tiger", font_size='30sp')
        self.layout.add_widget(self.table)

        # Betting Buttons
        btn_box = BoxLayout(spacing=10)
        btn_box.add_widget(Button(text="DRAGON", background_color=(1, 0, 0, 1)))
        btn_box.add_widget(Button(text="TIGER", background_color=(1, 1, 0, 1)))
        self.layout.add_widget(btn_box)
        
        # Coin Info
        self.info = Label(text="Min: ₹10 | Max: ₹50,000", font_size='15sp')
        self.layout.add_widget(self.info)

        return self.layout

if __name__ == "__main__":
    VIPCasino().run()
