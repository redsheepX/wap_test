class emulator:
    iPhone_XR = "iPhone XR"
    iPhone_12_Pro = "iPhone 12 Pro"
    iPhone_14_Pro_Max = "iPhone 14 Pro Max"
    Pixel_7 = "Pixel 7"
    Samsung_Galaxy_S8_Plus = "Samsung Galaxy S8+"
    Samsung_Galaxy_S20_Ultra = "Samsung Galaxy S20 Ultra"

    def get_all_devices(self):
        return [
            {"deviceName": self.iPhone_XR},
            {"deviceName": self.iPhone_12_Pro},
            {"deviceName": self.iPhone_14_Pro_Max},
            {"deviceName": self.Pixel_7},
            {"deviceName": self.Samsung_Galaxy_S8_Plus},
            {"deviceName": self.Samsung_Galaxy_S20_Ultra},
        ]
