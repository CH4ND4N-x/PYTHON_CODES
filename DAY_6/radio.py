#radio
class radio:
    color="mate black"
    brand="philips"
    ACPower=False
    headphone=True
    
    def __init__(self):
        self.power_led=None
        self.mode_led=None
        self.frequency=0.0
        self.volume=0
        print("_______ready to start________")
    def power_switch(self,power_status):
        self.power_led=power_status
        print("Radio is ->"+power_status) 
    def mode_switch(self,mode_status):
        self.mode_led=mode_status
        print("Radio set in Mode ->"+mode_status)
    def band_tuner(self,freq):
        self.frequency=freq
        print("Radio set at frequency ->",freq)
    def volume_tuner(self,vol):
        self.volume=vol
        print("Volume set at ->",vol)
        
national_radio=radio()
national_radio.power_switch("ON")
national_radio.mode_switch("FM")
national_radio.band_tuner(93.8)
national_radio.volume_tuner(100)        